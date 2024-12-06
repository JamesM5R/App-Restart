import customtkinter as ctk
from PIL import Image
import os

class HomeFrame(ctk.CTkFrame):
    def __init__(self, parent):
        super().__init__(parent, corner_radius=0, fg_color="white")
        self.grid_rowconfigure(0, weight=1)  # Expandable space
        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(10, weight=0) # Footer at the bottom
        # Label for title
        self.home_label = ctk.CTkLabel(self, text="Workspace Management Application", font=("Arial", 20, "bold"), text_color=("dodgerblue", "blue2"))
        self.home_label.grid(row=0, column=0, padx=20, pady=20)

        # Construct the image path
        image_path = os.path.join(os.path.dirname(__file__), "test_images", "Slide1.png")  # Replace 'your_image.png' with your image filename
        
        # Load the image
        self.image = Image.open(image_path)
        #self.image = self.image.resize((200, 200))  # Resize to fit in your frame

        # Create a CTkImage object
        self.image_tk = ctk.CTkImage(self.image, size=(1080, 600))

        # Label to display the image
        self.image_label = ctk.CTkLabel(self, image=self.image_tk, text="")
        self.image_label.grid(row=1, column=0, padx=20, pady=20)

        # Footer
        footer = ctk.CTkLabel(
            self, 
            text="© 2024 Workspace Management Application. Capgemini Engineering.", 
            font=("Arial", 10, 'italic'), 
            text_color="black", 
            fg_color="white"
        )
        footer.grid(row=10, column=0, columnspan=2, padx=20, pady=10, sticky="ew")

    
