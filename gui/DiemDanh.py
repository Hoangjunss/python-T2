import tkinter as tk
from tkinter import Image, ttk, messagebox
from PIL import Image, ImageTk
import sys
import os
import cv2,os
import pandas as pd
from tkcalendar import DateEntry

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from dao import AttendancesDAO, ClassDAO, DepartmentDAO, StudentDAO, TeacherDAO
import datetime
import time
from datetime import datetime


from dao.TestDAO import TestDAO
from models.Students import Student
from models.Attendances import Attendances
class DiemDanh(tk.Frame):
    def __init__(self, parent=None, teacherId=None):
        super().__init__(parent)
        self.parent = parent
        self.time= datetime.today()
        self.teacherId = teacherId
        self.DiemDanh()
        self.refresh_list(self.time, self.teacherId)

    def DiemDanh(self):

        frame_top = tk.Frame(self)
        frame_top.pack(fill=tk.X, padx=10, pady=10)

        
        # Tạo frame để chứa các widget liên quan đến ngày
        date_frame = tk.Frame(frame_top)
        date_frame.pack(pady=20)

        selectDate = tk.Label(date_frame, text="Chọn ngày:", font=("Times New Roman", 25))
        selectDate.pack(side=tk.LEFT, padx=10)

        dateEntry = DateEntry(date_frame, width=13, background='white', foreground='black', borderwidth=2, font=("Times New Roman", 15))
        dateEntry.pack(side=tk.LEFT, padx=10)

        def getValueTime():
            selected_date = dateEntry.get_date()
            self.refresh_list(selected_date, self.teacherId)                            
            print(f"Selected date: {selected_date}")
            # Add your logic here to handle the selected date

        buttonGetValueTime = tk.Button(date_frame, text="chọn", font=("Times New Roman", 12), command=getValueTime)
        buttonGetValueTime.pack(side=tk.LEFT, padx=10)

        #Phần dưới (bảng và các nút)
        frame_bottom = tk.Frame(self)
        frame_bottom.pack(fill=tk.BOTH, expand=True, padx=10, pady=5)

        # Table
        frame_table = tk.Frame(frame_bottom)
        frame_table.pack(side=tk.LEFT, expand="true", fill=tk.BOTH, padx=5)

        columns = ("STT", "MSSV", "Họ tên", "Ngày sinh", "Giới tính", "Thời gian", "Trạng thái")
        self.tree = ttk.Treeview(frame_table, columns=columns, show="headings")

        for col in columns:
            self.tree.heading(col, text=col, command=lambda _col=col: self.treeview_sort_column(_col, False))
            self.tree.column(col, anchor="center")

        self.tree.column("STT", width=30)
        self.tree.column("MSSV", width=80)
        self.tree.column("Họ tên", width=180)
        self.tree.column("Ngày sinh", width=90)
        self.tree.column("Giới tính", width=50)
        self.tree.column("Thời gian", width=120)
        self.tree.column("Trạng thái", width=120)

        # Tạo Scrollbar
        scrollbar = ttk.Scrollbar(frame_table, orient="vertical", command=self.tree.yview)
        self.tree.configure(yscrollcommand=scrollbar.set)

        # Đặt Treeview và Scrollbar vào Frame
        self.tree.pack(side=tk.LEFT, expand=True, fill=tk.BOTH)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)


    def refresh_list(self,time, teacherId):
        # Xóa hết nội dung hiện tại
        for item in self.tree.get_children():
            self.tree.delete(item)
        i=1
        teacher = TeacherDAO.get_by_id(teacherId)
        print(teacher)
        try:
            attendance = AttendancesDAO.get_addtendent_by_time(time=time, departmentid=teacher.department_id)
            print(attendance)
            for at in attendance:
                print(3)
                student_info = StudentDAO.get_by_id(at.student_id)
                self.tree.insert("", "end", values=(
                    i,
                    student_info.id,
                    student_info.fullname,
                    student_info.dateOfBirth,
                    student_info.gender,
                    at.checkin_time,
                    at.status

                ))
                i += 1
        except Exception as e:
            print(f'Error: {e}')
            messagebox.showerror('Error', str(e))

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
    
    def diem_danh(self):
        recognizer = cv2.face.LBPHFaceRecognizer_create()#cv2.createLBPHFaceRecognizer()
        recognizer.read("gui/TrainingImageLabel/Trainner.yml")
        harcascadePath = "gui/haarcascade_frontalface_default.xml"
        faceCascade = cv2.CascadeClassifier(harcascadePath);    
        # df=pd.read_csv("StudentDetails\StudentDetails.csv")
        cam = cv2.VideoCapture(0)
        font = cv2.FONT_HERSHEY_SIMPLEX        
        col_names =  ['Id','Name','Date','Time']
        attendance = pd.DataFrame(columns = col_names)    
        while True:
            ret, im =cam.read()
            gray=cv2.cvtColor(im,cv2.COLOR_BGR2GRAY)
            faces=faceCascade.detectMultiScale(gray, 1.2,5)    
            for(x,y,w,h) in faces:
                cv2.rectangle(im,(x,y),(x+w,y+h),(225,0,0),2)
                Id, conf = recognizer.predict(gray[y:y+h,x:x+w])                                   
                if(conf < 50):
                    print(Id)
                    student=StudentDAO.get_by_id(Id)
                    ts = time.time()      
                   
                    # Lấy thời gian hiện tại
                    current_time = datetime.now()

                    # Chuyển sang định dạng MySQL DATETIME
                    formatted_time = current_time.strftime('%Y-%m-%d %H:%M:%S')
                   # aa=df.loc[df['Id'] == Id]['Name'].values
                    tt=str(Id)+"-"+student.fullname
                    attendance.loc[len(attendance)] = [Id,student.fullname,current_time,current_time]
                   
                    
                else:
                    Id='Unknown'                
                    tt=str(Id)             
                cv2.putText(im,str(tt),(x,y+h), font, 1,(255,255,255),2)        
            attendance=attendance.drop_duplicates(subset=['Id'],keep='first')    
            cv2.imshow('im',im) 
            if (cv2.waitKey(1)==ord('q')):
                break
            
        cam.release()
        attendances=Attendances(id=546123,  student_id=student.id, status="Điểm danh thành công", checkin_time=formatted_time, scheduledetail_id= 4)
        AttendancesDAO.save(attendances=attendances)
        cv2.destroyAllWindows()
        self.refresh_list(self.time, self.teacherId)
          
if __name__ == '__main__':
    app = DiemDanh()
    app.mainloop()