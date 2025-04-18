import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from PIL import Image, ImageTk
import os

class StudentView:
    def __init__(self, root):
        self.root = root
        self.root.title("Sinh Viên")
        
        # Get screen dimensions
        screen_width = self.root.winfo_screenwidth()
        screen_height = self.root.winfo_screenheight()
        self.root.geometry(f"{screen_width}x{screen_height}")
        
        # Create main container with white background
        self.main_container = tk.Frame(self.root, bg="white")
        self.main_container.place(x=0, y=0, width=screen_width, height=screen_height)
        
        # Create left menu frame with light gray background
        self.menu_frame = tk.Frame(self.main_container, width=250, bg="#f0f0f0")
        self.menu_frame.place(x=0, y=0, height=screen_height)
        self.menu_frame.pack_propagate(False)  # Prevent frame from shrinking
        
        # Create content frame
        self.content_frame = tk.Frame(self.main_container, bg="white")
        self.content_frame.place(x=250, y=0, width=screen_width-250, height=screen_height)
        
        # Add header
        self.create_header()
        
        # Create menu buttons
        self.create_menu_buttons()
        
        # Initialize content frames
        self.create_content_frames()
        
        # Show default frame
        self.show_frame("personal_info")
    
    def create_header(self):
        # Header frame
        header_frame = tk.Frame(self.menu_frame, bg="#f0f0f0")
        header_frame.pack(fill=tk.X, pady=20)
        
        # School name
        tk.Label(header_frame, text="Trường Đại học Sài Gòn", 
                font=("Times New Roman", 13), fg="black", bg="#f0f0f0").pack()
        
        # Student portal title
        tk.Label(header_frame, text="Cổng thông tin sinh viên", 
                font=("Times New Roman", 16, "bold"), fg="red", bg="#f0f0f0").pack(pady=10)
    
    def create_menu_buttons(self):
        # Menu buttons frame
        buttons_frame = tk.Frame(self.menu_frame, bg="#f0f0f0")
        buttons_frame.pack(fill=tk.X, pady=20)
        
        # Menu buttons with consistent styling
        button_style = {
            "font": ("Times New Roman", 12),
            "width": 25,
            "bd": 0,
            "bg": "red",
            "fg": "white",
            "pady": 10
        }
        
        tk.Button(buttons_frame, text="Thông tin cá nhân", 
                 command=lambda: self.show_frame("personal_info"), **button_style).pack(pady=5)
        tk.Button(buttons_frame, text="Xem lịch học", 
                 command=lambda: self.show_frame("schedule"), **button_style).pack(pady=5)
        tk.Button(buttons_frame, text="Xem lịch điểm danh", 
                 command=lambda: self.show_frame("attendance"), **button_style).pack(pady=5)
        
        # Logout button at bottom with different style
        logout_style = button_style.copy()
        logout_style["bg"] = "#f44336"  # Red color for logout
        
        # Create a frame for the logout button at the bottom
        logout_frame = tk.Frame(self.menu_frame, bg="#f0f0f0")
        logout_frame.pack(side=tk.BOTTOM, fill=tk.X, pady=20)
        
        tk.Button(logout_frame, text="Đăng xuất", 
                 command=self.logout, **logout_style).pack(pady=5)
    
    def create_content_frames(self):
        # Create frames for each section
        self.personal_info_frame = self.create_personal_info_frame()
        self.schedule_frame = self.create_schedule_frame()
        self.attendance_frame = self.create_attendance_frame()
    
    def create_personal_info_frame(self):
        # Create personal info frame
        frame = tk.Frame(self.content_frame, bg="white")
        
        # Title
        title_frame = tk.Frame(frame, bg="white")
        title_frame.pack(fill=tk.X, pady=20)
        
        tk.Label(title_frame, text="Thông tin cá nhân", 
                font=("Times New Roman", 20, "bold"), fg="red", bg="white").pack(side=tk.LEFT, padx=30)

        # Sample student data
        self.student_data = {
            "id": "SV001",
            "fullname": "Nguyễn Văn A",
            "dateOfBirth": "01/01/2000",
            "gender": "Nam",
            "class_name": "CNTT1",
            "department_name": "Công nghệ thông tin",
            "address": "123 Đường ABC, Quận 1, TP.HCM",
            "ethnicity": "Kinh",
            "religion": "Không",
            "nationality": "Việt Nam",
            "academicYear": "2023-2024",
            "status": "Đang học"
        }

        # Labels list with display names
        self.labels = [
            ("Mã SV:", self.student_data["id"]),
            ("Họ và tên:", self.student_data["fullname"]),
            ("Ngày sinh:", self.student_data["dateOfBirth"]),
            ("Giới tính:", self.student_data["gender"]),
            ("Lớp:", self.student_data["class_name"]),
            ("Khoa:", self.student_data["department_name"]),
            ("Địa chỉ:", self.student_data["address"]),
            ("Dân tộc:", self.student_data["ethnicity"]),
            ("Tôn giáo:", self.student_data["religion"]),
            ("Quốc tịch:", self.student_data["nationality"]),
            ("Niên khóa:", self.student_data["academicYear"]),
            ("Trạng thái:", self.student_data["status"])
        ]

        # Create main container
        self.main_container = tk.Frame(frame, bg="white")
        self.main_container.pack(fill=tk.BOTH, expand=True, padx=30, pady=10)

        # Store value labels for later access
        self.value_labels = []

        # Create labels and values
        for i, (label, value) in enumerate(self.labels):
            tk.Label(self.main_container, text=label, font=("Times New Roman", 12, "bold"), 
                    bg="white").grid(row=i, column=0, sticky="w", padx=10, pady=5)
            label_value = tk.Label(self.main_container, text=value, font=("Times New Roman", 12), 
                    bg="white")
            label_value.grid(row=i, column=1, sticky="w", padx=10, pady=5)
            self.value_labels.append(label_value)

        # Image section
        img_path = r"D:\University\Exercise\PYTHON\python-T2\dataset\image_student\image.png"
        
        if os.path.exists(img_path):
            try:
                img = Image.open(img_path)
                img = img.resize((150, 200), Image.LANCZOS)  # Increased size for better visibility
                photo = ImageTk.PhotoImage(img)
                
                img_label = tk.Label(self.main_container, image=photo, bg="white")
                img_label.image = photo  # Keep a reference
                img_label.grid(row=0, column=2, rowspan=8, padx=(50, 20), pady=10)
                
                # Add a border around the image
                border_frame = tk.Frame(self.main_container, bg="#dddddd", bd=1, relief="solid")
                border_frame.grid(row=0, column=2, rowspan=8, padx=(50, 20), pady=10)
                border_frame.grid_propagate(False)
                border_frame.configure(width=170, height=220)  # Slightly larger than the image
                border_frame.lower()  # Place behind the image
                
            except Exception as e:
                tk.Label(self.main_container, text="Không thể tải ảnh", 
                        font=("Times New Roman", 12), bg="white", fg="red").grid(
                            row=0, column=2, rowspan=8, padx=(50, 20), pady=10)
        else:
            tk.Label(self.main_container, text="Ảnh sinh viên\nKhông tìm thấy ảnh", 
                    font=("Times New Roman", 12), bg="white", fg="#666666").grid(
                        row=0, column=2, rowspan=8, padx=(50, 20), pady=10)

        # Add buttons frame at the bottom
        # button_frame = tk.Frame(self.main_container, bg="white")
        # button_frame.grid(row=0, column=2, rowspan=8, padx=(50, 20), pady=100)

        # Create buttons
        self.edit_button = tk.Button(self.main_container, text="Sửa", 
                                   font=("Times New Roman", 12),
                                   width=15, bg="#1C86EE", fg="white",
                                   command=self.switch_to_edit_mode)
        self.edit_button.grid(row=7, column=2, rowspan=8, padx=(50, 20), pady=10)

        return frame
    
    def create_schedule_frame(self):
        # Create schedule frame
        frame = tk.Frame(self.content_frame, bg="white")
        
        # Title
        tk.Label(frame, text="Xem lịch học", 
                font=("Times New Roman", 20, "bold"), fg="red", bg="white").pack(pady=20)
        
        # Content container
        content_container = tk.Frame(frame, bg="white")
        content_container.pack(fill=tk.BOTH, expand=True, padx=30, pady=10)
        
        # Add placeholder content
        tk.Label(content_container, text="Lịch học sẽ hiển thị ở đây", 
                font=("Times New Roman", 14), bg="white").pack(pady=50)
        
        return frame
    
    def create_attendance_frame(self):
        # Create attendance frame
        frame = tk.Frame(self.content_frame, bg="white")
        
        # Title
        title_frame = tk.Frame(frame, bg="white")
        title_frame.pack(fill=tk.X, pady=20)
        
        tk.Label(title_frame, text="Xem lịch điểm danh", 
                font=("Times New Roman", 20, "bold"), fg="red", bg="white").pack(side=tk.LEFT, padx=30)

        # Class name section
        class_frame = tk.Frame(frame, bg="white")
        class_frame.pack(fill=tk.X, padx=30, pady=10)
        
        tk.Label(class_frame, text="Lớp: CNTT1", 
                font=("Times New Roman", 14, "bold"), bg="white").pack(anchor="w")

        # Create table frame
        table_frame = tk.Frame(frame, bg="white")
        table_frame.pack(fill=tk.BOTH, expand=True, padx=30, pady=10)

        # Create Treeview
        columns = ("id", "status", "checkin_time")
        self.attendance_tree = ttk.Treeview(table_frame, columns=columns, show="headings", height=20)

        # Define column headings
        self.attendance_tree.heading("id", text="Mã điểm danh")
        self.attendance_tree.heading("status", text="Trạng thái")
        self.attendance_tree.heading("checkin_time", text="Thời gian điểm danh")

        # Define column widths
        self.attendance_tree.column("id", width=150, anchor="center")
        self.attendance_tree.column("status", width=150, anchor="center")
        self.attendance_tree.column("checkin_time", width=200, anchor="center")

        # Add scrollbar
        scrollbar = ttk.Scrollbar(table_frame, orient="vertical", command=self.attendance_tree.yview)
        self.attendance_tree.configure(yscrollcommand=scrollbar.set)

        # Pack the Treeview and scrollbar
        self.attendance_tree.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

        # Style the Treeview
        style = ttk.Style()
        style.configure("Treeview.Heading", font=("Times New Roman", 12, "bold"))
        style.configure("Treeview", font=("Times New Roman", 11), rowheight=25)

        # Sample data (you can replace this with actual data later)
        sample_data = [
            ("ATT001", "Có mặt", "2024-01-15 08:00:00"),
            ("ATT002", "Có mặt", "2024-01-16 08:00:00"),
            ("ATT003", "Vắng", "2024-01-17 08:00:00"),
            ("ATT004", "Có mặt", "2024-01-18 08:00:00"),
            ("ATT005", "Có mặt", "2024-01-19 08:00:00"),
        ]

        # Insert sample data
        for item in sample_data:
            self.attendance_tree.insert("", tk.END, values=item)

        # Add alternating row colors
        self.attendance_tree.tag_configure("oddrow", background="#f0f0f0")
        self.attendance_tree.tag_configure("evenrow", background="white")
        
        for i, item in enumerate(self.attendance_tree.get_children()):
            if i % 2 == 0:
                self.attendance_tree.item(item, tags=("evenrow",))
            else:
                self.attendance_tree.item(item, tags=("oddrow",))

        return frame
    
    def show_frame(self, frame_name):
        # Hide all frames
        self.personal_info_frame.place_forget()
        self.schedule_frame.place_forget()
        self.attendance_frame.place_forget()
        
        # Show selected frame
        if frame_name == "personal_info":
            self.personal_info_frame.place(x=0, y=0, width=self.content_frame.winfo_width(), 
                                         height=self.content_frame.winfo_height())
        elif frame_name == "schedule":
            self.schedule_frame.place(x=0, y=0, width=self.content_frame.winfo_width(), 
                                    height=self.content_frame.winfo_height())
        elif frame_name == "attendance":
            self.attendance_frame.place(x=0, y=0, width=self.content_frame.winfo_width(), 
                                      height=self.content_frame.winfo_height())
    
    def logout(self):
        if messagebox.askyesno("Đăng xuất", "Bạn có chắc chắn muốn đăng xuất?"):
            self.root.destroy()

    def switch_to_edit_mode(self):
        if self.edit_button.cget("text") == "Sửa":
            # Change to edit mode
            self.edit_button.config(text="Lưu", bg="#4CAF50", command=self.save_changes)
            
            # Convert labels to entries for editable fields
            editable_fields = ["Địa chỉ:", "Dân tộc:", "Tôn giáo:"]
            for i, (label, _) in enumerate(self.labels):
                if label in editable_fields:
                    current_value = self.value_labels[i].cget("text")
                    self.value_labels[i].destroy()
                    entry = tk.Entry(self.main_container, font=("Times New Roman", 12))
                    entry.insert(0, current_value)
                    entry.grid(row=i, column=1, sticky="w", padx=10, pady=5)
                    self.value_labels[i] = entry

        else:
            # Already in edit mode, save changes handled by save_changes method
            pass

    def save_changes(self):
        try:
            # Get values from entries
            updated_values = {}
            editable_fields = ["Địa chỉ:", "Dân tộc:", "Tôn giáo:"]
            
            for i, (label, _) in enumerate(self.labels):
                if label in editable_fields:
                    if isinstance(self.value_labels[i], tk.Entry):
                        updated_values[label] = self.value_labels[i].get()

            # Validate input
            if not all(updated_values.values()):
                messagebox.showerror("Lỗi", "Vui lòng điền đầy đủ thông tin!")
                return

            # Update student_data
            for label, value in updated_values.items():
                if label == "Địa chỉ:":
                    self.student_data["address"] = value
                elif label == "Dân tộc:":
                    self.student_data["ethnicity"] = value
                elif label == "Tôn giáo:":
                    self.student_data["religion"] = value

            # Convert entries back to labels
            for i, (label, _) in enumerate(self.labels):
                if label in editable_fields:
                    if isinstance(self.value_labels[i], tk.Entry):
                        current_value = self.value_labels[i].get()
                        self.value_labels[i].destroy()
                        new_label = tk.Label(self.main_container, text=current_value,
                                          font=("Times New Roman", 12), bg="white")
                        new_label.grid(row=i, column=1, sticky="w", padx=10, pady=5)
                        self.value_labels[i] = new_label

            # Reset button
            self.edit_button.config(text="Sửa", bg="#1C86EE", command=self.switch_to_edit_mode)
            
            messagebox.showinfo("Thành công", "Cập nhật thông tin thành công!")

        except Exception as e:
            messagebox.showerror("Lỗi", f"Có lỗi xảy ra: {str(e)}")
            # Reset to edit mode if error occurs
            self.edit_button.config(text="Sửa", bg="#1C86EE", command=self.switch_to_edit_mode)

# Example usage
if __name__ == "__main__":
    root = tk.Tk()
    app = StudentView(root)
    root.mainloop() 