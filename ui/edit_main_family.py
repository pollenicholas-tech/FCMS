import customtkinter as ctk
from tkinter import messagebox

class EditMainFamily(ctk.CTkToplevel):

    def __init__(self,parent,db,family_id,family_name,coordinator,description,on_saved):
        super().__init__(parent)

        self.db=db
        self.family_id=family_id
        self.on_saved=on_saved

        self.title("Edit Main Family")
        self.geometry("420x300")
        self.resizable(False,False)

        ctk.CTkLabel(self,text="Family Name").pack(pady=(15,5))
        self.family=ctk.CTkEntry(self,width=320)
        self.family.insert(0,family_name)
        self.family.pack()

        ctk.CTkLabel(self,text="Coordinator").pack(pady=(10,5))
        self.coord=ctk.CTkEntry(self,width=320)
        self.coord.insert(0,coordinator)
        self.coord.pack()

        ctk.CTkLabel(self,text="Description").pack(pady=(10,5))
        self.desc=ctk.CTkEntry(self,width=320)
        self.desc.insert(0,description)
        self.desc.pack()

        ctk.CTkButton(self,text="Save Changes",
                      command=self.save).pack(pady=20)

    def save(self):
        if not self.family.get().strip():
            messagebox.showerror("Validation","Family name is required.")
            return

        self.db.update_main_family(
            self.family_id,
            self.family.get().strip(),
            self.coord.get().strip(),
            self.desc.get().strip()
        )

        messagebox.showinfo("Success","Family updated successfully.")

        if self.on_saved:
            self.on_saved()

        self.destroy()

