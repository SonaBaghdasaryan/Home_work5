# Создайте функцию генератор чисел Фибоначчи

def fib(n):
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a + b
        yield a

print(*fib(10))
