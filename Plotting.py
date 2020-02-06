import numpy as np
import matplotlib.pyplot as plt
import csv

# creating sublot instances
fig, ax = plt.subplots()
N = 5
width = 0.35
ind = np.arange(N)
# arrays to store the records from the csv file
x = []
y = []
x2 = []
y2 = []
# Open the CSV file and inserting the records in the arrays
with open('Pivot _Table_3.csv', 'r') as csvfile:
    plots = csv.reader(csvfile, delimiter=',')
    plots2 = csv.reader(csvfile, delimiter=',')
    for row in plots:
        if row[0] == 'DEU':
            x.append(int(row[1]))
            y.append(int(row[2]))
        if row[0] == 'FRA':
            x2.append(int(row[1]))
            y2.append(int(row[2]))

# Generating the  graphs
x = np.array(x)
DEU = ax.bar(x - .19, y, label="DEU", width=0.3, align='center', color='r')
x2 = np.array(x2)
FRA = ax.bar(x2 + .19, y2, label="FRA", width=0.3, align='center', color='b')
ax.legend(loc="upper right")
plt.xlabel('Month')
plt.ylabel('Average Conversions')
plt.xticks(x)

ax.set_title('Average conversions per month')


#  Attach a text label above each bar, displaying its height
def autolabel(rects):
    for rect in rects:
        height = rect.get_height()
        ax.annotate('{}'.format(height),
                    xy=(rect.get_x() + rect.get_width() / 2, height),
                    xytext=(0, 3),  # 3 points vertical offset
                    textcoords="offset points",
                    ha='center', va='bottom')


autolabel(DEU)
autolabel(FRA)

# plot the graph
plt.show()
