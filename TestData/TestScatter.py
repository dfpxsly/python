import matplotlib.pyplot as plt

x_values=list(range(1,5001))
y_values=[x**3 for x in x_values]

plt.scatter(x_values, y_values, s=10, c=y_values, cmap=plt.cm.Blues) 

plt.title("square numbers",fontsize=24)
plt.xlabel("value", fontsize=14)
plt.ylabel("square of value",fontsize=14)

#刻度
plt.axis([0,5000,0,125000000000])
plt.tick_params(axis="both", which='major',labelsize=14)

plt.show()
#plt.savefig('squares_plot.jpg',bbox_inches='tight')