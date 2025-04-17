import os
import sys
import tkinter as tk
from tkinter import ttk


sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from dao import ScheduleDAO, ScheduleDetailDAO, DepartmentDAO, SemesterDAO

class DepartmentScheduleFrame(ttk.Frame):
    def __init__(self, parent, department_id=1, back_callback=None, close_callback=None):
        super().__init__(parent)
        self.department_id = department_id
        self.back_callback = back_callback
        self.close_callback = close_callback
        self.setup_ui()
        self.load_data()

    def setup_ui(self):
        # Create main container
        self.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)

        # Create header frame
        header_frame = ttk.Frame(self)
        header_frame.pack(fill=tk.X, pady=(0, 10))

        # Get department name for title
        department = DepartmentDAO.get_by_id(self.department_id)
        department_name = department.name if department else "Unknown Department"
        
        # Add title label
        title_label = ttk.Label(header_frame, text=f"Schedule for {department_name}", font=("Arial", 14, "bold"))
        title_label.pack(side=tk.LEFT)

        # Add buttons frame
        buttons_frame = ttk.Frame(header_frame)
        buttons_frame.pack(side=tk.RIGHT)

        # Add back button
        if self.back_callback:
            back_button = ttk.Button(buttons_frame, text="Back to Departments", command=self.back_callback)
            back_button.pack(side=tk.LEFT, padx=5)

        # Add close button
        if self.close_callback:
            close_button = ttk.Button(buttons_frame, text="Close", command=self.close_callback)
            close_button.pack(side=tk.LEFT, padx=5)

        # Create Treeview for schedules
        self.tree = ttk.Treeview(self, columns=('ID', 'Semester', 'Description', 'Schedule Details'), show='headings')
        self.tree.heading('ID', text='ID')
        self.tree.heading('Semester', text='Semester')
        self.tree.heading('Description', text='Description')
        self.tree.heading('Schedule Details', text='Schedule Details')
        
        # Set column widths
        self.tree.column('ID', width=50)
        self.tree.column('Semester', width=150)
        self.tree.column('Description', width=200)
        self.tree.column('Schedule Details', width=300)

        # Add scrollbar
        scrollbar = ttk.Scrollbar(self, orient=tk.VERTICAL, command=self.tree.yview)
        self.tree.configure(yscrollcommand=scrollbar.set)

        # Pack widgets
        self.tree.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

        # Add status bar
        self.status_bar = ttk.Label(self, text="", relief=tk.SUNKEN, anchor=tk.W)
        self.status_bar.pack(side=tk.BOTTOM, fill=tk.X, pady=(10, 0))

    def load_data(self):
        # Clear existing items
        for item in self.tree.get_children():
            self.tree.delete(item)

        # Get department name
        department = DepartmentDAO.get_by_id(self.department_id)
        if not department:
            self.status_bar.config(text="Error: Department not found")
            return

        # Get all schedules for the department
        schedules = ScheduleDAO.get_by_department_id(self.department_id)
        
        if not schedules:
            self.status_bar.config(text="No schedules found for this department")
            return
            
        for schedule in schedules:
            # Get semester information
            semester = SemesterDAO.get_by_id(schedule.semesterId)
            semester_name = semester.name if semester else "Unknown"

            # Get schedule details
            schedule_details = ScheduleDetailDAO.get_by_schedule_id(schedule.id)
            details_text = ""
            for detail in schedule_details:
                details_text += f"{detail.dayOfWeek}: {detail.startTime}-{detail.endTime}\n"

            # Insert into treeview
            self.tree.insert('', tk.END, values=(
                schedule.id,
                semester_name,
                schedule.description,
                details_text.strip()
            ))
            
        self.status_bar.config(text=f"Found {len(schedules)} schedules for {department.name}") 