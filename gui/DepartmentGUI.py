import os
import sys
import tkinter as tk
from tkinter import ttk, messagebox
import uuid


sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from dao import DepartmentDAO
from models.Department import Department

class DepartmentGUI(tk.Frame):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.gui_Department()
        self.refresh_department_list()

    def gui_Department(self):
        # Phần trên (tiêu đề và tìm kiếm)
        frame_top = tk.Frame(self)
        frame_top.pack(fill=tk.X, padx=10, pady=10)

        label_title = tk.Label(frame_top, text="Quản Lý Khoa", font=("Arial", 14, 'bold'))
        label_title.pack(anchor="w")

        # Phần bảng và các chức năng
        frame_midle = tk.Frame(self)
        frame_midle.pack(fill=tk.BOTH, expand=True, padx=10, pady=5)

         # Table
        frame_table = tk.Frame(frame_midle)
        frame_table.pack(side=tk.LEFT, expand="true", fill=tk.BOTH, padx=5)

        columns = ("STT", "Mã Khoa", "Tên Khoa", "Số lượng sinh viên")
        tree = ttk.Treeview(frame_table, columns=columns, show="headings")

        tree.heading("STT", text="STT")
        tree.column("STT", width=30, anchor="center")
        tree.heading("Mã Khoa", text="ID")
        tree.column("Mã Khoa", width=80, anchor="center")
        tree.heading("Tên Khoa", text="Tên khoa")
        tree.column("Tên Khoa", width=200, anchor="center")
        tree.heading("Số lượng sinh viên", text="Số lượng sinh viên")
        tree.column("Số lượng sinh viên", width=120, anchor="center")


        self.tree = tree

        scrollbar = ttk.Scrollbar(frame_table, orient="vertical", command=self.tree.yview)
        self.tree.configure(yscrollcommand=scrollbar.set)

        # Đặt Treeview và Scrollbar vào Frame
        self.tree.pack(side=tk.LEFT, expand=True, fill=tk.BOTH)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

        #Các nút chức năng

        frame_btns = tk.Frame(frame_midle)
        frame_btns.pack(side=tk.RIGHT, fill=tk.Y, padx=10, expand=True)

        frame_btns.pack_propagate(False)
        frame_btns.config(width=200)

        tk.Label(frame_btns, text="Chức năng:", font=("Arial", 12)).pack(side=tk.TOP, pady=20)

        btn_add = tk.Button(frame_btns, text="Thêm", width=20, command=self.add_department)
        btn_add.pack(fill= tk.X, padx=10, pady=10)

        btn_edit = tk.Button(frame_btns, text="Sửa", command = self.update_department)
        btn_edit.pack(fill=tk.X, padx=10, pady=10)
        
        btn_delete = tk.Button(frame_btns, text="Xóa", command= self.delete_department)
        btn_delete.pack(fill=tk.X, padx=10, pady=10)

        btn_show_detail= tk.Button(frame_btns, text="Chi tiết", command=self.detail_department)
        btn_show_detail.pack(fill=tk.X, padx=10, pady=10)


    def refresh_department_list(self):
        # Xóa hết nội dung hiện tại
        for item in self.tree.get_children():
            self.tree.delete(item)
        i=1
        try:
            departments = DepartmentDAO.get_all()
            for dep in departments:
                # print(type(dep))
                quantity_students = DepartmentDAO.count_students_by_department(dep.id)
                self.tree.insert("", "end", values=(
                    i,
                    dep.id,
                    dep.name,
                    quantity_students,
                ))
                i += 1
        except Exception as e:
            print(f"Error: {e}")
            messagebox.showerror("Error", str(e))   

    def add_department(self):
        self.detail_window = tk.Toplevel(self)
        self.detail_window.title("Thêm khoa mới")
        self.detail_window.geometry("400x250")
        self.detail_window.configure(bg="white")
        self.detail_window.resizable(False, False)

        # Tiêu đề
        title_label = tk.Label(self.detail_window, text="Thêm khoa", font=("Arial", 12, "bold"), bg="white", fg="red")
        title_label.pack(pady=20)

        # Label + Entry: Tên khoa
        name_frame = tk.Frame(self.detail_window, bg="white")
        name_frame.pack(pady=10)

        name_label = tk.Label(name_frame, text="Tên khoa:", font=("Arial", 18), bg="white")
        name_label.pack(side="left", padx=10)

        self.department_name_entry = tk.Entry(name_frame, font=("Arial", 18), width=20)
        self.department_name_entry.pack(side="left")

        # Nút "Thêm"
        add_button = tk.Button(self.detail_window, text="Thêm khoa", font=("Arial", 16, "bold"),
                            bg="#4CAF50", fg="white", width=15, height=2, bd=0, command=self.save_department)
        add_button.pack(pady=20)

    def update_department(self):
        self.edit_window = tk.Toplevel(self)
        self.edit_window.title("Sửa thông tin khoa")
        self.edit_window.geometry("800x600")
        self.edit_window.configure(bg="white")
        self.edit_window.resizable(False, False)

        title_label = tk.Label(self.edit_window, font=("Arial", 25, "bold"),
                            text="Cập nhật mới thông tin khoa", bg="white", fg="red")
        title_label.place(x=200, y=30)

        locationX = 30
        locationEntry = 280
        locationY = 100
        backUpLocationY = 70

        stt_label = tk.Label(self.edit_window, font=("Arial", 17), text="STT:", bg="white", fg="black")
        stt_label.place(x=locationX, y=locationY)
        id_label = tk.Label(self.edit_window, font=("Arial", 17), text="MÃ KHOA:", bg="white", fg="black")
        id_label.place(x=locationX, y=locationY + backUpLocationY)
        name_label = tk.Label(self.edit_window, font=("Arial", 17), text="TÊN KHOA:", bg="white", fg="black")
        name_label.place(x=locationX, y=locationY + 2 * backUpLocationY)
        lead_label = tk.Label(self.edit_window, font=("Arial", 17), text="TRƯỞNG KHOA:", bg="white", fg="black")
        lead_label.place(x=locationX, y=locationY + 3 * backUpLocationY)
        student_label = tk.Label(self.edit_window, font=("Arial", 17), text="SỐ LƯỢNG SINH VIÊN:", bg="white", fg="black")
        student_label.place(x=locationX, y=locationY + 4 * backUpLocationY)

        self.textSTTDepartment = tk.Entry(self.edit_window, font=("Arial", 17), fg="black", width=30, borderwidth=1)
        self.textSTTDepartment.place(x=locationEntry, y=locationY)
        self.textIDDepartment = tk.Entry(self.edit_window, font=("Arial", 17), fg="black", width=30, borderwidth=1)
        self.textIDDepartment.place(x=locationEntry, y=locationY + backUpLocationY)
        self.textNameDepartment = tk.Entry(self.edit_window, font=("Arial", 17), fg="black", width=30, borderwidth=1)
        self.textNameDepartment.place(x=locationEntry, y=locationY + 2 * backUpLocationY)
        self.textLeadDepartment = tk.Entry(self.edit_window, font=("Arial", 17), fg="black", width=30, borderwidth=1)
        self.textLeadDepartment.place(x=locationEntry, y=locationY + 3 * backUpLocationY)
        self.textStudentDepartment = tk.Entry(self.edit_window, font=("Arial", 17), fg="black", width=30, borderwidth=1)
        self.textStudentDepartment.place(x=locationEntry, y=locationY + 4 * backUpLocationY)

        buttonUpdate = tk.Button(self.edit_window, text="Cập nhật", font=("Arial", 18, "bold"),
                                bg="black", fg="white", width=15, height=2, bd=0)
        buttonUpdate.place(x=300, y=locationY + 5 * backUpLocationY + 20)

            # Sự kiện hover vào button
        buttonUpdate.bind("<Enter>", lambda e:buttonUpdate.config(bg="red", fg="white"))

            # Sự kiện rời khỏi button
        buttonUpdate.bind("<Leave>", lambda e:buttonUpdate.config(bg="black", fg="white"))

    def detail_department(self):
        self.edit_window = tk.Toplevel(self)
        self.edit_window.title("Sửa thông tin khoa")
        self.edit_window.geometry("800x600")
        self.edit_window.configure(bg="white")
        self.edit_window.resizable(False, False)

        title_label = tk.Label(self.edit_window, font=("Arial", 25, "bold"),
                            text="Chi tiết thông tin khoa", bg="white", fg="red")
        title_label.place(x=200, y=30)

        locationX = 30
        locationEntry = 280
        locationY = 100
        backUpLocationY = 70

        stt_label = tk.Label(self.edit_window, font=("Arial", 17), text="STT:", bg="white", fg="black")
        stt_label.place(x=locationX, y=locationY)
        id_label = tk.Label(self.edit_window, font=("Arial", 17), text="MÃ KHOA:", bg="white", fg="black")
        id_label.place(x=locationX, y=locationY + backUpLocationY)
        name_label = tk.Label(self.edit_window, font=("Arial", 17), text="TÊN KHOA:", bg="white", fg="black")
        name_label.place(x=locationX, y=locationY + 2 * backUpLocationY)
        lead_label = tk.Label(self.edit_window, font=("Arial", 17), text="TRƯỞNG KHOA:", bg="white", fg="black")
        lead_label.place(x=locationX, y=locationY + 3 * backUpLocationY)
        student_label = tk.Label(self.edit_window, font=("Arial", 17), text="SỐ LƯỢNG SINH VIÊN:", bg="white", fg="black")
        student_label.place(x=locationX, y=locationY + 4 * backUpLocationY)

        self.textSTTDepartment = tk.Entry(self.edit_window, font=("Arial", 17), fg="black", width=30, borderwidth=1,state="readonly")
        self.textSTTDepartment.place(x=locationEntry, y=locationY)
        self.textIDDepartment = tk.Entry(self.edit_window, font=("Arial", 17), fg="black", width=30, borderwidth=1,state="readonly")
        self.textIDDepartment.place(x=locationEntry, y=locationY + backUpLocationY)
        self.textNameDepartment = tk.Entry(self.edit_window, font=("Arial", 17), fg="black", width=30, borderwidth=1,state="readonly")
        self.textNameDepartment.place(x=locationEntry, y=locationY + 2 * backUpLocationY)
        self.textLeadDepartment = tk.Entry(self.edit_window, font=("Arial", 17), fg="black", width=30, borderwidth=1,state="readonly")
        self.textLeadDepartment.place(x=locationEntry, y=locationY + 3 * backUpLocationY)
        self.textStudentDepartment = tk.Entry(self.edit_window, font=("Arial", 17), fg="black", width=30, borderwidth=1,state="readonly")
        self.textStudentDepartment.place(x=locationEntry, y=locationY + 4 * backUpLocationY)

        buttonUpdate = tk.Button(self.edit_window, text="Cập nhật thông tin mới cho khoa", font=("Arial", 18, "bold"),
                                bg="black", fg="white", width=30, height=2, bd=0, command = self.update_department)
        buttonUpdate.place(x=200, y=locationY + 5 * backUpLocationY + 20)

            # Sự kiện hover vào button
        buttonUpdate.bind("<Enter>", lambda e:buttonUpdate.config(bg="red", fg="white"))

            # Sự kiện rời khỏi button
        buttonUpdate.bind("<Leave>", lambda e:buttonUpdate.config(bg="black", fg="white"))

    def generate_unique_id(self):
        return int(uuid.uuid4().int % (2**29))
    
    def save_department(self):
        department_name = self.department_name_entry.get().strip()

        if not department_name:
            messagebox.showwarning("Thiếu thông tin", "Vui lòng nhập tên khoa.")
            return

        department = Department(
            id=self.generate_unique_id(),  # hoặc để None nếu để DB tự sinh
            name=department_name
        )

        print(department)
        DepartmentDAO.save(department)

        messagebox.showinfo("Thành công", f"Đã thêm khoa: {department_name}")
        self.detail_window.destroy()
        self.refresh_department_list()

    def delete_department(self):
        selected_item = self.tree.selection()
        if selected_item:
            department_id = self.tree.item(selected_item[0])["values"][1]
            name_department = self.tree.item(selected_item[0])["values"][2]
            confirm = messagebox.askyesno("Xác nhận xóa", f"Bạn có chắc chắn muốn xóa {name_department} không?")
            if confirm:
                try:
                    DepartmentDAO.delete(department_id)
                    self.refresh_department_list()
                    messagebox.showinfo("Thông báo", "Xóa thành công.")
                except Exception as e:
                    messagebox.showerror("Error", str(e))
        else:
            messagebox.showinfo("Thông báo", "Vui lòng chọn khoa để xóa.")

if __name__ == '__main__':
    app = DepartmentGUI()
    app.mainloop()