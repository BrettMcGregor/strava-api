from stravalib import Client
import csv
from datetime import timedelta

client_id = '28201'
my_token = '06e91657960068f2c92e2e02419934f6493fe5b6'

client = Client(access_token=my_token)

segment = client.get_segment(615163)

print(segment.distance)
print(segment.average_grade)
print(segment.effort_count)

my_efforts = client.get_segment_efforts(615163, athlete_id=1057216)

with open("mtcoottha_back.csv", "w", newline="") as file:
    csv_writer = csv.writer(file)
    back = []
    for effort in my_efforts:
        date = str(effort.start_date_local) #[:10]
        time = timedelta(seconds=timedelta.total_seconds(effort.elapsed_time))        
        csv_writer.writerow([date,time])


