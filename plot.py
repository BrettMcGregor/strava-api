import numpy as np
import matplotlib.pyplot as plt
import csv

with open('activities.csv', 'r') as file:
    data = csv.reader(file) 
    ride_date = []
    ride_distance = []
    ride_climb = []
    for d in data:
        ride_date.append(d[0])
        ride_distance.append(int(d[1]))
        ride_climb.append(float(d[2]))


fig, ax = plt.subplots()

index = np.arange(len(ride_date))
bar_width = 0.35
opacity = 0.4


dist = plt.bar(index, ride_distance, bar_width, color="orange", label="Distance")
elev = plt.bar(index + bar_width, ride_climb, bar_width, color="blue", label="Climb")

ax.set_xlabel("Ride Date")
ax.set_ylabel("metres")
ax.set_title("Strava Ride Stats")

ax.set_xticks(index + bar_width / 2)
ax.set_xticklabels([x for x in ride_date],{'horizontalalignment': 'right'})



for tick in ax.get_xticklabels():
            tick.set_rotation(55)
            
fig.align_labels()
plt.subplots_adjust(bottom=0.3)
ax.legend(loc="best")
plt.show()

fig.savefig('test.png')