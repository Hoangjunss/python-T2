import os
import sys
import tkinter as tk
from tkinter import ttk, messagebox


sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from dao import DepartmentDAO
from models.Department import Department

class DepartmentGUI(tk.Tk):
    def __init__(self):
        super().__init__()
        self.gui_Department()
        self.refresh_department_list()
        self.mainloop()

    def gui_Department(self):
        self.title('Phần Mềm Điểm Danh Sinh Viên Bằng Nhận Diện Khuôn Mặt')
        self.geometry('850x650')

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

        btn_edit = tk.Button(frame_btns, text="Sửa")
        btn_edit.pack(fill=tk.X, padx=10, pady=10)
        
        btn_delete = tk.Button(frame_btns, text="Xóa", command= self.delete_department)
        btn_delete.pack(fill=tk.X, padx=10, pady=10)

        btn_show_detail= tk.Button(frame_btns, text="Chi tiết")
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
                # print("=============================================")
                # print(dep.id)
                # print(dep.name)
                # print(quantity_students)
                # print("=============================================")
        except Exception as e:
            print(f"Error: {e}")
            messagebox.showerror("Error", str(e))   

    def add_department(self):
        detail_window = tk.Toplevel(self)
        detail_window.title("Thông Tin Chi Tiết")
        detail_window.geometry("300x250")

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