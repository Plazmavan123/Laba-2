import tkinter as tk
from tkinter import messagebox


class ToDoUI:
    def init(self, root, task_manager):
        self.root = root
        self.root.title("To-Do List")
        self.task_manager = task_manager

        # Установка цвета фона для главного окна
        self.root.configure(bg="#CCEEFF")  # Светло-голубой цвет

        # Создание интерфейса
        self.create_widgets()

    def create_widgets(self):
        # Поле ввода задачи
        self.input_frame = tk.Frame(self.root, bg="#f0f8ff")  # Цвет фона совпадает с окном
        self.input_frame.pack(pady=10)

        self.task_entry = tk.Entry(self.input_frame, width=40)
        self.task_entry.pack(side=tk.LEFT, padx=5)

        # Кнопка "Добавить" с кастомными цветами
        self.add_button = tk.Button(
            self.input_frame,
            text="Добавить",
            bg="#4CAF50",  # Зеленый цвет кнопки
            fg="white",  # Белый цвет текста
            activebackground="#45a049",  # Темно-зеленый цвет при наведении
            activeforeground="white"  # Белый цвет текста при наведении
        )
        self.add_button.pack(side=tk.LEFT)
        self.add_button.config(command=self.add_task)  # Добавляем действие после создания кнопки

        # Список задач
        self.listbox = tk.Listbox(
            self.root,
            width=50,
            height=15,
            selectmode=tk.SINGLE,
            bg="#f9f9f9",  # Светло-серый фон
            fg="black"  # Черный текст
        )
        self.listbox.pack(pady=10)

        # Нижние кнопки
        self.button_frame = tk.Frame(self.root, bg="#f0f8ff")
        self.button_frame.pack(pady=10)

        self.delete_button = tk.Button(
            self.button_frame,
            text="Удалить задачу",
            bg="#0000FF",  # Темно-синий
            fg="white",
            activebackground="#e64a19",
            activeforeground="white"
        )
        self.delete_button.pack(side=tk.LEFT, padx=5)
        self.delete_button.config(command=self.delete_task)

        self.clear_button = tk.Button(
            self.button_frame,
            text="Очистить все",
            bg="#0000FF",  # Темно- синий 
            fg="white",
            activebackground="#455a64",
            activeforeground="white"
        )
        self.clear_button.pack(side=tk.LEFT, padx=5)
        self.clear_button.config(command=self.clear_all_tasks)

        self.exit_button = tk.Button(
            self.button_frame,
            text="Выход",
            bg="#f44336",  # Красный цвет
            fg="white",
            activebackground="#d32f2f",
            activeforeground="white",
            command=self.root.quit
        )
        self.exit_button.pack(side=tk.LEFT, padx=5)

    def add_task(self):
        task = self.task_entry.get()
        if task.strip():  # Проверка на пустую строку
            self.task_manager.add_task(task)
            self.listbox.insert(tk.END, task)
            self.task_entry.delete(0, tk.END)
        else:
            messagebox.showwarning("Ошибка", "Введите задачу!")

    def delete_task(self):
        try:
            selected_task_index = self.listbox.curselection()[0]
            self.listbox.delete(selected_task_index)
            self.task_manager.delete_task(selected_task_index)
        except IndexError:
            messagebox.showwarning("Ошибка", "Выберите задачу для удаления!")

    def clear_all_tasks(self):
        self.task_manager.clear_all_tasks()
        self.listbox.delete(0, tk.END)