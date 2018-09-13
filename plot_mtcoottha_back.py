import numpy as np
import matplotlib.pyplot as plt
import csv
import datetime

with open('mtcoottha_back.csv', 'r') as file:
    efforts = csv.reader(file)
    ride_date = []
    ride_time = []
    for e in efforts:
        ride_date.append(datetime.date(e[0]))
        ride_time.append(datetime.time(e[1]))
       

fig, ax = plt.subplots()

index = np.arange(len(ride_date))
bar_width = 0.35
opacity = 0.4


# dist = plt.bar(index, ride_time, bar_width, color="orange", label="Time")
dist = plt.scatter(ride_date, ride_time, s=9, c="orange", label="effort time")




ax.set_xlabel("Ride Date")
ax.set_ylabel("Time")
ax.set_title("Mt Coot-tha Back Efforts")

ax.set_xticks(index)
ax.set_xticklabels([x for x in ride_date],{'horizontalalignment': 'right'})



for tick in ax.get_xticklabels():
            tick.set_rotation(55)
            
fig.align_labels()
plt.subplots_adjust(bottom=0.3)
ax.legend(loc="best")
plt.show()

fig.savefig('coottha_back.png')
