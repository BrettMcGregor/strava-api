from stravalib import Client
import csv

client_id = '28201'
my_token = '06e91657960068f2c92e2e02419934f6493fe5b6'

client = Client(access_token=my_token)

activities = client.get_activities(limit=100)
rides = list(activities)

with open("activities.csv", "w", newline="") as file:
    csv_writer = csv.writer(file)
    for ride in rides:
        date = str(ride.start_date_local)[:10]
        distance = str(ride.distance)[:-5]
        elevation = str(ride.total_elevation_gain).rstrip(" m")
        csv_writer.writerow([date, distance, elevation])

# activity = client.get_activity(1801822008)

# print(activity.distance)
# print(activity.moving_time)
# print(activity.average_speed)
# print(activity.total_elevation_gain)

