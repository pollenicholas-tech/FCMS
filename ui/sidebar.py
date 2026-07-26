import customtkinter as ctk
from config import SIDEBAR_WIDTH, COLORS


class Sidebar(ctk.CTkFrame):

    def __init__(self, parent):
        super().__init__(
            parent,
            width=SIDEBAR_WIDTH,
            fg_color=COLORS["sidebar"],
            corner_radius=0
        )

        self.grid_propagate(False)

        ctk.CTkLabel(
            self,
            text="FCMS",
            font=("Segoe UI",22,"bold"),
            text_color="white"
        ).pack(pady=(25,30))

        self.dashboard_btn=self.create_button("🏠 Dashboard")
        self.main_family_btn=self.create_button("👨 Main Families")
        self.sub_family_btn=self.create_button("👪 Sub Families")
        self.members_btn=self.create_button("👤 Members")
        self.contributions_btn=self.create_button("💰 Contributions")
        self.projects_btn=self.create_button("📂 Projects")
        self.reports_btn=self.create_button("📊 Reports")
        self.settings_btn=self.create_button("⚙ Settings")

        ctk.CTkButton(
            self,
            text="🚪 Exit",
            fg_color="#C0392B",
            hover_color="#922B21",
            command=parent.destroy
        ).pack(side="bottom",fill="x",padx=12,pady=20)

    def create_button(self,text):

        btn=ctk.CTkButton(
            self,
            text=text,
            anchor="w",
            height=42,
            fg_color="transparent",
            hover_color="#2A6F97",
            text_color="white"
        )

        btn.pack(fill="x",padx=12,pady=3)

        return btn

