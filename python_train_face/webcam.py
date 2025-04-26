import cv2
import numpy as np
from mtcnn import MTCNN
import tensorflow as tf

from sklearn.preprocessing import LabelEncoder

IMG_SIZE = 160
MODEL_PATH = "face_recognition_model.h5"
LABEL_PATH = "labels.npy"

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

    while True:
        ret, frame = cap.read()
        if not ret:
            print("Không thể đọc khung hình")
            break

        img_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        faces = detector.detect_faces(img_rgb)

        for face in faces:
            x, y, w, h = face['box']
            x, y = max(0, x), max(0, y)
            face_img = frame[y:y+h, x:x+w]

            name, confidence = predict_face(face_img)

            # Vẽ khung và tên
            cv2.rectangle(frame, (x, y), (x+w, y+h), (255, 0, 0), 2)
            cv2.putText(frame, f"{name} ({confidence:.2f})", (x, y - 10),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.8, (255, 0, 0), 2)

        cv2.imshow("Webcam - Face Recognition (MTCNN)", frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()
detect_face_from_webcam_mtcnn()