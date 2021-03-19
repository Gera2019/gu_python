class Worker:
    def __init__(self, name, surname, position, wage, bonus):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = {'wage': wage, 'bonus': bonus}


class Position(Worker):
    def get_full_name(self):
        return self.name, self.surname

    def get_total_income(self):
        return self._income['wage'] + self._income['bonus']


worker1 = Position('Andrew', 'Tanenbaum', 'professor', 5000, 2500)
print(worker1.get_total_income())
print(worker1.position)
print(worker1.name)

worker2 = Position('Mark', 'Lutz', 'developer', 3000, 3000)
print(worker2.get_full_name(), worker2.get_total_income())
print(worker2.position)