# ✔ Выведите в консоль таблицу умножения
# от 2х2 до 9х10 как на школьной тетрадке.
# ✔ Таблицу создайте в виде однострочного
# генератора, где каждый элемент генератора —
# отдельный пример таблицы умножения.
# ✔ Для вывода результата используйте «принт»
# без перехода на новую строку.

def my_table():
    LOW_LIMIT = 2
    UPP_lIMIT = 10
    COL = 4
    print(' ', end='')
    print(*(f'{k:>} x {j:>2} = {k * j:>2}\n\n' if j == UPP_lIMIT and k == i + COL - 1 else \
                f'{k:>} x {j:>2} = {k * j:>2}\n' if k == i + COL - 1 else \
                    f'{k:>} x {j:>2} = {k * j:>2}\t\t' \
            for i in range(LOW_LIMIT, UPP_lIMIT, COL)
            for j in range(LOW_LIMIT, UPP_lIMIT + 1)
            for k in range(i, i + COL)))
my_table()
def product_table() -> iter:
    LOW_LIMIT = 2
    UPP_lIMIT = 10
    COL = 4

    for i in range(LOW_LIMIT, UPP_lIMIT, COL):
        for j in range(LOW_LIMIT, UPP_lIMIT + 1):
            for k in range(i, i + COL):
                if j == UPP_lIMIT and k == i + COL - 1:
                    print(f'{k:>} x {j:>2} = {k * j:>2}\n\n', end='')
                elif k == i + COL - 1:
                    print(f'{k:>} x {j:>2} = {k * j:>2}\n', end='')
                else:
                    print(f'{k:>} x {j:>2} = {k * j:>2}\t\t', end='')

