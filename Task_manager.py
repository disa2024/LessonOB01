#Создай класс Task, который позволяет управлять задачами (делами).
# У задачи должны быть атрибуты: описание задачи, срок выполнения и
# статус (выполнено/не выполнено). Реализуй функцию для добавления задач,
# отметки выполненных задач и вывода списка текущих (не выполненных) задач.

class Task():
    def __init__(self, name, deadline, status=0):
        self.name = name
        self.deadline = deadline
        self.status = status
    def execute(self):
        self.status = 1
    def __str__(self):
        if self.status == 1:
            status = "Выполнена"
        else:
            status = "Не выполнена"
        return f"{self.name}, {self.deadline}, статус: {status}"

class Task_manager():
    def __init__(self):
        self.tasks = []
    def add_task(self, name, deadline):
        task = Task(name, deadline)
        self.tasks.append(task)
    def change_status(self, task_index):
        if 0 <= task_index < len(self.tasks):
            self.tasks[task_index].execute()
            print("\n","Задача")
            print(self.tasks[task_index])
        else:
            print("Неверный индекс задачи")

    def all_tasks(self):
        print("\n","Все задачи:")
        for task in self.tasks:
            print(task)

    def get_current_tasks(self):
        for task in self.tasks:
            if task.status == 0:
                print("\n","Не выполненные задачи:")
                print(task)


# Пример использования
task = Task_manager()
task.add_task("Сделать домашнее задание", "16-00")
task.add_task("Купить продукты", "17-00")
task.all_tasks()
task.change_status(1)
task.get_current_tasks()
task.all_tasks()














