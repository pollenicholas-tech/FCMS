import customtkinter as ctk
from tkinter import messagebox
from database.database import Database

class MainFamilies(ctk.CTkFrame):

    def __init__(self,parent):
        super().__init__(parent)
        self.db=Database()
        self.build_ui()

    def build_ui(self):
        ctk.CTkLabel(self,text="Main Families",
                     font=("Segoe UI",28,"bold")).pack(anchor="w",padx=20,pady=(20,10))

        top=ctk.CTkFrame(self)
        top.pack(fill="x",padx=20)

        self.search_box=ctk.CTkEntry(top,width=300,placeholder_text="Search family...")
        self.search_box.pack(side="left",padx=5,pady=10)

        ctk.CTkButton(top,text="Search",command=self.load_data).pack(side="left",padx=5)
        ctk.CTkButton(top,text="+ Add Family",command=self.open_add_dialog).pack(side="right",padx=5)

        self.table_frame=ctk.CTkFrame(self)
        self.table_frame.pack(fill="both",expand=True,padx=20,pady=20)

        self.load_data()

    def load_data(self):
        for w in self.table_frame.winfo_children():
            w.destroy()

        headers=["ID","Family Name","Coordinator","Description"]
        for c,h in enumerate(headers):
            ctk.CTkLabel(self.table_frame,text=h,font=("Segoe UI",14,"bold")).grid(row=0,column=c,padx=10,pady=10,sticky="w")

        for r,row in enumerate(self.db.get_main_families(),start=1):
            for c,val in enumerate(row):
                ctk.CTkLabel(self.table_frame,text=str(val)).grid(row=r,column=c,padx=10,pady=6,sticky="w")

    def open_add_dialog(self):

    dlg = ctk.CTkToplevel(self)

    dlg.title("Add Main Family")
    dlg.geometry("450x320")
    dlg.resizable(False, False)

    # Keep the dialog in front
    dlg.transient(self.winfo_toplevel())
    dlg.grab_set()
    dlg.focus_force()
    dlg.lift()
    dlg.attributes("-topmost", True)
    dlg.after(100, lambda: dlg.attributes("-topmost", False))

    ctk.CTkLabel(
        dlg,
        text="Family Name"
    ).pack(pady=(15, 5))

    e1 = ctk.CTkEntry(dlg, width=300)
    e1.pack()

    ctk.CTkLabel(
        dlg,
        text="Coordinator"
    ).pack(pady=(10, 5))

    e2 = ctk.CTkEntry(dlg, width=300)
    e2.pack()

    ctk.CTkLabel(
        dlg,
        text="Description"
    ).pack(pady=(10, 5))

    e3 = ctk.CTkEntry(dlg, width=300)
    e3.pack()

    def save():

        family = e1.get().strip()

        if family == "":
            messagebox.showerror(
                "Error",
                "Family Name is required."
            )
            return

        self.db.add_main_family(
            family,
            e2.get().strip(),
            e3.get().strip()
        )

        self.load_data()

        dlg.destroy()

        messagebox.showinfo(
            "Success",
            "Family saved successfully."
        )

    ctk.CTkButton(
        dlg,
        text="Save",
        command=save
    ).pack(pady=20)