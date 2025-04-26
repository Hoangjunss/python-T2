from mtcnn import MTCNN
import cv2
import os

detector = MTCNN()  # Khởi tạo MTCNN một lần

def save_faces_mtcnn(img, mtcnn_faces, save_dir, img_basename="image"):
    """Lưu các khuôn mặt được MTCNN phát hiện"""
    if not os.path.exists(save_dir):
        os.makedirs(save_dir)

    for i, face in enumerate(mtcnn_faces):
        x, y, w, h = face['box']
        x, y = max(0, x), max(0, y)
        face_img = img[y:y+h, x:x+w]

        # Dùng tên ảnh gốc làm prefix để không bị trùng
        face_filename = os.path.join(save_dir, f"{img_basename}_face_{i}.jpg")
        cv2.imwrite(face_filename, face_img)

    print(f"Đã lưu {len(mtcnn_faces)} khuôn mặt vào {save_dir}")


def detect_faces_in_folder(image_folder, output_folder):
    print("detect_faces_in_folder bắt đầu")

    if not os.path.exists(image_folder):
        print("Thư mục ảnh không tồn tại.")
        return

    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    for user_id in os.listdir(image_folder):
        print(f"Đang xử lý người dùng: {user_id}")
        user_folder = os.path.join(image_folder, user_id)
        
        if not os.path.isdir(user_folder):
            continue

        user_face_folder = os.path.join(output_folder, user_id)
        if not os.path.exists(user_face_folder):
            os.makedirs(user_face_folder)

        for img_name in os.listdir(user_folder):
            print(f"  -> Xử lý ảnh: {img_name}")
            img_path = os.path.join(user_folder, img_name)
            img = cv2.imread(img_path)
            if img is None:
                print("    -> Không đọc được ảnh.")
                continue

            img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
            mtcnn_faces = detector.detect_faces(img_rgb)

            if not mtcnn_faces:
                print("    -> Không phát hiện khuôn mặt.")
                continue

            img_name_wo_ext = os.path.splitext(img_name)[0]  # bỏ phần mở rộng
            save_faces_mtcnn(img, mtcnn_faces, user_face_folder, img_name_wo_ext)

image_folder = "image"
output_folder = "faces"
detect_faces_in_folder(image_folder, output_folder)