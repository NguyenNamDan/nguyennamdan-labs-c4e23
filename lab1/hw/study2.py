import matplotlib
matplotlib.use("TkAgg")
from matplotlib import pyplot

machine_count = [18, 4, 2]
machine_name = ["PC", "MAC", "Linux"]
pyplot.pie(machine_count, labels = machine_name, autopct = "%.2f%%", shadow = True, explode = [0, 0.2, 0])
pyplot.title("PC vs MAC vs Linux Usage")
pyplot.axis("equal")
pyplot.show()