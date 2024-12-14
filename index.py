import tkinter as tk
from tkinter import messagebox


class ToDoApp:
    def __init__(self, root):
        self.root = root
        self.root.title("To-Do List")
        self.task_list = []

        # Создание интерфейса
        self.create_widgets()

    def create_widgets(self):
        # Поле ввода задачи
        self.input_frame = tk.Frame(self.root)
        self.input_frame.pack(pady=10)

        self.task_entry = tk.Entry(self.input_frame, width=40)
        self.task_entry.pack(side=tk.LEFT, padx=5)

        self.add_button = tk.Button(self.input_frame, text="Добавить", command=self.add_task)
        self.add_button.pack(side=tk.LEFT)

        # Список задач
        self.listbox = tk.Listbox(self.root, width=50, height=15, selectmode=tk.SINGLE)
        self.listbox.pack(pady=10)

        # Нижние кнопки
        self.button_frame = tk.Frame(self.root)
        self.button_frame.pack(pady=10)

        self.delete_button = tk.Button(self.button_frame, text="Удалить задачу", command=self.delete_task)
        self.delete_button.pack(side=tk.LEFT, padx=5)

        self.clear_button = tk.Button(self.button_frame, text="Очистить все", command=self.clear_all_tasks)
        self.clear_button.pack(side=tk.LEFT, padx=5)

        self.exit_button = tk.Button(self.button_frame, text="Выход", command=self.root.quit)
        self.exit_button.pack(side=tk.LEFT, padx=5)

    def add_task(self):
        task = self.task_entry.get()
        if task.strip():  # Проверка на пустую строку
            self.task_list.append(task)
            self.listbox.insert(tk.END, task)
            self.task_entry.delete(0, tk.END)
        else:
            messagebox.showwarning("Ошибка", "Введите задачу!")

    def delete_task(self):
        try:
            selected_task_index = self.listbox.curselection()[0]
            self.listbox.delete(selected_task_index)
            del self.task_list[selected_task_index]
        except IndexError:
            messagebox.showwarning("Ошибка", "Выберите задачу для удаления!")

    def clear_all_tasks(self):
        self.task_list.clear()
        self.listbox.delete(0, tk.END)


# Инициализация приложения
if __name__ == "__main__":
    root = tk.Tk()
    app = ToDoApp(root)
    root.mainloop()

    