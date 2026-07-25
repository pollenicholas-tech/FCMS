import customtkinter as ctk
from config import APP_NAME,WINDOW_WIDTH,WINDOW_HEIGHT

class MainWindow(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title(APP_NAME)
        self.geometry(f'{WINDOW_WIDTH}x{WINDOW_HEIGHT}')
        ctk.CTkLabel(self,text='Welcome to FCMS',font=('Segoe UI',24)).pack(pady=40)
