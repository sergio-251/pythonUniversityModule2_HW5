# Функции в Python. Функция с параметром
def get_matrix(n, m, value):
    return [[value for j in range(m)] for i in range(n)]

print(get_matrix(2,2,10))