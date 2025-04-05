import cv2
import numpy as np
import os
import pickle
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report

# ===== THU THẬP DỮ LIỆU =====
def collect_face_data(student_id, student_name, num_samples=100):
    """Thu thập ảnh khuôn mặt từ camera"""
    dataset_dir = "face_dataset"
    if not os.path.exists(dataset_dir):
        os.makedirs(dataset_dir)
    
    student_dir = os.path.join(dataset_dir, str(student_id))
    if not os.path.exists(student_dir):
        os.makedirs(student_dir)
    
    cap = cv2.VideoCapture(0)
    face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
    
    count = 0
    print(f"Thu thập dữ liệu cho sinh viên {student_id}_{student_name}")
    
    while count < num_samples:
        ret, frame = cap.read()
        if not ret:
            break
            
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        
        faces = face_cascade.detectMultiScale(gray, 1.3, 5)
        
        for (x, y, w, h) in faces:
            cv2.rectangle(frame, (x, y), (x+w, y+h), (255, 0, 0), 2)
            
            face_roi = gray[y:y+h, x:x+w]
            face_roi = cv2.resize(face_roi, (64, 64))  
            
            img_path = os.path.join(student_dir, f"{count}.jpg")
            cv2.imwrite(img_path, face_roi)
            
            count += 1
            cv2.putText(frame, f"Count: {count}/{num_samples}", (x, y-10), 
                       cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 255, 0), 2)
        
        cv2.imshow('Face Collection', frame)
        
        # Nhấn 'q' để thoát
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
            
        if count >= num_samples:
            break
    
    cap.release()
    cv2.destroyAllWindows()
    print(f"Đã thu thập {count} mẫu cho sinh viên {student_id}_{student_name}")

# ===== TRÍCH XUẤT ĐẶC TRƯNG =====
def extract_features_manual(image):
    """Trích xuất đặc trưng LBP đơn giản từ ảnh"""
    # Histogram LBP (Local Binary Pattern) đơn giản - trích xuất đặc trưng thủ công
    patterns = np.zeros(256, dtype=np.int32)
    h, w = image.shape
    
    # Duyệt qua từng pixel (trừ viền)
    for i in range(1, h-1):
        for j in range(1, w-1):
            center = image[i, j]
            code = 0
            
            # Tính LBP code
            code |= (image[i-1, j-1] >= center) << 7
            code |= (image[i-1, j] >= center) << 6
            code |= (image[i-1, j+1] >= center) << 5
            code |= (image[i, j+1] >= center) << 4
            code |= (image[i+1, j+1] >= center) << 3
            code |= (image[i+1, j] >= center) << 2
            code |= (image[i+1, j-1] >= center) << 1
            code |= (image[i, j-1] >= center) << 0
            
            patterns[code] += 1
    
    # Chuẩn hóa histogram
    patterns = patterns / np.sum(patterns)
    
    # Kết hợp với HOG đặc trưng thô sơ
    gx = cv2.Sobel(image, cv2.CV_32F, 1, 0, ksize=3)
    gy = cv2.Sobel(image, cv2.CV_32F, 0, 1, ksize=3)
    
    mag, ang = cv2.cartToPolar(gx, gy)
    
    # Chia góc thành 9 bins (0-180 độ)
    nbins = 9
    hog_hist = np.zeros(nbins, dtype=np.float32)
    
    # Chuyển góc từ radian sang độ và chia bins
    ang_deg = ang * 180 / np.pi
    bin_size = 180 / nbins
    
    for i in range(ang_deg.shape[0]):
        for j in range(ang_deg.shape[1]):
            bin_idx = int(ang_deg[i, j] / bin_size) % nbins
            hog_hist[bin_idx] += mag[i, j]
    
    # Chuẩn hóa HOG histogram
    if np.sum(hog_hist) > 0:
        hog_hist = hog_hist / np.sum(hog_hist)
    
    # Kết hợp hai đặc trưng
    features = np.concatenate((patterns, hog_hist))
    
    # Thêm đặc trưng trung bình cường độ theo vùng
    regions = [(0, 0, 32, 32), (32, 0, 64, 32), (0, 32, 32, 64), (32, 32, 64, 64)]
    region_features = []
    
    for x1, y1, x2, y2 in regions:
        region = image[y1:y2, x1:x2]
        avg_intensity = np.mean(region)
        std_intensity = np.std(region)
        region_features.extend([avg_intensity, std_intensity])
    
    # Kết hợp tất cả đặc trưng
    features = np.concatenate((features, region_features))
    
    return features

# ===== HUẤN LUYỆN PHÂN LOẠI TỰ VIẾT =====
class SimpleClassifier:
    """Phân loại đơn giản sử dụng khoảng cách Euclidean"""
    def __init__(self):
        self.features = []
        self.labels = []
        self.label_mapping = {}
    
    def fit(self, X, y):
        self.features = X
        self.labels = y
        unique_labels = np.unique(y)
        for idx, label in enumerate(unique_labels):
            self.label_mapping[idx] = label
        print(f"Đã huấn luyện mô hình với {len(X)} mẫu và {len(unique_labels)} lớp")
    
    def predict(self, X):
        predictions = []
        for sample in X:
            distances = [np.linalg.norm(sample - feat) for feat in self.features]
            nearest_idx = np.argmin(distances)
            predictions.append(self.labels[nearest_idx])
        return np.array(predictions)
    
    def predict_proba(self, X):
        """Tính xác suất dựa trên khoảng cách nghịch đảo"""
        all_probs = []
        
        for sample in X:
            distances = np.array([np.linalg.norm(sample - feat) for feat in self.features])
            
            # Tránh chia cho 0
            distances = np.maximum(distances, 1e-10)
            
            # Chuyển khoảng cách thành điểm tin cậy (khoảng cách càng nhỏ càng tin cậy)
            confidence = 1.0 / distances
            
            # Chuẩn hóa để tổng bằng 1
            confidence = confidence / np.sum(confidence)
            
            unique_labels = np.unique(self.labels)
            probs = np.zeros(len(unique_labels))
            
            for i, label in enumerate(unique_labels):
                mask = (self.labels == label)
                if np.any(mask):
                    probs[i] = np.sum(confidence[mask])
            
            # Chuẩn hóa lại
            probs = probs / np.sum(probs)
            all_probs.append(probs)
            
        return np.array(all_probs)

