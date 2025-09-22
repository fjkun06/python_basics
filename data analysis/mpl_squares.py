import matplotlib.pyplot as plt

input_values = range(1, 1001)
squares = [value**2 for value in input_values]

plt.style.use("seaborn-v0_8-darkgrid")
fig, ax = plt.subplots()

# ax.plot(input_values, squares, linewidth=.1)
ax.scatter(input_values, squares, c=squares, cmap=plt.cm.Blues, s=10)

# Set chart title and axis labels
ax.set_title("Square Numbers", fontsize=24)
ax.set_xlabel("Value", fontsize=14)
ax.set_ylabel("Square of Value", fontsize=14)
ax.axis([0, 1100, 0, 1_100_000])
ax.ticklabel_format(style='scientific')

# Set size of tick labels
ax.tick_params(labelsize=14)
print(plt.style.available)
plt.show()
