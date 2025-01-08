import tkinter as tk
from tkinter import messagebox

# Create the main application
class ToDoApp:
    def __init__(self, root):
        self.root = root
        self.root.title("To-Do List App")
        self.root.geometry("400x500")
        self.root.config(bg="#fdfdfd")

        # Title Label
        title_label = tk.Label(self.root, text="To-Do List", font=("Arial", 20, "bold"), fg="#4a4a4a", bg="#fdfdfd")
        title_label.pack(pady=10)

        # Task Entry Field
        self.task_entry = tk.Entry(self.root, font=("Arial", 14), bg="#f1f1f1", bd=0, highlightthickness=1)
        self.task_entry.pack(pady=10, padx=20, fill="x")
        self.task_entry.config(highlightbackground="#cccccc", highlightcolor="#4caf50")

        # Add Task Button
        add_button = tk.Button(self.root, text="Add Task", font=("Arial", 12), bg="#4caf50", fg="white", bd=0,
                               command=self.add_task)
        add_button.pack(pady=10)

        # Task List
        self.task_listbox = tk.Listbox(self.root, font=("Arial", 14), bg="#f9f9f9", fg="#4a4a4a", selectbackground="#4caf50")
        self.task_listbox.pack(pady=10, padx=20, fill="both", expand=True)

        # Delete Button
        delete_button = tk.Button(self.root, text="Delete Task", font=("Arial", 12), bg="#e74c3c", fg="white", bd=0,
                                  command=self.delete_task)
        delete_button.pack(pady=5, padx=20, fill="x")

        # Mark as Done Button
        mark_done_button = tk.Button(self.root, text="Mark as Done", font=("Arial", 12), bg="#3498db", fg="white", bd=0,
                                     command=self.mark_done)
        mark_done_button.pack(pady=5, padx=20, fill="x")

    def add_task(self):
        """Add a new task to the list."""
        task = self.task_entry.get().strip()
        if task:
            self.task_listbox.insert(tk.END, task)
            self.task_entry.delete(0, tk.END)
        else:
            messagebox.showwarning("Warning", "Task cannot be empty!")

    def delete_task(self):
        """Delete the selected task."""
        try:
            selected_task_index = self.task_listbox.curselection()[0]
            self.task_listbox.delete(selected_task_index)
        except IndexError:
            messagebox.showwarning("Warning", "Please select a task to delete!")

    def mark_done(self):
        """Mark the selected task as done."""
        try:
            selected_task_index = self.task_listbox.curselection()[0]
            task = self.task_listbox.get(selected_task_index)
            # Mark the task as done
            if not task.startswith("✔"):
                self.task_listbox.delete(selected_task_index)
                self.task_listbox.insert(selected_task_index, f"✔ {task}")
        except IndexError:
            messagebox.showwarning("Warning", "Please select a task to mark as done!")

# Run the application
if __name__ == "__main__":
    root = tk.Tk()
    app = ToDoApp(root)
    root.mainloop()
