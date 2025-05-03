import matplotlib.pyplot as plt

x = [1, 2, 3, 4, 5]
y = [2, 4, 1, 5, 3]

plt.plot(x, y, marker='o', linestyle='--', color='red', label='Линия')
plt.title('Пример линейного графика')  # Заголовок
plt.xlabel('Ось X')  # Подпись оси X
plt.ylabel('Ось Y')  # Подпись оси Y
plt.grid(True)  # Сетка
plt.legend()  # Легенда
plt.show()