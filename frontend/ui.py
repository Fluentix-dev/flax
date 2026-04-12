import customtkinter as ctk
from PIL import Image

# Basic Configuration
ctk.set_appearance_mode("light") 

class LoginApp(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.title("Welcome Back")
        self.geometry("400x550")
        self.configure(fg_color="#FDF8F5") # Soft cream background

        # Layout Grid
        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(0, weight=1)

        # Main Container (The "Card")
        self.main_frame = ctk.CTkFrame(
            self, 
            corner_radius=24, 
            fg_color="white", 
            border_color="#EAE0DA", 
            border_width=1
        )
        self.main_frame.grid(row=0, column=0, padx=30, pady=40, sticky="nsew")
        self.main_frame.grid_columnconfigure(0, weight=1)

        # --- UI Elements ---
        
        # Logo placeholder (Google-style but cozy)
        self.logo_label = ctk.CTkLabel(
            self.main_frame, 
            text="G", 
            font=("Inter", 32, "bold"),
            text_color="#D4A373" # Warm terracotta
        )
        self.logo_label.pack(pady=(30, 5))

        self.title_label = ctk.CTkLabel(
            self.main_frame, 
            text="Sign in", 
            font=("Inter", 22),
            text_color="#463F3A"
        )
        self.title_label.pack(pady=(0, 5))

        self.subtitle_label = ctk.CTkLabel(
            self.main_frame, 
            text="Use your Cozy Account", 
            font=("Inter", 13),
            text_color="#8A817C"
        )
        self.subtitle_label.pack(pady=(0, 30))

        # Input Fields
        self.email_entry = ctk.CTkEntry(
            self.main_frame, 
            placeholder_text="Email or phone", 
            width=280, 
            height=50,
            corner_radius=8,
            border_color="#BCB8B1",
            fg_color="transparent"
        )
        self.email_entry.pack(pady=10)

        self.password_entry = ctk.CTkEntry(
            self.main_frame, 
            placeholder_text="Enter your password", 
            show="*", 
            width=280, 
            height=50,
            corner_radius=8,
            border_color="#BCB8B1",
            fg_color="transparent"
        )
        self.password_entry.pack(pady=10)

        # Forgot link
        self.forgot_btn = ctk.CTkButton(
            self.main_frame, 
            text="Forgot password?", 
            fg_color="transparent", 
            text_color="#A98467", 
            hover_color="#F5EBE0",
            font=("Inter", 12, "bold"),
            width=100
        )
        self.forgot_btn.pack(anchor="w", padx=45, pady=(0, 20))

        # Footer Buttons
        self.footer_frame = ctk.CTkFrame(self.main_frame, fg_color="transparent")
        self.footer_frame.pack(fill="x", side="bottom", pady=30, padx=40)

        self.create_account_btn = ctk.CTkButton(
            self.footer_frame, 
            text="Create account", 
            fg_color="transparent", 
            text_color="#A98467", 
            hover_color="#F5EBE0",
            font=("Inter", 13, "bold"),
            width=100
        )
        self.create_account_btn.pack(side="left")

        self.next_btn = ctk.CTkButton(
            self.footer_frame, 
            text="Next", 
            fg_color="#D4A373", 
            hover_color="#BC8A5F",
            text_color="white",
            font=("Inter", 13, "bold"),
            width=80,
            height=36,
            corner_radius=20
        )
        self.next_btn.pack(side="right")

if __name__ == "__main__":
    app = LoginApp()
    app.mainloop()