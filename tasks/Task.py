from abc import ABC, abstractmethod


class Task(ABC):
    def __init__(self, name: str, number: int):
        self.number = number
        self.name = name

    @abstractmethod
    def display(self):
        pass

    @abstractmethod
    def on_mount(self):
        pass

    @abstractmethod
    def on_unmount(self):
        pass


