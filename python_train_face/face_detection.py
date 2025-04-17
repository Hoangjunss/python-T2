import os
import cv2
import numpy as np

IMG_SIZE = 160  # Kích thước ảnh chuẩn

def detect_skin(img):
    """ Phát hiện vùng da trong ảnh """
    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    lower_skin = np.array([0, 20, 70], dtype=np.uint8)
    upper_skin = np.array([20, 255, 255], dtype=np.uint8)
    mask = cv2.inRange(hsv, lower_skin, upper_skin)
    mask = cv2.GaussianBlur(mask, (5, 5), 0)
    return mask

def is_eyes_dark(img, x, y, w, h):
    """ Kiểm tra độ tối của mắt trong khuôn mặt """
    face_roi = img[y:y+h, x:x+w]
    gray_face = cv2.cvtColor(face_roi, cv2.COLOR_BGR2GRAY)
    eye_region = gray_face[10:int(h/2), 10:int(w-10)]  # Vùng mắt
    avg_brightness = np.mean(eye_region)
    return avg_brightness < 100  

def is_forehead_brighter_than_chin(img, x, y, w, h):
    """ Kiểm tra độ sáng giữa trán và cằm """
    gray_face = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    forehead = gray_face[y:y+int(h/3), x:x+w]  # Trán
    chin = gray_face[y+int(h/3):y+h, x:x+w]  # Cằm
    avg_forehead = np.mean(forehead)
    avg_chin = np.mean(chin)
    return avg_forehead > avg_chin

def find_face_candidates(img, skin_mask):
    """ Tìm và lọc các khuôn mặt từ mask """
    contours, _ = cv2.findContours(skin_mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    face_candidates = []

    for cnt in contours:
        area = cv2.contourArea(cnt)
        if area < 1000: continue  # Bỏ qua các vùng nhỏ

        x, y, w, h = cv2.boundingRect(cnt)
        aspect_ratio = w / float(h)
        if 0.75 < aspect_ratio < 1.4:  # Tỷ lệ khuôn mặt hợp lý
            if is_eyes_dark(img, x, y, w, h) and is_forehead_brighter_than_chin(img, x, y, w, h):
                face_candidates.append((x, y, w, h))

    return face_candidates

def save_faces(img, candidates, save_dir):
    """ Lưu các khuôn mặt phát hiện được thành ảnh """
    if not os.path.exists(save_dir):
        os.makedirs(save_dir)

    for i, (x, y, w, h) in enumerate(candidates):
        face = img[y:y+h, x:x+w]
        face_filename = os.path.join(save_dir, f"face_{i}.jpg")
        cv2.imwrite(face_filename, face)
    print(f"Lưu {len(candidates)} khuôn mặt vào thư mục {save_dir}")

def detect_faces_in_folder(image_folder, output_folder):
    """ Phát hiện khuôn mặt trong tất cả các ảnh trong folder """
    if not os.path.exists(image_folder):
        os.makedirs(image_folder)

    if not os.path.exists(output_folder):
        os.makedirs(output_folder)
    for user_id in os.listdir(image_folder):
        user_folder = os.path.join(image_folder, user_id)
        
        if not os.path.isdir(user_folder):
            continue
        
        # Tạo thư mục cho mỗi user trong folder face
        user_face_folder = os.path.join(output_folder, user_id)
        if not os.path.exists(user_face_folder):
            os.makedirs(user_face_folder)
        
        # Lặp qua tất cả các ảnh của user
        for img_name in os.listdir(user_folder):
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

detect_faces_in_folder(image_folder, output_folder)
