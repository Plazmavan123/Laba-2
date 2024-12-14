import tkinter as tk
from task_manager import TaskManager
from ui import ToDoUI


def main():
    # Создаем корневое окно
    root = tk.Tk()

    # Создаем менеджер задач
    task_manager = TaskManager()

    # Передаем менеджер задач в интерфейс
    app = ToDoUI(root, task_manager)

    # Запускаем приложение
    root.mainloop()


if __name__ == "__main__":
    main()