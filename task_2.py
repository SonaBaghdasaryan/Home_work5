# Напишите однострочный генератор словаря, который принимает
# на вход три списка одинаковой длины: имена str, ставка int,
# премия str с указанием процентов вида «10.25%». В результате
# получаем словарь с именем в качестве ключа и суммой
# премии в качестве значения. Сумма рассчитывается
# как ставка умноженная на процент премии

names = ['John', 'Peter', 'Sem']
salary = [10000, 20000, 18800]
bonus = ['15%', '12%', '20%']

result = {key: value_1 * value_2 + value_1 for key, value_1, value_2 in zip(names, salary, ((int(x.rstrip(x[-1])) / 100) for x in bonus))}

print(result)