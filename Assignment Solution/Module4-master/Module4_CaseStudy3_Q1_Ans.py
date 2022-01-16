import matplotlib.pyplot as plt
import numpy as np

x_axis_year=[]
y_axis_hurricanes=[]
i=0
hurricane_file=open('c:/temp/Hurricanes.csv', 'r')
for data in hurricane_file:
    data = data.rstrip('\n')
    i += 1
    if i == 1:  # 1st Line is header skip it.
        continue

    x_axis_year.append(data.split(',')[0])
    y_axis_hurricanes.append(data.split(',')[1])

# print x_axis_year
# print y_axis_hurricanes

# plt.plot(x_axis_year,y_axis_hurricanes)
plt.ylabel('Year')
plt.xlabel('The number of hurricanes')
# plt.show()

plt.bar(x_axis_year,y_axis_hurricanes)
plt.show()
