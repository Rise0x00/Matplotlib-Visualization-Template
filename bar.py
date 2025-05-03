import matplotlib.pyplot as plt

values = [15, 30, 45, 10]
categories = ['A', 'B', 'C', 'D']

plt.bar(categories, values, color='green')
plt.title('Столбчатая диаграмма')
plt.xlabel('Категории')
plt.ylabel('Значения')
plt.show()