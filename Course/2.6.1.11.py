hour = int(input("Starting time (hours): "))
mins = int(input("Starting time (minutes): "))
dura = int(input("Event duration (minutes): "))

# Write your code here.
#initialize
hour_in_mins = hour * 60
time_in_mins = hour_in_mins + mins
end_time_mins = time_in_mins + dura

#next
end_hour = end_time_mins // 60 % 24
end_mins = end_time_mins % 60
end_time = str(end_hour) + ":" + str(end_mins)
print(end_time)