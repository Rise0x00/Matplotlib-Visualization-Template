import matplotlib.pyplot as plt

labels = ['Python', 'Java', 'C++', 'JavaScript']
colors = ['gold', 'lightcoral', 'lightskyblue', 'lightgreen']
sizes = [45, 30, 10, 25]

plt.pie(sizes, labels=labels, colors=colors, shadow=True, startangle=90)
# startangle - угол начала графика
plt.title('Распределение языков программирования')
plt.show()