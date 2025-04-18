import os
import cv2
import numpy as np
import tensorflow as tf

IMG_SIZE = 160  # Kích thước ảnh chuẩn
model = tf.keras.models.load_model("face_recognition_model.h5")
labels = np.load("labels.npy")
def predict_face(face_img):
    """
    Nhận diện khuôn mặt từ ảnh (numpy array).
    Trả về: tên (ID) và độ tin cậy.
    """
    try:
        # Resize và chuẩn hóa
        img = cv2.resize(face_img, (IMG_SIZE, IMG_SIZE))
        img = img / 255.0
        img = np.expand_dims(img, axis=0)  # [1, 160, 160, 3]

        # Dự đoán
        pred = model.predict(img, verbose=0)
        idx = np.argmax(pred)
        name = labels[idx]
        confidence = np.max(pred)
        return name, confidence
    except Exception as e:
        print("Lỗi dự đoán:", e)
        return "Unknown", 0.0

def detect_skin(img):
    """ Phát hiện vùng da trong ảnh """
    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    lower_skin = np.array([0, 20, 70], dtype=np.uint8)
    upper_skin = np.array([20, 255, 255], dtype=np.uint8)
    mask = cv2.inRange(hsv, lower_skin, upper_skin)
    mask = cv2.GaussianBlur(mask, (5, 5), 0)
    return mask

def is_eyes_dark(img, x, y, w, h):
    print("is_eyes_dark")

    """ Kiểm tra độ tối của mắt trong khuôn mặt """
    face_roi = img[y:y+h, x:x+w]
    gray_face = cv2.cvtColor(face_roi, cv2.COLOR_BGR2GRAY)
    eye_region = gray_face[10:int(h/2), 10:int(w-10)]  # Vùng mắt
    avg_brightness = np.mean(eye_region)
    print("is_eyes_dark avg_brightness: ", avg_brightness)

    return avg_brightness < 100  

def is_forehead_brighter_than_chin(img, x, y, w, h):
    print("is_forehead_brighter_than_chin")
    """ Kiểm tra độ sáng giữa trán và cằm """
    gray_face = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    forehead = gray_face[y:y+int(h/3), x:x+w]  # Trán
    chin = gray_face[y+int(h/3):y+h, x:x+w]  # Cằm
    avg_forehead = np.mean(forehead)
    avg_chin = np.mean(chin)
    print("is_forehead_brighter_than_chin: ", avg_forehead, avg_chin)
    return avg_forehead < avg_chin

def find_face_candidates(img, skin_mask):
    print("find_face_candidates")
    """ Tìm và lọc các khuôn mặt từ mask """
    contours, _ = cv2.findContours(skin_mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    face_candidates = []

    for cnt in contours:
        print("find_face_candidates:", cnt)
        area = cv2.contourArea(cnt)
        if area < 1000: continue  # Bỏ qua các vùng nhỏ

        x, y, w, h = cv2.boundingRect(cnt)
        aspect_ratio = w / float(h)
        if 0.75 < aspect_ratio < 1.4:  # Tỷ lệ khuôn mặt hợp lý
            print("find_face_candidates if 0.75")
            if is_forehead_brighter_than_chin(img, x, y, w, h):
                print("find_face_candidates if is_eyes_dark")
                face_candidates.append((x, y, w, h))

    return face_candidates

def save_faces(img, candidates, save_dir):
    print("save_faces")
    """ Lưu các khuôn mặt phát hiện được thành ảnh """
    if not os.path.exists(save_dir):
        print("save_faces not os.path.exists")
        os.makedirs(save_dir)

    for i, (x, y, w, h) in enumerate(candidates):
        print("save_faces: ", i, (x, y, w, h))
        face = img[y:y+h, x:x+w]
        face_filename = os.path.join(save_dir, f"face_{i}.jpg")
        cv2.imwrite(face_filename, face)
    print(f"Lưu {len(candidates)} khuôn mặt vào thư mục {save_dir}")

def detect_faces_in_folder(image_folder, output_folder):
    print("detect_faces_in_folder: 62")
    """ Phát hiện khuôn mặt trong tất cả các ảnh trong folder """
    if not os.path.exists(image_folder):
        print("detect_faces_in_folder not os.path.exists(image_folder)")
        os.makedirs(image_folder)

    if not os.path.exists(output_folder):
        print("detect_faces_in_folder not os.path.exists(output_folder)")
        os.makedirs(output_folder)

    if not os.listdir(image_folder):
        print("detect_faces_in_folder not os.listdir(image_folder)")

    for user_id in os.listdir(image_folder):
        print("detect_faces_in_folder user_id in os.listdir(image_folder): ", user_id)
        user_folder = os.path.join(image_folder, user_id)
        
        if not os.path.isdir(user_folder):
            print("detect_faces_in_folder not os.path.isdir(user_folder)")
            continue
        
        # Tạo thư mục cho mỗi user trong folder face
        user_face_folder = os.path.join(output_folder, user_id)
        if not os.path.exists(user_face_folder):
            print("detect_faces_in_folder not os.path.exists(user_face_folder)")
            os.makedirs(user_face_folder)
        
        # Lặp qua tất cả các ảnh của user
        for img_name in os.listdir(user_folder):
            print("detect_faces_in_folder: ", img_name)

            img_path = os.path.join(user_folder, img_name)
            img = cv2.imread(img_path)
            if img is None:
                continue
            
            # Phát hiện khuôn mặt
            skin_mask = detect_skin(img)
            face_candidates = find_face_candidates(img, skin_mask)
            
            # Lưu các khuôn mặt phát hiện được
            save_faces(img, face_candidates, user_face_folder)

# Ví dụ sử dụng:
image_folder = "image"  # Thư mục chứa các folder của từng user (name_id)
output_folder = "faces"  # Thư mục để lưu các khuôn mặt đã phát hiện
def detect_faces():
    detect_faces_in_folder(image_folder, output_folder)
