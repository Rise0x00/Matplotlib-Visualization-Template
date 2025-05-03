import matplotlib.pyplot as plt

y1 = [10, 15, 20, 25]
y2 = [5, 10, 15, 20] # Прибавляется к y1
categories = ['A', 'B', 'C', 'D']

plt.bar(categories, y1, label='Группа 1')
plt.bar(categories, y2, bottom=y1, label='Группа 2') # Bottom=y1 - под 1 группой
plt.legend()
plt.title("Сложная столбчатая диаграмма")
plt.show()