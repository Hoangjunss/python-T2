import tkinter as tk
from tkinter import Image, ttk, messagebox
from PIL import Image, ImageTk
import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from dao import DepartmentDAO, StudentDAO
# from models.Students import Student


class Student_List(tk.Tk):
    def __init__(self):
        super().__init__()
        self.gui_DSSV()
        self.refresh_student_list() 
        self.mainloop()

    def gui_DSSV(self):
        self.title('Phần Mềm Điểm Danh Sinh Viên Bằng Nhận Diện Khuôn Mặt')
        self.geometry('850x650')

        # Phần trên (tiêu đề và tìm kiếm)
        frame_top = tk.Frame(self)
        frame_top.pack(fill=tk.X, padx=10, pady=10)

        label_title = tk.Label(frame_top, text="Quản Lý Sinh Viên", font=("Arial", 14, 'bold'))
        label_title.pack(anchor="w")

        frame_search = tk.Frame(frame_top)
        frame_search.pack(fill=tk.X, pady=5)

        label_search = tk.Label(frame_search, text="Thông tin tìm kiếm:", font=("Arial", 8, "bold"))
        label_search.pack(side= tk.LEFT)

        label_search_ID = tk.Label(frame_search, text="ID (MASV):", font=("Arial", 7))
        label_search_ID.pack(side= tk.LEFT, padx= 3)

        self.entry_search_ID = tk.Entry(frame_search, width=15)
        self.entry_search_ID.pack(side=tk.LEFT, padx= 3)

        label_search_Name = tk.Label(frame_search, text="Họ tên:", font=("Arial", 7))
        label_search_Name.pack(side= tk.LEFT, padx= 3)

        self.entry_search_Name = tk.Entry(frame_search, width=15)
        self.entry_search_Name.pack(side=tk.LEFT, padx= 3)
        
        btn_search = tk.Button(frame_search, text="Tìm Kiếm", width=15, command=self.find_student)
        btn_search.pack(side=tk.RIGHT, padx=5)

        #Phần dưới (bảng và các nút)
        frame_bottom = tk.Frame(self)
        frame_bottom.pack(fill=tk.BOTH, expand=True, padx=10, pady=5)

        # Table
        frame_table = tk.Frame(frame_bottom)
        frame_table.pack(side=tk.LEFT, expand="true", fill=tk.BOTH, padx=5)

        columns = ("STT", "ID", "Họ tên", "Ngày sinh", "Giới tính", "Trạng thái")
        tree = ttk.Treeview(frame_table, columns=columns, show="headings")

        tree.heading("STT", text="STT")
        tree.column("STT", width=30, anchor="center")
        tree.heading("ID", text="ID")
        tree.column("ID", width=80, anchor="center")
        tree.heading("Họ tên", text="Họ Tên")
        tree.column("Họ tên", width=200, anchor="center")
        tree.heading("Ngày sinh", text="Ngày sinh")
        tree.column("Ngày sinh", width=120, anchor="center")
        tree.heading("Giới tính", text="Giới tính")
        tree.column("Giới tính", width=80, anchor="center")
        tree.heading("Trạng thái", text="Trạng thái")
        tree.column("Trạng thái", width=120, anchor="center")

        # Gán tree vào thuộc tính của class để có thể sử dụng ở các phương thức khác
        self.tree = tree  

        # Tạo Scrollbar
        scrollbar = ttk.Scrollbar(frame_table, orient="vertical", command=self.tree.yview)
        self.tree.configure(yscrollcommand=scrollbar.set)

        # Đặt Treeview và Scrollbar vào Frame
        self.tree.pack(side=tk.LEFT, expand=True, fill=tk.BOTH)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

        # self.after(100, self.refresh_student_list)

        #Các nút chức năng

        frame_btns = tk.Frame(frame_bottom)
        frame_btns.pack(side=tk.RIGHT, fill=tk.Y, padx=10, expand=True)

        frame_btns.pack_propagate(False)
        frame_btns.config(width=200)

        tk.Label(frame_btns, text="Chức năng:", font=("Arial", 12)).pack(side=tk.TOP, pady=20)

        btn_add = tk.Button(frame_btns, text="Thêm", width=20)
        btn_add.pack(fill= tk.X, padx=10, pady=10)

        btn_edit = tk.Button(frame_btns, text="Sửa")
        btn_edit.pack(fill=tk.X, padx=10, pady=10)
        
        btn_delete = tk.Button(frame_btns, text="Xóa", command=self.delete_student)
        btn_delete.pack(fill=tk.X, padx=10, pady=10)

        btn_show_detail= tk.Button(frame_btns, text="Chi tiết", command=self.show_details_student)
        btn_show_detail.pack(fill=tk.X, padx=10, pady=10)

        #Footer
        frame_footer = tk.Frame(self)
        frame_footer.pack(fill=tk.X, padx=10, pady=10)
    
        btn_back = tk.Button(frame_footer, text="Trở về", width=15, command=self.destroy)# tạm thời khi nhấn sẽ tắt 
        btn_back.pack(side=tk.RIGHT, anchor="se", padx=10, pady=5)

    def refresh_student_list(self):
       # Xóa hết nội dung hiện tại
        for item in self.tree.get_children():
            self.tree.delete(item)
        i=1
        try:
            students = StudentDAO.get_all()
            for stu in students: 
                self.tree.insert("", "end", values=(
                    i,
                    stu.id,
                    stu.fullname,
                    stu.dateOfBirth,
                    stu.gender,
                    stu.status,  # Trạng thái sinh viên
                ))
                i+=1
        except Exception as e:
            print(f"Error: {e}")
            messagebox.showerror("Error", str(e))   
    
    def delete_student(self):
        selected_item = self.tree.selection()
        if selected_item:
            student_id = self.tree.item(selected_item[0])["values"][1]
            name_student = self.tree.item(selected_item[0])["values"][2]

            confirm = messagebox.askyesno("Xác nhận xóa", f"Bạn có chắc chắn muốn xóa sinh viên tên {name_student} không?")
            if confirm:
                try:
                    StudentDAO.delete(student_id)
                    self.refresh_student_list()
                    messagebox.showinfo("Thông báo", "Xóa thành công.")
                except Exception as e:
                    print(f"Error: {e}")
                    messagebox.showerror("Error", str(e))
        else:
            messagebox.showinfo("Thông báo", "Vui lòng chọn sinh viên để xóa.")

    def show_details_student(self):
        selected_item = self.tree.selection()
        if not selected_item:
            return
        
        student_id = self.tree.item(selected_item[0])["values"][1]
        student_details = StudentDAO.get_by_id(student_id)

        # Tạo cửa sổ con
        detail_window = tk.Toplevel(self)
        detail_window.title(f"Thông Tin Chi Tiết - {student_details.fullname}")
        detail_window.geometry("500x400")

        detail_window.columnconfigure(0, weight=1)
        detail_window.columnconfigure(1, weight=1)

        department_of_student = DepartmentDAO.get_by_id(student_details.departmentId)
        department_name = getattr(department_of_student, "name", "Không có dữ liệu")
        
        labels = [
            ("Mã SV:", student_details.id),
            ("Họ và tên:", student_details.fullname),
            ("Ngày sinh:", student_details.dateOfBirth),
            ("Giới tính:", student_details.gender),
            ("Khoa:", department_name),
            ("Địa chỉ:", student_details.address),
            ("Dân tộc:", student_details.ethnicity),
            ("Tôn giáo:", student_details.religion),
            ("Quốc tịch:", student_details.nationality),
            ("Niên khóa:", student_details.academicYear),
            ("Trạng thái:", student_details.status)
        ]

        for i, (label, value) in enumerate(labels):
            tk.Label(detail_window, text=label, font=("Arial", 10, "bold")).grid(row=i, column=0, sticky="w", padx=10, pady=2)
            tk.Label(detail_window, text=value, font=("Arial", 10)).grid(row=i, column=1, sticky="w", padx=10, pady=2)

        #HÌnh ảnh
        img_path = "D:\\University\\Pyhon-T2\\New_T2_Khoa\\dataset\\image_student\\Test_img.jpg"

        if os.path.exists(img_path):
            img = Image.open(img_path)
            img = img.resize((100, 130), Image.LANCZOS)
            img = ImageTk.PhotoImage(img)

            label_img = tk.Label(detail_window, image=img)
            label_img.image = img  
            label_img.grid(row=0, column=2, rowspan=6, padx=20, pady=10)
        else:
            tk.Label(detail_window, text="Không có ảnh", bg="lightgray", font=("Arial", 10), width=12, height=8).grid(row=0, column=2, rowspan=6, padx=20, pady=10)

        # Nút đóng cửa sổ
        tk.Button(detail_window, text="Đóng", command=detail_window.destroy).grid(row=14, column=1, pady=10)

    def find_student(self):
        # 1️⃣ Lấy giá trị từ Entry
        id_student = self.entry_search_ID.get().strip()  # Xóa khoảng trắng
        name_student = self.entry_search_Name.get().strip().lower()  # Chuyển thành chữ thường

        if id_student or name_student:
            # 2️⃣ Lấy danh sách sinh viên từ CSDL
            list_student = StudentDAO.get_all()

            # 3️⃣ Tạo danh sách chứa kết quả tìm kiếm
            filtered_students = []

            for student in list_student:
                student_id = str(student.id)  # Đảm bảo ID là chuỗi để so sánh
                student_name = student.fullname.lower()  # Chuyển thành chữ thường

                # 4️⃣ Kiểm tra điều kiện tìm kiếm
                if id_student and id_student in student_id:  # Nếu tìm theo ID
                    filtered_students.append(student)
                elif name_student and name_student in student_name:  # Nếu tìm theo tên
                    filtered_students.append(student)

            # 5️⃣ Xóa dữ liệu cũ trong TreeView
            for item in self.tree.get_children():
                self.tree.delete(item)

            # 6️⃣ Hiển thị kết quả tìm kiếm
            for i, stu in enumerate(filtered_students, start=1):
                self.tree.insert("", "end", values=(i, stu.id, stu.fullname, stu.dateOfBirth, stu.gender,stu.status,))

            self.clear_filed()

            print(f"🔎 Tìm thấy {len(filtered_students)} kết quả.")
        else:
            self.refresh_student_list()

    def clear_filed(self):
        self.entry_search_ID.delete(0, tk.END)
        self.entry_search_Name.delete(0, tk.END)

if __name__ == '__main__':
    app = Student_List()
    app.mainloop()