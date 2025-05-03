import matplotlib.pyplot as plt

x = [5, 7, 8, 2, 4, 6]
y = [3, 9, 1, 6, 2, 7]

plt.scatter(x, y, s=100, c='green', alpha=0.75, edgecolors='black')
# s - размер точек
# c - цвет точек
# alpha - прозрачность точек
# edgecolors - цвет границы точек
plt.title('Точечный график')
plt.xlabel('Ось X')
plt.ylabel('Ось Y')
plt.grid(True)
plt.show()