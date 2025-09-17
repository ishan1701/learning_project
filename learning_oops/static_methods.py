# one example
from abc import ABC


class TaskManager:
    def __init__(self):
        self.tasks = []

    def add(self, task):
        self.tasks.append(task)

    def remove(self, task):
        self.tasks.remove(task)


class TaskPresenter:
    # Here the class doesnt hold any members. Hence, the methods should be declared as static.
    @staticmethod
    def present(tasks):
        for task in tasks:
            print(task)


class TaskInput:
    # Here the class doesnt hold any members. Hence, the methods should be declared as static.
    @staticmethod
    def input_add():
        return input("Enter a task")

    @staticmethod
    def input_remove():
        return input("Enter a task to remove")

    @staticmethod
    def input_list():
        return input("Enter a list of tasks")


def main():
    tm = TaskManager()
    new_task = TaskInput.input_add()

    tm.add(new_task)
    TaskPresenter.present(tm.tasks)


if __name__ == "__main__":
    main()