# ===== TẢI DỮ LIỆU =====
def load_data(dataset_dir):
    """Tải dữ liệu từ thư mục dataset"""
    X = []
    y = []
    
    for student_id in os.listdir(dataset_dir):
        student_dir = os.path.join(dataset_dir, student_id)
        
        if os.path.isdir(student_dir):
            print(f"Đang xử lý dữ liệu của sinh viên {student_id}")
            
            for img_file in os.listdir(student_dir):
                if img_file.endswith('.jpg') or img_file.endswith('.png'):
                    img_path = os.path.join(student_dir, img_file)
                    
                    img = cv2.imread(img_path, cv2.IMREAD_GRAYSCALE)
                    
                    if img is not None:
                        features = extract_features_manual(img)
                        X.append(features)
                        y.append(int(student_id))
    
    return np.array(X), np.array(y)

# ===== HUẤN LUYỆN MÔ HÌNH =====
def train_model(X, y):
    """Huấn luyện mô hình phân loại"""
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    
    print("Bắt đầu huấn luyện mô hình...")
    model = SimpleClassifier()
    model.fit(X_train, y_train)
    
    y_pred = model.predict(X_test)
    accuracy = sum(y_pred == y_test) / len(y_test)
    print(f"Độ chính xác: {accuracy * 100:.2f}%")
    print(classification_report(y_test, y_pred))
    
    with open('face_recognition_model_manual.pkl', 'wb') as f:
        pickle.dump(model, f)
    
    return model

# ===== NHẬN DIỆN KHUÔN MẶT =====
def recognize_face_attendance():
    """Hệ thống điểm danh sử dụng nhận diện khuôn mặt"""
    try:
        with open('face_recognition_model_manual.pkl', 'rb') as f:
            model = pickle.load(f)
    except:
        print("Không tìm thấy mô hình. Vui lòng huấn luyện trước.")
        return
    
    cap = cv2.VideoCapture(0)
    face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
    
    attendance = set()
    
    while True:
        ret, frame = cap.read()
        if not ret:
            break
        
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        
        faces = face_cascade.detectMultiScale(gray, 1.3, 5)
        
        for (x, y, w, h) in faces:
            cv2.rectangle(frame, (x, y), (x+w, y+h), (255, 0, 0), 2)
            
            face_roi = gray[y:y+h, x:x+w]
            face_roi = cv2.resize(face_roi, (64, 64))
            
            features = extract_features_manual(face_roi)
            features = features.reshape(1, -1)
            
            try:
                probs = model.predict_proba(features)[0]
                student_id = model.predict(features)[0]
                max_prob = np.max(probs)
                
                if max_prob > 0.4: 
                    label = f"SV: {student_id}, {max_prob:.2f}"
                    cv2.putText(frame, label, (x, y-10), 
                               cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)
                    
                    attendance.add(student_id)
                else:
                    cv2.putText(frame, "Unknown", (x, y-10), 
                               cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 255), 2)
            except:
                cv2.putText(frame, "Error", (x, y-10), 
                           cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 255), 2)
        
        cv2.putText(frame, f"Diem danh: {len(attendance)} sinh vien", (10, 30),
                   cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 0, 255), 2)
        
        cv2.imshow('Face Recognition Attendance', frame)
        
        # Nhấn 'q' để thoát
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    
    cap.release()
    cv2.destroyAllWindows()
    
    # In danh sách điểm danh
    print("\nDanh sách sinh viên đã điểm danh:")
    for sid in attendance:
        print(f"- Sinh viên ID: {sid}")

# ===== CHƯƠNG TRÌNH CHÍNH =====
def main():
    while True:
        print("\n===== HỆ THỐNG ĐIỂM DANH BẰNG NHẬN DIỆN KHUÔN MẶT =====")
        print("1. Thu thập dữ liệu khuôn mặt")
        print("2. Huấn luyện mô hình")
        print("3. Bắt đầu điểm danh")
        print("0. Thoát")
        
        choice = input("Lựa chọn của bạn: ")
        
        if choice == '1':
            student_id = input("Nhập ID sinh viên: ")
            student_name = input("Nhập tên sinh viên: ")
            collect_face_data(student_id, student_name)
        
        elif choice == '2':
            dataset_dir = "face_dataset"
            if not os.path.exists(dataset_dir):
                print("Thư mục dataset không tồn tại!")
                continue
                
            X, y = load_data(dataset_dir)
            if len(X) == 0:
                print("Không có dữ liệu. Vui lòng thu thập dữ liệu trước!")
                continue
                
            train_model(X, y)
        
        elif choice == '3':
            recognize_face_attendance()
        
        elif choice == '0':
            print("Tạm biệt!")
            break
        
        else:
            print("Lựa chọn không hợp lệ. Vui lòng thử lại!")

if __name__ == "__main__":
    main()