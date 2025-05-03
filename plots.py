import matplotlib.pyplot as plt

# Данные для столбчатой диаграммы
values = [15, 30, 45, 10]
categories = ['A', 'B', 'C', 'D']

# Построение столбчатой диаграммы
plt.bar(categories, values, color='green', alpha=0.5, label='Столбцы')

# Данные для линейного графика
x_line = [0, 1, 2, 3]
y_line = [10, 20, 15, 5]

# Построение линейного графика поверх столбчатой диаграммы
plt.plot(x_line, y_line, marker='o', linestyle='--', color='red', label='Линия')

plt.title('Столбчатая диаграмма с линейным графиком')
plt.xlabel('Категории')
plt.ylabel('Значения')
plt.legend()
plt.show()