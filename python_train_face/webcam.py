import uuid
import cv2
import numpy as np
from mtcnn import MTCNN
import tensorflow as tf
import os

from sklearn.preprocessing import LabelEncoder
from dao import AttendancesDAO, StudentDAO
from models.Students import Student
from models.Attendances import Attendances

IMG_SIZE = 160
# Get the directory of the current file
CURRENT_DIR = os.path.dirname(os.path.abspath(__file__))
MODEL_PATH = os.path.join(CURRENT_DIR, "face_recognition_model.h5")
LABEL_PATH = os.path.join(CURRENT_DIR, "labels.npy")

# Load model đã train
model = tf.keras.models.load_model(MODEL_PATH)
labels = np.load(LABEL_PATH)
le = LabelEncoder()
le.classes_ = labels

# Khởi tạo MTCNN
detector = MTCNN()

def predict_face(face_img):
    try:
        # Resize và chuẩn hóa ảnh
        face = cv2.resize(face_img, (IMG_SIZE, IMG_SIZE))
        face = face.astype("float32") / 255.0
        face = np.expand_dims(face, axis=0)

        # Dự đoán
        preds = model.predict(face)[0]
        class_index = np.argmax(preds)
        confidence = preds[class_index]
        name = le.inverse_transform([class_index])[0]
        return name, confidence
    except:
        return "unknown", 0.0

def detect_face_from_webcam_mtcnn():
    cap = cv2.VideoCapture(0)

    if not cap.isOpened():
        print("Không thể mở webcam")
        return
    detected_names = []
    while True:
        ret, frame = cap.read()
        if not ret:
            print("Không thể đọc khung hình")
            break

        img_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        faces = detector.detect_faces(img_rgb)
        recognized_faces = []
        for face in faces:
            x, y, w, h = face['box']
            x, y = max(0, x), max(0, y)
            face_img = frame[y:y+h, x:x+w]

            name, confidence = predict_face(face_img)

            # Vẽ khung và tên
            cv2.rectangle(frame, (x, y), (x+w, y+h), (255, 0, 0), 2)
            cv2.putText(frame, f"{name} ({confidence:.2f})", (x, y - 10),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.8, (255, 0, 0), 2)
            recognized_faces.append((name, confidence))
        for name, confidence in recognized_faces:
            if name not in detected_names:  # Kiểm tra xem tên đã được nhận diện chưa
                detected_names.append(name)  # Thêm tên vào danh sách đã nhận diện
                save_to_db(name, confidence)  # Lưu vào DB


        cv2.imshow("Webcam - Face Recognition (MTCNN)", frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()

def generate_unique_id():
    return int(uuid.uuid4().int % (2**29))
def save_to_db(name, confidence):
    print(f"Lưu vào DB: {name} - {confidence:.2f}")
    name_student, student_id = name.split('_')
    student= StudentDAO.get_by_id(student_id)
    if student:
        attendance = Attendances(id=generate_unique_id(),student_id=student.id,scheduledetail_id=1, status=1)
        AttendancesDAO.save(attendance)
       
    

#detect_face_from_webcam_mtcnn()

