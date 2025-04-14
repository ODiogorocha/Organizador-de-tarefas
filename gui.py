import tkinter as tk
from tkinter import ttk, messagebox
from task_utils import load_tasks, save_tasks, suggest_next_task
from task import Task
import platform

class TaskManagerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Task Manager")

        # Definir tamanho fixo para a janela (800x600)
        self.root.geometry("800x600")

        # Permitir que a janela seja redimensionada
        self.root.resizable(True, True)

        # Definir tela cheia ou maximizada conforme o SO (isso será removido para um tamanho fixo)
        # Com o tamanho fixo, não precisaremos de tela cheia ou maximizada.
        # if platform.system() == "Windows":
        #     self.root.state("zoomed")
        # else:
        #     self.root.attributes("-fullscreen", True)

        self.tasks = load_tasks()
        self.create_widgets()
        self.update_task_list()

        # Adicionar um atalho de teclado para sair do programa (tecla ESC)
        self.root.bind("<Escape>", self.exit_program)

    def create_widgets(self):
        # Task entry
        self.name_label = ttk.Label(self.root, text="Task Name:")
        self.name_label.grid(row=0, column=0, padx=5, pady=5)

        self.name_entry = ttk.Entry(self.root, width=30)
        self.name_entry.grid(row=0, column=1, padx=5, pady=5)

        self.priority_label = ttk.Label(self.root, text="Priority:")
        self.priority_label.grid(row=1, column=0, padx=5, pady=5)

        self.priority_combo = ttk.Combobox(self.root, values=["High", "Medium", "Low"], state="readonly")
        self.priority_combo.grid(row=1, column=1, padx=5, pady=5)
        self.priority_combo.current(0)

        self.add_button = ttk.Button(self.root, text="Add Task", command=self.add_task)
        self.add_button.grid(row=2, column=0, columnspan=2, pady=10)

        # Task list display
        self.task_listbox = tk.Listbox(self.root, width=50, selectmode=tk.SINGLE)
        self.task_listbox.grid(row=3, column=0, columnspan=2, padx=10, pady=5)

        self.suggest_button = ttk.Button(self.root, text="Suggest Next Task", command=self.suggest_task)
        self.suggest_button.grid(row=4, column=0, columnspan=2, pady=10)

        # Add button to delete task
        self.delete_button = ttk.Button(self.root, text="Delete Task", command=self.delete_task)
        self.delete_button.grid(row=5, column=0, columnspan=2, pady=10)

    def add_task(self):
        name = self.name_entry.get()
        priority = self.priority_combo.get()

        if not name:
            messagebox.showwarning("Warning", "Task name cannot be empty.")
            return

        task = Task(name, priority)
        self.tasks.append(task)
        save_tasks(self.tasks)
        self.update_task_list()

        self.name_entry.delete(0, tk.END)

    def update_task_list(self):
        self.task_listbox.delete(0, tk.END)
        for task in self.tasks:
            self.task_listbox.insert(tk.END, f"{task.name} [Priority: {task.priority}]")

    def suggest_task(self):
        task = suggest_next_task(self.tasks)
        if task:
            messagebox.showinfo("Suggested Task", f"{task.name} [Priority: {task.priority}]")
        else:
            messagebox.showinfo("No Suggestion", "No tasks available.")

    def delete_task(self):
        try:
            # Get the selected task
            selected_index = self.task_listbox.curselection()[0]
            selected_task = self.tasks[selected_index]

            # Remove the task from the list
            self.tasks.remove(selected_task)
            save_tasks(self.tasks)

            # Update the listbox to reflect the change
            self.update_task_list()

            messagebox.showinfo("Task Deleted", f"Task '{selected_task.name}' has been deleted.")
        except IndexError:
            messagebox.showwarning("No Selection", "Please select a task to delete.")

    def exit_program(self, event=None):
        """Fecha o programa quando a tecla Esc é pressionada"""
        self.root.quit()

if __name__ == "__main__":
    root = tk.Tk()
    app = TaskManagerApp(root)
    root.mainloop()
