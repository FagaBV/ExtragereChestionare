import customtkinter as ctk

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")


class MainWindow(ctk.CTk):

    def __init__(self):
        super().__init__()

        self.title("Extragere Chestionare")
        self.geometry("900x650")

        self.label = ctk.CTkLabel(
            self,
            text="Extragere Chestionare PDF",
            font=("Arial", 26, "bold")
        )

        self.label.pack(pady=30)

        self.pdf_button = ctk.CTkButton(
            self,
            text="Alege PDF"
        )

        self.pdf_button.pack(pady=15)

        self.start_button = ctk.CTkButton(
            self,
            text="Procesează"
        )

        self.start_button.pack(pady=15)

        self.progress = ctk.CTkProgressBar(self)

        self.progress.pack(fill="x", padx=30, pady=30)

        self.progress.set(0)
