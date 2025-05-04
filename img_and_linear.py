import matplotlib.pyplot as plt

# 1. Загружаем изображение
image = plt.imread("./images/cat.jpg")  # Укажите путь к файлу

# 2. Создаем фигуру и оси
fig, ax = plt.subplots(figsize=(10, 6))

# 3. Отображаем изображение
ax.imshow(image, extent=[19, 24, 0, 10], aspect='auto')  # extent задает границы [xmin, xmax, ymin, ymax]

# 4. Создаем данные для графика
x = [19, 20, 21, 22, 23, 24]
y = [2, 4, 3, 7, 8, 10]

# 5. Рисуем график поверх изображения
ax.plot(x, y, '--', color='red', linewidth=3, label='Line')
ax.set_title("График поверх изображения")
ax.set_xlabel("Время")
ax.set_ylabel("Усталость")
ax.legend()

plt.show()