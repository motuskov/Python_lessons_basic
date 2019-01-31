import re


# Задание-1: Решите задачу (дублированную ниже):

# Дана ведомость расчета заработной платы (файл "data/workers").
# Рассчитайте зарплату всех работников, зная что они получат полный оклад,
# если отработают норму часов. Если же они отработали меньше нормы,
# то их ЗП уменьшается пропорционально, а за заждый час переработки они получают
# удвоенную ЗП, пропорциональную норме.
# Кол-во часов, которые были отработаны, указаны в файле "data/hours_of"

# С использованием классов.
# Реализуйте классы сотрудников так, чтобы на вход функции-конструктора
# каждый работник получал строку из файла


# Решение задания-1
class Worker:
    def __init__(self, worker_data):
        parsed_data = re.match(r"(\w+)\s+(\w+)\s+(\d+)\s+(\w+)\s+(\d+)", worker_data)
        self.first_name = parsed_data.group(1)
        self.last_name = parsed_data.group(2)
        self.salary = int(parsed_data.group(3))
        self.job = parsed_data.group(4)
        self.standard_hours = int(parsed_data.group(5))

    def get_full_name(self):
        return f"{self.first_name} {self.last_name}"

    def calc_salary(self, hours):
        return self.salary / self.standard_hours * hours if hours <= self.standard_hours else \
            self.salary + self.salary / self.standard_hours * (hours - self.standard_hours) * 2


workers = []
with open("data\workers", encoding="UTF-8") as f:
    for line in f:
        if re.match(r"\w+\s+\w+\s+\d+\s+\w+\s+\d+", line):
            workers.append(Worker(line))

with open("data\hours_of", encoding="UTF-8") as f:
    for line in f:
        hours_data = re.match(r"(\w+)\s+(\w+)\s+(\d+)", line)
        if hours_data:
            for worker in workers:
                if worker.get_full_name() == f"{hours_data.group(1)} {hours_data.group(2)}":
                    print(f"{worker.get_full_name()} - {worker.calc_salary(int(hours_data.group(3))):.2f}")

