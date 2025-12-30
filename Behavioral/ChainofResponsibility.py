class SupportHandler:
    def __init__(self, successor=None):
        self.successor = successor
    
    def handle_request(self, request):
        if self.successor:
            return self.successor.handle_request(request)
        return "Запрос не может быть обработан"

class AutoResponder(SupportHandler):
    def handle_request(self, request):
        if request == "password_reset":
            return "Автоответчик: Ссылка для сброса пароля отправлена"
        return super().handle_request(request)

class FirstLineSupport(SupportHandler):
    def handle_request(self, request):
        if request == "cannot_login":
            return "Оператор 1 линии: Проверьте подключение к интернету"
        elif request == "slow_system":
            return "Оператор 1 линии: Попробуйте очистить кэш"
        return super().handle_request(request)

class TechnicalSupport(SupportHandler):
    def handle_request(self, request):
        if request == "server_error":
            return "Технический специалист: Перезапускаем сервер"
        elif request == "database_issue":
            return "Технический специалист: Восстанавливаем БД"
        return super().handle_request(request)

class Manager(SupportHandler):
    def handle_request(self, request):
        if request == "billing_dispute":
            return "Менеджер: Рассматриваем спор по оплате"
        elif request == "legal_issue":
            return "Менеджер: Подключаем юристов"
        return super().handle_request(request)

# Создаем цепочку
manager = Manager()
tech = TechnicalSupport(manager)
first_line = FirstLineSupport(tech)
auto_responder = AutoResponder(first_line)

# Использование
requests = ["password_reset", "cannot_login", "server_error", "billing_dispute", "unknown_issue"]

for req in requests:
    print(f"\nЗапрос: '{req}'")
    print(f"Ответ: {auto_responder.handle_request(req)}")