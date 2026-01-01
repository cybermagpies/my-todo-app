import customtkinter as ctk

# Styling configuration
ctk.set_appearance_mode("light")
ctk.set_default_color_theme("blue")

class TodoApp(ctk.CTk):
    def __init__(self):
        super().__init__()

        # Window Setup
        self.title("Cybermagpies Task Manager")
        self.geometry("400x700")
        self.configure(fg_color="#F2F5FF") # Soft Dribbble background

        # 1. HEADER SECTION
        self.header_frame = ctk.CTkFrame(self, fg_color="transparent")
        self.header_frame.pack(fill="x", padx=30, pady=(40, 20))
        
        self.title_label = ctk.CTkLabel(self.header_frame, text="My Tasks", 
                                        font=("Helvetica", 28, "bold"), text_color="#2D3142")
        self.title_label.pack(side="left")

        # 2. CATEGORY BUBBLES
        self.category_frame = ctk.CTkFrame(self, fg_color="transparent")
        self.category_frame.pack(fill="x", padx=30, pady=10)
        
        categories = ["All", "Work", "Personal"]
        for cat in categories:
            btn = ctk.CTkButton(self.category_frame, text=cat, width=80, height=32, 
                                corner_radius=16, fg_color="white", text_color="#5271FF",
                                hover_color="#E0E7FF", font=("Helvetica", 12, "bold"))
            btn.pack(side="left", padx=(0, 10))

        # 3. TASK LIST (The "Cards")
        self.task_list_frame = ctk.CTkScrollableFrame(self, fg_color="transparent", width=340, height=450)
        self.task_list_frame.pack(pady=10)

        # 4. BOTTOM INPUT BAR (The Floating Bar)
        self.input_frame = ctk.CTkFrame(self, fg_color="white", corner_radius=25, height=60)
        self.input_frame.pack(side="bottom", fill="x", padx=20, pady=30)
        self.input_frame.pack_propagate(False)

        self.entry = ctk.CTkEntry(self.input_frame, placeholder_text="Add a new task...", 
                                  fg_color="transparent", border_width=0, width=280)
        self.entry.pack(side="left", padx=20, pady=10)

        self.add_btn = ctk.CTkButton(self.input_frame, text="+", width=40, height=40, 
                                     corner_radius=20, fg_color="#5271FF", 
                                     font=("Helvetica", 20, "bold"), command=self.add_task)
        self.add_btn.pack(side="right", padx=10)

    def add_task(self):
        task_text = self.entry.get()
        if task_text:
            # Create a stylized Task Card
            card = ctk.CTkFrame(self.task_list_frame, fg_color="white", corner_radius=15, height=50)
            card.pack(fill="x", pady=5, padx=5)
            
            check = ctk.CTkCheckBox(card, text=task_text, font=("Helvetica", 14), 
                                    border_color="#5271FF", hover_color="#E0E7FF",
                                    checkmark_color="white", fg_color="#5271FF")
            check.pack(side="left", padx=15, pady=10)
            
            self.entry.delete(0, 'end')

if __name__ == "__main__":
    app = TodoApp()
    app.mainloop()
