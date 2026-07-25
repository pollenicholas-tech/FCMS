import customtkinter as ctk
from config import *
from ui.sidebar import Sidebar
from ui.dashboard import Dashboard
class MainWindow(ctk.CTk):
    def __init__(self): super().__init__();self.title(APP_NAME)