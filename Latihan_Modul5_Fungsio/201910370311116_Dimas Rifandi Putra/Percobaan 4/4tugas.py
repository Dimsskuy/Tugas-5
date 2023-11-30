import matplotlib.pyplot as plt

x = [1, 2, 3, 4, 5]
y = [3, 7, 2, 8, 5]
colors = ['red', 'blue', 'green', 'yellow', 'black']

plt.title('Percobaan 4', loc='center', pad=20, fontsize='30', color='red')
plt.xlabel('Titik titik X', fontsize=12)
plt.ylabel('Titik titik Y', fontsize=12)
plt.scatter(x, y, color=colors)  
plt.show()
