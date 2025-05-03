import matplotlib.pyplot as plt

data = [23, 45, 56, 78, 34, 12, 45, 67, 89, 90, 23, 45, 67]

# Строит график частоты встречаемости чисел в списке
plt.hist(data, bins=10, color='yellow', edgecolor='red')
plt.title('Гистограмма')
plt.xlabel('Интервалы')
plt.ylabel('Частота')
plt.show()