from abc import ABC, abstractmethod


class FileSystemComponent(ABC):
    @abstractmethod
    def show(self, indent=0):
        pass


class File(FileSystemComponent):
    def __init__(self, name):
        self.name = name

    def show(self, indent=0):
        return "  " * indent + f"📄 {self.name}"


class Folder(FileSystemComponent):
    def __init__(self, name):
        self.name = name
        self.children = []

    def add(self, component):
        self.children.append(component)

    def remove(self, component):
        self.children.remove(component)

    def show(self, indent=0):
        result = "  " * indent + f"📁 {self.name}"
        for child in self.children:
            result += "\n" + child.show(indent + 1)
        return result


# Использование
root = Folder("Корневая папка")

documents = Folder("Документы")
documents.add(File("резюме.pdf"))
documents.add(File("договор.docx"))

photos = Folder("Фото")
photos.add(File("отпуск.jpg"))
photos.add(File("семья.png"))

documents.add(photos)
root.add(documents)
root.add(File("readme.txt"))

print("Структура файловой системы:")
print(root.show())