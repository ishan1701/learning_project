from abc import ABC, abstractmethod
from enum import Enum


class Employee(ABC):
    total_employee: int = 0

    def __init__(self, name: str, salary: float, manager: 'Manager'):
        assert salary >= 0, 'salary must be positive'
        self.name = name
        self.__salary = salary,
        self._manager = manager
        # Employee.total_employee += 1
        print(f'total employee: {self.total_employee}')


class Accountant(Employee):
    acc_count: int = 0

    def __init__(self, name: str, salary: float, manager: 'Manager', is_passed_accounts: bool):
        super().__init__(name=name, salary=salary, manager=manager)
        self.is_passed_accounts = is_passed_accounts
        self.acc_count += 1

    def calculate_taxes(self):
        if self.is_passed_accounts:
            print('Calculating taxes')
        else:
            print('Calculating taxes not possible')


class Salesman(Employee):
    salesman_count: int = 0

    def __init__(self, name: str, salary: float, manager: 'Manager', is_passed_salesmanship: bool):
        super().__init__(name=name, salary=salary, manager=manager)
        self.is_passed_salesmanship = is_passed_salesmanship
        Salesman.salesman_count += 1



class Manager(Employee, ABC):
    managers_count: int = 0

    def __init__(self, name: str, salary: float, manager: 'Manager', reporting_employee: list[Employee]):
        Employee.__init__(self, name=name, salary=salary, manager=manager)
        self.reporting_employee = reporting_employee
        Manager.managers_count += 1
        print(f'Manager {self.managers_count} reported employees')

    @abstractmethod
    def add_employee(self, employee: Employee):
        pass

    @abstractmethod
    def remove_employee(self, employee: Employee):
        pass


class SalesManager(Manager, Salesman):
    salesman_count: int = 0

    def __init__(self, name, salary: float, manager: 'Manager', reporting_employee: list[Employee],
                 is_passed_salesmanship: bool, is_masters: bool):
        print(self.salesman_count)
        Manager.__init__(self, name=name, salary=salary, manager=manager, reporting_employee=reporting_employee)
        Salesman.__init__(self, name=name, salary=salary, manager=manager,
                          is_passed_salesmanship=is_passed_salesmanship)
        self.is_masters = is_masters
        SalesManager.salesman_count += 1
        print(self.salesman_count)

    def add_employee(self, employee: Employee):
        self.reporting_employee.append(employee)

    def remove_employee(self, employee: Employee):
        self.reporting_employee.remove(employee)


class EmployeeType(Enum):
    salesman = Salesman
    accountant = Accountant
    sales_manager = SalesManager


class EmployeeFactory:
    @staticmethod
    def create_employee(emp_type: str, **kwargs) -> Employee:
        if emp_type == "salesman":
            return Salesman(
                name=kwargs["name"],
                salary=kwargs["salary"],
                manager=kwargs.get("manager"),
                is_passed_salesmanship=kwargs["is_passed_salesmanship"]
            )
        elif emp_type == "accountant":
            return Accountant(
                name=kwargs["name"],
                salary=kwargs["salary"],
                manager=kwargs.get("manager"),
                is_passed_accounts=kwargs["is_passed_accounts"]
            )
        elif emp_type == "sales_manager":
            return SalesManager(
                name=kwargs["name"],
                salary=kwargs["salary"],
                manager=kwargs.get("manager"),
                reporting_employee=kwargs.get("reporting_employee", []),
                is_passed_salesmanship=kwargs["is_passed_salesmanship"],
                is_masters=kwargs["is_masters"]
            )
        else:
            raise ValueError('Invalid employee type')


if __name__ == '__main__':
    s_m = EmployeeFactory.create_employee("sales_manager", name="Charlie", salary=80000, manager=None,
                                                    reporting_employee=[], is_passed_salesmanship=True, is_masters=True)

    s_m1 = EmployeeFactory.create_employee("sales_manager", name="Charlie", salary=80000, manager=None,
                                          reporting_employee=[], is_passed_salesmanship=True, is_masters=True)

    s_mman = EmployeeFactory.create_employee("salesman", name="Charlie", salary=80000, manager=None,
                                           reporting_employee=[], is_passed_salesmanship=True, is_masters=True)


