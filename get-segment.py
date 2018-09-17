from stravalib import Client
import csv
from datetime import timedelta
from matplotlib import pyplot as plt
import numpy as np

client_id = '28201'
my_token = '06e91657960068f2c92e2e02419934f6493fe5b6'

client = Client(access_token=my_token)
mt_coottha = 615163
# segment = client.get_segment(mt_coottha)

# print(segment.distance)
# print(segment.average_grade)
# print(segment.effort_count)

 

my_efforts = client.get_segment_efforts(mt_coottha, athlete_id=1057216, start_date_local='2018-06-01', end_date_local='2019-01-01')



with open("mtcoottha_back.csv", "w", newline="") as file:
    csv_writer = csv.writer(file)
    back = []
    for effort in my_efforts:
        date = str(effort.start_date_local)[:10]  #just get the yy-mm-dd part
        # time = timedelta(seconds=timedelta.total_seconds(effort.elapsed_time))
        time = effort.elapsed_time
        back.append((date, time))
        back.sort(key=lambda date: date[0])
    for attempt in back:    
        csv_writer.writerow(attempt)



fig, ax = plt.subplots()

index = np.arange(len(back))
bar_width = 0.35
opacity = 0.4


x = [x[0] for x in back]
# convert timedelta object to total seconds
y = [timedelta.total_seconds(y[1]) for y in back]


# dist = plt.bar(index, ride_time, bar_width, color="orange", label="Time")
dist = plt.scatter(x, y, c="orange")




ax.set_xlabel("Ride Date")
ax.set_ylabel("Time (seconds)")
ax.set_title("Recent Mt Coot-tha Back Efforts")

ax.set_xticks(index)
ax.set_xticklabels([x for x in x],{'horizontalalignment': 'right'})
ax.invert_yaxis()


for tick in ax.get_xticklabels():
            tick.set_rotation(55)
            
fig.align_labels()
plt.subplots_adjust(bottom=0.35)
# ax.legend(loc="best")
plt.show()

fig.savefig('coottha_back.png')

