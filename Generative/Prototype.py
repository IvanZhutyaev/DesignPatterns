import copy


class Document:
    def __init__(self, text, author):
        self.text = text
        self.author = author
        self.metadata = {
            'created': '2024-01-01',
            'pages': len(text.split())
        }

    def clone(self):
        # Глубокое копирование, чтобы копировались и вложенные объекты
        return copy.deepcopy(self)

    def __str__(self):
        return f"Документ от {self.author}: {self.text[:30]}..."


# Использование
original = Document("Это очень важный конфиденциальный документ.", "Иван Иванов")
print("Оригинал:", original)
print("Метаданные оригинала:", original.metadata)

# Создаем копию (ксерокс)
copy_doc = original.clone()
copy_doc.author = "Копия Иванова"
copy_doc.metadata['copied'] = '2024-01-02'

print("\nКопия:", copy_doc)
print("Метаданные копии:", copy_doc.metadata)

# Проверяем, что это разные объекты
print(f"\nЭто один объект? {original is copy_doc}")
print(f"Текст одинаковый? {original.text == copy_doc.text}")