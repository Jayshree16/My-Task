import tkinter as tk
from tkinter import messagebox

class CalculatorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Calculator")
        self.root.geometry("300x400")
        self.root.config(bg="#fdfdfd")
        self.root.resizable(False, False)

        # Title Label
        title_label = tk.Label(self.root, text="Simple Calculator", font=("Arial", 16, "bold"), fg="#4a4a4a", bg="#fdfdfd")
        title_label.pack(pady=10)

        # First Number Entry
        self.first_num = tk.Entry(self.root, font=("Arial", 14), bd=1, relief="solid")
        self.first_num.pack(pady=10, padx=20, fill="x")

        # Second Number Entry
        self.second_num = tk.Entry(self.root, font=("Arial", 14), bd=1, relief="solid")
        self.second_num.pack(pady=10, padx=20, fill="x")

        # Operation Buttons Frame
        button_frame = tk.Frame(self.root, bg="#fdfdfd")
        button_frame.pack(pady=10)

        # Buttons for operations
        btn_add = tk.Button(button_frame, text="+", font=("Arial", 14), bg="#4caf50", fg="white", width=5, command=self.add)
        btn_add.grid(row=0, column=0, padx=5, pady=5)

        btn_subtract = tk.Button(button_frame, text="-", font=("Arial", 14), bg="#e67e22", fg="white", width=5, command=self.subtract)
        btn_subtract.grid(row=0, column=1, padx=5, pady=5)

        btn_multiply = tk.Button(button_frame, text="×", font=("Arial", 14), bg="#3498db", fg="white", width=5, command=self.multiply)
        btn_multiply.grid(row=1, column=0, padx=5, pady=5)

        btn_divide = tk.Button(button_frame, text="÷", font=("Arial", 14), bg="#e74c3c", fg="white", width=5, command=self.divide)
        btn_divide.grid(row=1, column=1, padx=5, pady=5)

        # Result Label
        self.result_label = tk.Label(self.root, text="Result: ", font=("Arial", 14), fg="#4a4a4a", bg="#fdfdfd")
        self.result_label.pack(pady=20)

    def get_numbers(self):
        """Retrieve numbers from the input fields."""
        try:
            num1 = float(self.first_num.get())
            num2 = float(self.second_num.get())
            return num1, num2
        except ValueError:
            messagebox.showerror("Input Error", "Please enter valid numbers.")
            return None, None

    def add(self):
        num1, num2 = self.get_numbers()
        if num1 is not None and num2 is not None:
            result = num1 + num2
            self.result_label.config(text=f"Result: {result}")

    def subtract(self):
        num1, num2 = self.get_numbers()
        if num1 is not None and num2 is not None:
            result = num1 - num2
            self.result_label.config(text=f"Result: {result}")

    def multiply(self):
        num1, num2 = self.get_numbers()
        if num1 is not None and num2 is not None:
            result = num1 * num2
            self.result_label.config(text=f"Result: {result}")

    def divide(self):
        num1, num2 = self.get_numbers()
        if num1 is not None and num2 is not None:
            if num2 != 0:
                result = num1 / num2
                self.result_label.config(text=f"Result: {result}")
            else:
                messagebox.showerror("Math Error", "Division by zero is not allowed.")

# Run the application
if __name__ == "__main__":
    root = tk.Tk()
    app = CalculatorApp(root)
    root.mainloop()
