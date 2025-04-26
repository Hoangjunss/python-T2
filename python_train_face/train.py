import os
import cv2
import numpy as np
import tensorflow as tf
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split

IMG_SIZE = 160  # Kích thước ảnh chuẩn
FACES_DIR = "faces"  # Thư mục chứa các ảnh khuôn mặt của mỗi user

# Tải dữ liệu từ thư mục chứa ảnh khuôn mặt
def load_faces_data(faces_dir):
    print("load_faces_data")
    X, y = [], []
    
    for user_id in os.listdir(faces_dir):
        print("load_faces_data user_id: ", user_id)

        user_folder = os.path.join(faces_dir, user_id)
        
        if not os.path.isdir(user_folder):
            continue
        
        # Lặp qua các ảnh trong thư mục của từng user
        for img_name in os.listdir(user_folder):
            print("load_faces_data img_name: ", img_name)

            img_path = os.path.join(user_folder, img_name)
            img = cv2.imread(img_path)
            if img is None:
                continue
            
            # Resize ảnh và chuẩn hóa
            img = cv2.resize(img, (IMG_SIZE, IMG_SIZE))
            img = img / 255.0  # Chuẩn hóa ảnh (giảm giá trị từ 0-255 về 0-1)
            X.append(img)
            y.append(user_id)  # Gắn nhãn là user_id
            print("load_faces_data X Y : ", X, y)

    
    return np.array(X), np.array(y)

# Tải dữ liệu và mã hóa nhãn
X, y = load_faces_data(FACES_DIR)

# Mã hóa nhãn user_id thành số
le = LabelEncoder()
y_encoded = le.fit_transform(y)

# Lưu các nhãn để sử dụng khi dự đoán
np.save("labels.npy", le.classes_)

# Chia dữ liệu thành tập huấn luyện và kiểm tra
X_train, X_test, y_train, y_test = train_test_split(X, y_encoded, test_size=0.2, random_state=42)

# Xây dựng mô hình CNN
model = tf.keras.Sequential([
    tf.keras.layers.Conv2D(32, (3,3), activation='relu', input_shape=(IMG_SIZE, IMG_SIZE, 3)),
    tf.keras.layers.MaxPooling2D(2,2),
    
    tf.keras.layers.Conv2D(64, (3,3), activation='relu'),
    tf.keras.layers.MaxPooling2D(2,2),
    
    tf.keras.layers.Conv2D(128, (3,3), activation='relu'),
    tf.keras.layers.MaxPooling2D(2,2),
    
    tf.keras.layers.Flatten(),
    tf.keras.layers.Dense(256, activation='relu'),
    tf.keras.layers.Dropout(0.5),
    tf.keras.layers.Dense(len(np.unique(y_encoded)), activation='softmax')
])

model.compile(optimizer='adam', loss='sparse_categorical_crossentropy', metrics=['accuracy'])
model.summary()

# Huấn luyện mô hình
model.fit(X_train, y_train, epochs=20, validation_data=(X_test, y_test), batch_size=16)

# Lưu mô hình sau khi huấn luyện
model.save("face_recognition_model.h5")