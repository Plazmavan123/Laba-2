class TaskManager:
    def init(self):
        # Хранение задач в списке
        self.tasks = []

    def add_task(self, task):
        """Добавляет задачу в список."""
        self.tasks.append(task)

    def delete_task(self, index):
        """Удаляет задачу по индексу."""
        if 0 <= index < len(self.tasks):
            del self.tasks[index]
        else:
            raise IndexError("Индекс задачи вне диапазона.")

    def clear_all_tasks(self):
        """Очищает весь список задач."""
        self.tasks.clear()
