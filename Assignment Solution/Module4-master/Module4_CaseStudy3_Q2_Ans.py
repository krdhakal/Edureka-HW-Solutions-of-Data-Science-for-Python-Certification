import matplotlib.pyplot as plt, numpy
x_axis=[]
i=0
myfile=open('c:/temp/CityTemps.csv', 'r')
for data in myfile:
    data = data.rstrip('\n')
    i += 1
    if i == 1:  # 1st Line is header skip it.
        continue

    x_axis.append(data.split(',')[2])

plt.hist(x_axis,2014)
plt.hist(x_axis,2015)
plt.show()
