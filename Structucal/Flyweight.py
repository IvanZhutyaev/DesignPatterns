class FontStyle:
    """Легковес - разделяемое состояние"""

    def __init__(self, font_family, size, color):
        self.font_family = font_family
        self.size = size
        self.color = color

    def __str__(self):
        return f"{self.font_family} {self.size}pt {self.color}"


class FontFactory:
    """Фабрика легковесов"""
    _styles = {}

    @staticmethod
    def get_style(font_family, size, color):
        key = (font_family, size, color)
        if key not in FontFactory._styles:
            FontFactory._styles[key] = FontStyle(font_family, size, color)
            print(f"Создан новый стиль: {key}")
        return FontFactory._styles[key]


class Character:
    """Символ с уникальными и разделяемыми состояниями"""

    def __init__(self, char, x, y, style):
        self.char = char  # уникальное состояние
        self.x = x  # уникальное состояние
        self.y = y  # уникальное состояние
        self.style = style  # разделяемое состояние

    def render(self):
        return f"'{self.char}' в позиции ({self.x},{self.y}) стиль: {self.style}"


# Использование
factory = FontFactory

# Создаем стили (разделяемые объекты)
style1 = factory.get_style("Arial", 12, "black")
style2 = factory.get_style("Times New Roman", 14, "red")
style3 = factory.get_style("Arial", 12, "black")  # Не создастся новый, возьмет существующий

# Создаем символы
text = [
    Character('H', 0, 0, style1),
    Character('e', 10, 0, style1),
    Character('l', 20, 0, style2),  # Другой стиль
    Character('l', 30, 0, style2),
    Character('o', 40, 0, style1),
]

for char in text:
    print(char.render())

print(f"\nВсего создано стилей: {len(FontFactory._styles)}")