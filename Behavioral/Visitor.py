from abc import ABC, abstractmethod

# Элементы (отделы компании)
class Department(ABC):
    @abstractmethod
    def accept(self, visitor):
        pass

class AccountingDepartment(Department):
    def accept(self, visitor):
        return visitor.visit_accounting(self)

class WarehouseDepartment(Department):
    def accept(self, visitor):
        return visitor.visit_warehouse(self)

class ITDepartment(Department):
    def accept(self, visitor):
        return visitor.visit_it(self)

# Посетитель
class InsuranceAgent:
    def visit_accounting(self, department):
        return "Оценка финансовых рисков бухгалтерии"
    
    def visit_warehouse(self, department):
        return "Оценка рисков пожарной безопасности склада"
    
    def visit_it(self, department):
        return "Оценка киберрисков IT-отдела"

# Структура компании
class Company:
    def __init__(self):
        self.departments = [
            AccountingDepartment(),
            WarehouseDepartment(),
            ITDepartment()
        ]
    
    def accept_agent(self, agent):
        results = []
        for dept in self.departments:
            results.append(dept.accept(agent))
        return results

# Использование
company = Company()
agent = InsuranceAgent()

print("Страховой агент посещает компанию:")
for result in company.accept_agent(agent):
    print(f"  - {result}")