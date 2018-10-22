import matplotlib.pyplot as plt
from die_visual import get_results
from die import Die

x_values = [x for x in range(1,1001)]
y_values = get_results(dielist=[Die(),], nums=1000)


plt.scatter(x_values, y_values, s=1, c='red', edgecolor='none')
plt.title('try', fontsize=20)
plt.xlabel('times', fontsize=10)
plt.ylabel('value', fontsize=10)

plt.show()

