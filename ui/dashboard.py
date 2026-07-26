import customtkinter as ctk
from config import COLORS


class Dashboard(ctk.CTkFrame):

    def __init__(self, parent):
        super().__init__(
            parent,
            fg_color=COLORS["background"]
        )

        self.build()

    def build(self):

        title = ctk.CTkLabel(
            self,
            text="Dashboard",
            font=("Segoe UI", 28, "bold"),
            text_color=COLORS["text"]
        )
        title.pack(anchor="w", padx=30, pady=(25, 20))

        cards = ctk.CTkFrame(self, fg_color="transparent")
        cards.pack(fill="x", padx=30)

        self.create_card(cards, "Main Families", "0").pack(
            side="left", padx=10
        )

        self.create_card(cards, "Members", "0").pack(
            side="left", padx=10
        )

        self.create_card(cards, "Projects", "0").pack(
            side="left", padx=10
        )

        self.create_card(cards, "Collected", "KSh 0").pack(
            side="left", padx=10
        )

    def create_card(self, parent, title, value):

        card = ctk.CTkFrame(
            parent,
            width=220,
            height=120,
            fg_color=COLORS["card"],
            corner_radius=12
        )

        card.pack_propagate(False)

        ctk.CTkLabel(
            card,
            text=title,
            font=("Segoe UI", 15)
        ).pack(pady=(18, 6))

        ctk.CTkLabel(
            card,
            text=value,
            font=("Segoe UI", 28, "bold"),
            text_color=COLORS["primary"]
        ).pack()

        return card