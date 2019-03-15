import datetime
import random
import matplotlib.pyplot as plt
print(datetime.datetime.now())
# make up some data
x = [datetime.datetime.now()]
y = [i+random.gauss(0,1) for i,_ in enumerate(x)]


# plot
plt.plot(x,y)
# beautify the x-labels
plt.gcf().autofmt_xdate()
plt.show()
