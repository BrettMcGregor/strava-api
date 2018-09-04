import numpy as np
import matplotlib.pyplot as plt
import csv

with open('activities.csv', 'r') as file:
    rides = csv.reader(file)
    ride_date = []
    ride_distance = []
    ride_climb = []
    row_count = 0
    for ride in rides:
        if row_count < 20:
            ride_date.append(ride[0])
            ride_distance.append(int(ride[1]) / 1000)  # convert from metres to km
            ride_climb.append(float(ride[2]))
            row_count += 1
        else:
            break

# Create a figure and a set of subplots/axes (these two objects stored as a tuple. the second element may be an array of axes objects)
fig, ax_list = plt.subplots(1, 3)
index = np.arange(len(ride_date))
bar_width = 0.35

# subplot 0
ax_list[0].bar(index, ride_distance[::-1], color="orange")
ax_list[0].set_xlabel("Ride Date")
ax_list[0].set_ylabel("Distance (km)")
ax_list[0].set_xticks(index)
ax_list[0].set_xticklabels([x for x in ride_date[::-1]],{'horizontalalignment': 'right', 'size': 'x-small'})
for tick in ax_list[0].get_xticklabels():
            tick.set_rotation(55)

# subplot 1
ax_list[1].bar(index, ride_climb[::-1], color="blue")
ax_list[1].set_xlabel("Ride Date")
ax_list[1].set_ylabel("Total Climb Elevation (m)")
ax_list[1].set_xticks(index)
ax_list[1].set_xticklabels([x for x in ride_date[::-1]],{'horizontalalignment': 'right', 'size': 'x-small'})
for tick in ax_list[1].get_xticklabels():
            tick.set_rotation(55)

# subplot 2
ax_list[2].scatter(ride_distance[::-1], ride_climb[::-1], color="red")
ax_list[2].set_xlabel("Ride Distance")
ax_list[2].set_ylabel("Total Climb Elevation (m)")
# ax_list[1].set_xticks(index)
# ax_list[1].set_xticklabels([x for x in ride_date[::-1]],{'horizontalalignment': 'right', 'size': 'x-small'})
# for tick in ax_list[1].get_xticklabels():
#             tick.set_rotation(55)


fig.suptitle("Some of Brett's Strava Ride Stats")
plt.subplots_adjust(wspace=0.4, bottom=0.3)
plt.plot()
plt.show()
