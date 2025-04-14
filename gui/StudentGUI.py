import tkinter as tk
from tkinter import Image, ttk, messagebox
from PIL import Image, ImageTk
import sys
import os
import cv2,os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from dao import ClassDAO, DepartmentDAO, StudentDAO
from gui.UI import AddStudentGUI
from dao.TestDAO import TestDAO
from models.Students import Student
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
        self.tree = ttk.Treeview(frame_table, columns=columns, show="headings")

        for col in columns:
            self.tree.heading(col, text=col, command=lambda _col=col: self.treeview_sort_column(_col, False))
            self.tree.column(col, anchor="center")

        self.tree.column("STT", width=30)
        self.tree.column("ID", width=80)
        self.tree.column("Họ tên", width=200)
        self.tree.column("Ngày sinh", width=120)
        self.tree.column("Giới tính", width=80)
        self.tree.column("Trạng thái", width=120)

        # Gán tree vào thuộc tính của class để có thể sử dụng ở các phương thức khác

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

        btn_add = tk.Button(frame_btns, text="Thêm", width=20, command= self.add_student)
        btn_add.pack(fill= tk.X, padx=10, pady=10)

        btn_edit = tk.Button(frame_btns, text="Sửa", command=lambda: self.show_details_student(edit_mode=True))
        btn_edit.pack(fill=tk.X, padx=10, pady=10)
        
        btn_delete = tk.Button(frame_btns, text="Xóa", command=self.delete_student)
        btn_delete.pack(fill=tk.X, padx=10, pady=10)

        btn_show_detail= tk.Button(frame_btns, text="Chi tiết", command=self.show_details_student)
        btn_show_detail.pack(fill=tk.X, padx=10, pady=10)
        self.tree.bind("<Double-1>", self.show_details_student)

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
    
    def add_student(self):
        add_window = AddStudentGUI(self)  # Mở cửa sổ thêm sinh viên
    
        def on_close():
            self.refresh_student_list()  # Cập nhật danh sách sinh viên
            add_window.destroy()  # Đóng cửa sổ
    
        add_window.protocol("WM_DELETE_WINDOW", on_close)  # Gán sự kiện đóng cửa sổ
        add_window.grab_set()
        self.wait_window(add_window)
        # Cập nhật danh sách sinh viên sau khi thêm

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

    def show_details_student(self, event=None, edit_mode=False):
        selected_item = self.tree.selection()
        if not selected_item:
            return

        student_id = self.tree.item(selected_item[0])["values"][1]
        student_details = StudentDAO.get_by_id(student_id)

        detail_window = tk.Toplevel(self)
        detail_window.title(f"Thông Tin Chi Tiết - {student_details.fullname}")
        detail_window.geometry("500x400")

        detail_window.columnconfigure(0, weight=1)
        detail_window.columnconfigure(1, weight=1)

        department_of_student = DepartmentDAO.get_by_id(student_details.departmentId)
        department_name = getattr(department_of_student, "name", "Không có dữ liệu")

        class_of_student = ClassDAO.get_by_id(student_details.class_id)
        class_name = getattr(class_of_student, "name", "Không có dữ liệu")

        labels = [
            ("Mã SV:", student_details.id),
            ("Họ và tên:", student_details.fullname),
            ("Ngày sinh:", student_details.dateOfBirth),
            ("Giới tính:", student_details.gender),
            ("Lớp:", class_name),
            ("Khoa:", department_name),
            ("Địa chỉ:", student_details.address),
            ("Dân tộc:", student_details.ethnicity),
            ("Tôn giáo:", student_details.religion),
            ("Quốc tịch:", student_details.nationality),
            ("Niên khóa:", student_details.academicYear),
            ("Trạng thái:", student_details.status)
        ]

        # Danh sách các nhãn và giá trị hiển thị
        self.value_labels = []
        for i, (label, value) in enumerate(labels):
            tk.Label(detail_window, text=label, font=("Arial", 10, "bold")).grid(row=i, column=0, sticky="w", padx=10, pady=2)
            label_value = tk.Label(detail_window, text=value, font=("Arial", 10))
            label_value.grid(row=i, column=1, sticky="w", padx=10, pady=2)
            self.value_labels.append(label_value)

        self.original_data = {
            "id": student_details.id,
            "fullname": student_details.fullname,
            "dateOfBirth": student_details.dateOfBirth,
            "gender": student_details.gender,
            "class_id": student_details.class_id,
            "departmentId": student_details.departmentId,
            "address": student_details.address,
            "ethnicity": student_details.ethnicity,
            "religion": student_details.religion,
            "nationality": student_details.nationality,
            "academicYear": student_details.academicYear,
            "status": student_details.status
        }

         #HÌnh ảnh
        img_path = "D:\\University\\Pyhon-T2\\python-t2\\dataset\\image_student\\Test_img.jpg"

        if os.path.exists(img_path):
            img = Image.open(img_path)
            img = img.resize((100, 130), Image.LANCZOS)
            img = ImageTk.PhotoImage(img)

            label_img = tk.Label(detail_window, image=img)
            label_img.image = img  
            label_img.grid(row=0, column=2, rowspan=6, padx=20, pady=10)
        else:
            tk.Label(detail_window, text="Không có ảnh", bg="lightgray", font=("Arial", 10), width=12, height=8).grid(row=0, column=2, rowspan=6, padx=20, pady=10)

        # Frame chứa các nút
        frame_buttons = tk.Frame(detail_window)
        frame_buttons.grid(row=13, column=0, columnspan=3, pady=10)

        btn_width = 12  # Kích thước nút

        btnDong = tk.Button(frame_buttons, text="Đóng", width=btn_width, command=detail_window.destroy)
        btnDong.pack(side=tk.LEFT, padx=20)

        btnSua = tk.Button(frame_buttons, text="Sửa", width=btn_width, bg="#1C86EE", fg="white")
        btnSua.pack(side=tk.LEFT, padx=20)

        # Hàm đổi trạng thái nút
        def switch_to_edit_mode():
            if btnSua.cget("text") == "Sửa":
                btnSua.config(text="Lưu", command=save_changes, bg="#4CAF50")  # Đổi thành nút "Lưu"
                btnDong.config(text="Hủy", command=cancel_edit, bg="#f44336")  # Đổi thành nút "Hủy"

                status_options = ["Đang học", "Bảo lưu", "Đình chỉ", "Tốt nghiệp", "Khác"]

                # Chuyển label thành Entry để chỉnh sửa
                for i, (label, value) in enumerate(labels):
                    if label == "Trạng thái:":
                        combobox = ttk.Combobox(detail_window, values=status_options, state="readonly", font=("Arial", 10))
                        combobox.set(self.value_labels[i].cget("text"))  # Đặt giá trị ban đầu
                        combobox.grid(row=i, column=1, sticky="w", padx=8, pady=2)
                        self.value_labels[i].destroy()  # Xóa label cũ
                        self.value_labels[i] = combobox  # Thay thế bằng combobox
                    elif label != "Mã SV:" and label != "Lớp:" and label != "Khoa:":  # Các trường khác dùng Entry
                        entry = tk.Entry(detail_window, font=("Arial", 10))
                        entry.insert(0, self.value_labels[i].cget("text"))
                        entry.grid(row=i, column=1, sticky="w", padx=8, pady=2)
                        self.value_labels[i].destroy()
                        self.value_labels[i] = entry

            elif btnSua.cget("text") == "Lưu" and btnDong.cget("text") == "Hủy":
                # Kiểm tra dữ liệu đã nhập vào Entry
                btnDong.config(text="Đóng", width=btn_width, command=detail_window.destroy,  bg="SystemButtonFace")
                btnSua.config(text="Sửa", width=btn_width, command=switch_to_edit_mode, bg="#1C86EE", fg="white")
                
                # if not all(value.get() if isinstance(value, tk.Entry) else value.cget("text") for value in self.value_labels[1:]):
                #     messagebox.showerror("Lỗi", "Vui lòng nhập đầy đủ thông tin!")
                #     return
        # Hàm hủy chỉnh sửa
        def cancel_edit():
            for i, (label, value) in enumerate(labels):
                if isinstance(self.value_labels[i], (tk.Entry, ttk.Combobox)):  
                    original_value = self.original_data.get(
                        list(self.original_data.keys())[i],  # Lấy key tương ứng trong original_data
                        ""
                    )
                    new_label = tk.Label(detail_window, text=original_value, font=("Arial", 10))
                    new_label.grid(row=i, column=1, sticky="w", padx=10, pady=2)
                    self.value_labels[i].destroy()  
                    self.value_labels[i] = new_label  

            switch_to_edit_mode()
        
        # Hàm lưu thay đổi
        def save_changes():
            try:
                # Lấy giá trị mới từ Entry
                new_values = [
                    value.get() if isinstance(value, (tk.Entry, ttk.Combobox)) else value.cget("text")
                    for value in self.value_labels
                ]

                # Cập nhật dữ liệu vào đối tượng student_details
                student_details.fullname = new_values[1]
                student_details.dateOfBirth = new_values[2]
                student_details.gender = new_values[3]
                student_details.address = new_values[6]
                student_details.ethnicity = new_values[7]
                student_details.religion = new_values[8]
                student_details.nationality = new_values[9]
                student_details.academicYear = new_values[10]
                student_details.status = new_values[11]

                # Kiểm tra giá trị trước khi cập nhật
                if not all(new_values[1:]):  # Bỏ qua ID
                    messagebox.showerror("Lỗi", "Vui lòng nhập đầy đủ thông tin!")
                    return  # Ngừng hàm nếu dữ liệu không hợp lệ

                # Cập nhật dữ liệu vào CSDL
                StudentDAO.update(student_details)

                # Chuyển đổi Entry thành Label sau khi lưu
                for i, (label, value) in enumerate(labels):
                    if isinstance(self.value_labels[i], (tk.Entry, ttk.Combobox)):  # Kiểm tra nếu là Entry hoặc Combobox
                        new_label = tk.Label(detail_window, text=self.value_labels[i].get(), font=("Arial", 10))
                        new_label.grid(row=i, column=1, sticky="w", padx=10, pady=2)
                        self.value_labels[i].destroy()  # Xóa Entry/Combobox
                        self.value_labels[i] = new_label  # Cập nhật danh sách

                # Cập nhật trạng thái nút
                btnDong.config(text="Đóng", command=detail_window.destroy, bg="SystemButtonFace")
                btnSua.config(text="Sửa", command=switch_to_edit_mode, bg="#1C86EE", fg="white")

                messagebox.showinfo("Thông báo", "Cập nhật thông tin thành công!")

                # Đưa cửa sổ chi tiết lên trên sau khi đóng messagebox
                detail_window.lift()
                detail_window.focus_force() 

                self.refresh_student_list()
            
            except Exception as e:
                messagebox.showerror("Lỗi", f"Có lỗi xảy ra: {e}")


        # Nếu mở từ nút "Sửa" ở cửa sổ chính, vào ngay chế độ chỉnh sửa
        if edit_mode:
            detail_window.after(100, switch_to_edit_mode)
        # Gán sự kiện cho nút "Sửa"
        btnSua.config(command=switch_to_edit_mode)

    def find_student(self):
        #Lấy giá trị từ Entry
        id_student = self.entry_search_ID.get().strip()  # Xóa khoảng trắng
        name_student = self.entry_search_Name.get().strip().lower()  # Chuyển thành chữ thường

        if id_student or name_student:
            #Lấy danh sách sinh viên từ CSDL
            list_student = StudentDAO.get_all()

            #Tạo danh sách chứa kết quả tìm kiếm
            filtered_students = []

            for student in list_student:
                student_id = str(student.id)  # Đảm bảo ID là chuỗi để so sánh
                student_name = student.fullname.lower()  # Chuyển thành chữ thường

                #Kiểm tra điều kiện tìm kiếm
                if id_student and id_student in student_id:  # Nếu tìm theo ID
                    filtered_students.append(student)
                elif name_student and name_student in student_name:  # Nếu tìm theo tên
                    filtered_students.append(student)

            #Xóa dữ liệu cũ trong TreeView
            for item in self.tree.get_children():
                self.tree.delete(item)

            #Hiển thị kết quả tìm kiếm
            for i, stu in enumerate(filtered_students, start=1):
                self.tree.insert("", "end", values=(i, stu.id, stu.fullname, stu.dateOfBirth, stu.gender,stu.status,))

            self.clear_filed()

            print(f"🔎 Tìm thấy {len(filtered_students)} kết quả.")
        else:
            self.refresh_student_list()

    def treeview_sort_column(self, col, reverse):
        l = []
        for k in self.tree.get_children(''):
            try:
                val = float(self.tree.set(k, col))  # Thử chuyển đổi thành số thực
            except ValueError:
                val = self.tree.set(k, col)  # Nếu không phải số, giữ nguyên chuỗi
            l.append((val, k))

        l.sort(reverse=reverse)

        for index, (val, k) in enumerate(l):
            self.tree.move(k, '', index)

        self.tree.heading(col, command=lambda: self.treeview_sort_column(col, not reverse))
    
    
    def clear_filed(self):
        self.entry_search_ID.delete(0, tk.END)
        self.entry_search_Name.delete(0, tk.END)
    def TakeImages(self):        
       
            cam = cv2.VideoCapture(0)
            harcascadePath = "gui/haarcascade_frontalface_default.xml" # model phát hiện khuôn mặt haarcascade
            detector=cv2.CascadeClassifier(harcascadePath)
            sampleNum=0
            while(True):
                ret, img = cam.read()
                gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
                faces = detector.detectMultiScale(gray, 1.3, 5)
                for (x,y,w,h) in faces:
                    cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)        

                    sampleNum=sampleNum+1

                    cv2.imwrite("gui\TrainingImage\ "+"hhh" +"."+"787887"+'.'+ str(sampleNum) + ".jpg", gray[y:y+h,x:x+w]) #luu anh train vao folder

                    cv2.imshow('frame',img)

                if cv2.waitKey(1) & 0xFF == ord('q'):
                    break
                elif sampleNum>100: #luu anh cho den khi dc 100 anh
                    break
            cam.release()
            cv2.destroyAllWindows() 
           
           
            print("1")
            
            student=Student(id=2322332,fullname="hihi")
            StudentDAO.save(student)
        
       
        

if __name__ == '__main__':
    app = Student_List()
    app.mainloop()