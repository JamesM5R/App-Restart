import pandas as pd 
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import customtkinter as ctk
from tkinter import Listbox, MULTIPLE

class DashboardFrame(ctk.CTkFrame):
    def __init__(self, parent):
        super().__init__(parent, corner_radius=0, fg_color="white")
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=1)

        self.dashboard_label = ctk.CTkLabel(
            self,
            text="Dashboard",
            font=("Arial", 20, "bold"),
            text_color=("dodgerblue", "blue2"),
        )
        self.dashboard_label.grid(row=0, column=0, padx=20, pady=20, sticky="n")

        # Placeholder for the plot
        self.plot_frame = ctk.CTkFrame(self, fg_color="white")
        self.plot_frame.grid(row=1, column=0, padx=20, pady=20, sticky="nsew")

        footer = ctk.CTkLabel(
            self,
            text="© 2024 Workspace Management Application. Capgemini Engineering.",
            font=("Arial", 10, 'italic'),
            text_color="black",
            fg_color="white",
        )
        footer.grid(row=10, column=0, columnspan=2, padx=20, pady=10, sticky="ew")

    def plot_nested_donut_from_csv(self, file_path):
        """Loads data from a CSV file and generates the nested donut plot."""
        try:
            data = pd.read_csv(file_path)
            self.plot_nested_donut(data)
        except Exception as e:
            print(f"Error loading or plotting data: {e}")

    def plot_nested_donut(self, data):
        """Generates a nested donut plot with data labels displayed outside."""

        required_columns = [
            'Dates of Absences', 'Name', 'Email Name', 'Manager', 'Email Manager',
            'Week', 'Date of Send', 'Date of Response', 'Category', 'Justificative'
        ]
        if not all(col in data.columns for col in required_columns):
            raise ValueError(f"Data must include columns: {', '.join(required_columns)}")

        # Group the data by 'Category' and 'Justificative' and count the occurrences
        grouped_data = data.groupby(["Category", "Justificative"])["Name"].count().reset_index()
        grouped_data.rename(columns={"Name": "Count"}, inplace=True)

        category_counts = grouped_data.groupby("Category")["Count"].sum()
        justification_counts = grouped_data[["Category", "Justificative", "Count"]]

        # Colors for each ring
        a, b, c = [plt.cm.Blues, plt.cm.Reds, plt.cm.Greens]

        # Create the figure
        fig, ax = plt.subplots(figsize=(8, 6))
        ax.axis('equal')

        # First Ring (outer layer: Categories)
        mypie, _ = ax.pie(
            category_counts, 
            radius=1.3, 
            labels=category_counts.index, 
            colors=[a(0.6), b(0.6), c(0.6)], 
            labeldistance=1.1
        )
        plt.setp(mypie, width=0.3, edgecolor='white')

        # Second Ring (inner layer: Justifications)
        mypie2, _ = ax.pie(
            justification_counts["Count"], 
            radius=1.3 - 0.3, 
            labels=justification_counts["Justificative"], 
            labeldistance=0.7, 
            colors=[a(0.5), a(0.4), a(0.3), b(0.5), b(0.4), c(0.6), c(0.5), c(0.4), c(0.3), c(0.2)]
        )
        plt.setp(mypie2, width=0.4, edgecolor='white')

        # Title
        ax.set_title("Nested Donut Chart: Categories and Justifications", fontsize=14, weight='bold')

        # Embed into the tkinter canvas
        canvas = FigureCanvasTkAgg(fig, master=self.plot_frame)
        canvas.draw()
        canvas.get_tk_widget().pack(side="top", fill="both", expand=True)
