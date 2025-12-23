class BankAccount:
    """Реальный объект - банковский счет"""

    def __init__(self, balance):
        self.balance = balance

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            return f"Снято {amount}. Остаток: {self.balance}"
        else:
            return "Недостаточно средств"


class BankCard:
    """Прокси - банковская карта"""

    def __init__(self, account, pin_code):
        self.account = account
        self.pin_code = pin_code
        self.failed_attempts = 0

    def withdraw(self, amount, pin):
        # Дополнительная логика контроля доступа
        if pin != self.pin_code:
            self.failed_attempts += 1
            return f"Неверный PIN. Попытка {self.failed_attempts}"

        if self.failed_attempts >= 3:
            return "Карта заблокирована!"

        # Логирование
        print(f"Лог: Попытка снять {amount}")

        # Проверка лимита
        if amount > 50000:
            return "Превышен дневной лимит"

        # Делегирование вызова реальному объекту
        return self.account.withdraw(amount)


# Использование
account = BankAccount(100000)
card = BankCard(account, "1234")

print(card.withdraw(10000, "1234"))  # Успешно
print(card.withdraw(60000, "1234"))  # Лимит превышен
print(card.withdraw(10000, "0000"))  # Неверный PIN
print(card.withdraw(10000, "0000"))  # Еще раз неверный PIN
print(card.withdraw(10000, "0000"))  # Еще раз неверный PIN
