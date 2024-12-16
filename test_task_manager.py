import unittest
from task_manager import TaskManager  # Импортируем класс TaskManager из вашего файла

class TestTaskManager(unittest.TestCase):
    def setUp(self):
        """Настройка перед каждым тестом."""
        self.manager = TaskManager()  # Создаём новый экземпляр TaskManager перед каждым тестом

    def test_add_task(self):
        """Тест: добавление задачи в список."""
        self.manager.add_task("Задача 1")
        self.assertIn("Задача 1", self.manager.tasks)  # Проверяем, что задача добавлена

    def test_delete_task(self):
        """Тест: удаление задачи по индексу."""
        self.manager.add_task("Задача 1")
        self.manager.add_task("Задача 2")
        self.manager.delete_task(0)  # Удаляем первую задачу
        self.assertNotIn("Задача 1", self.manager.tasks)  # Проверяем, что первой задачи больше нет
        self.assertIn("Задача 2", self.manager.tasks)  # Вторая задача осталась

    def test_delete_task_invalid_index(self):
        """Тест: удаление задачи с неверным индексом."""
        self.manager.add_task("Задача 1")
        with self.assertRaises(IndexError):  # Проверяем, что вызывается исключение IndexError
            self.manager.delete_task(5)

    def test_clear_all_tasks(self):
        """Тест: очистка всех задач."""
        self.manager.add_task("Задача 1")
        self.manager.add_task("Задача 2")
        self.manager.clear_all_tasks()
        self.assertEqual(len(self.manager.tasks), 0)  # Проверяем, что список пуст

if __name__ == "__main__":
    unittest.main()
