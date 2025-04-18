# webcam_detection.py
import cv2
import numpy as np
import os
from face_detection import detect_skin, find_face_candidates, predict_face  # Import các hàm từ detection.py

# Hàm phát hiện khuôn mặt từ webcam
def detect_face_from_webcam():
    cap = cv2.VideoCapture(0)

    # Đảm bảo webcam mở được
    if not cap.isOpened():
        print("Không thể mở webcam")
        exit()

    while True:
        ret, frame = cap.read()
        if not ret:
            print("Không thể đọc khung hình từ webcam")
            break
        
        # Phát hiện vùng da
        skin_mask = detect_skin(frame)
        candidates = find_face_candidates(frame, skin_mask)

        for (x, y, w, h) in candidates:
            # Vẽ khung xung quanh khuôn mặt
            cv2.rectangle(frame, (x, y), (x+w, y+h), (255, 0, 0), 2)
            
            # Cắt khuôn mặt ra để dự đoán
            face = frame[y:y+h, x:x+w]
            
            name, confidence = predict_face(face)
            cv2.putText(frame, f"{name} ({confidence:.2f})", (x, y - 10),
                cv2.FONT_HERSHEY_SIMPLEX, 0.9, (255, 0, 0), 2)

        
        # Hiển thị kết quả
        cv2.imshow('Webcam - Nhận diện khuôn mặt', frame)
        
        # Thoát khi nhấn phím 'q'
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    
    # Giải phóng webcam và đóng cửa sổ
    cap.release()
    cv2.destroyAllWindows()

# Gọi hàm phát hiện khuôn mặt từ webcam
detect_face_from_webcam()
