import customtkinter as ctk

from config import APP_NAME, WINDOW_WIDTH, WINDOW_HEIGHT

from ui.sidebar import Sidebar
from ui.dashboard import Dashboard
from ui.main_families import MainFamilies


class MainWindow(ctk.CTk):

    def __init__(self):
        super().__init__()

        self.title(APP_NAME)
        self.geometry(f"{WINDOW_WIDTH}x{WINDOW_HEIGHT}")
        self.minsize(1200,700)

        self.grid_columnconfigure(1,weight=1)
        self.grid_rowconfigure(0,weight=1)

        self.sidebar=Sidebar(self)
        self.sidebar.grid(row=0,column=0,sticky="ns")

        self.content=ctk.CTkFrame(self,fg_color="transparent")
        self.content.grid(row=0,column=1,sticky="nsew")

        self.sidebar.dashboard_btn.configure(command=self.show_dashboard)
        self.sidebar.main_family_btn.configure(command=self.show_main_families)

        self.show_dashboard()

    def clear_content(self):
        for widget in self.content.winfo_children():
            widget.destroy()

    def show_dashboard(self):
        self.clear_content()
        Dashboard(self.content).pack(fill="both",expand=True)

    def show_main_families(self):
        self.clear_content()
        MainFamilies(self.content).pack(fill="both",expand=True)

