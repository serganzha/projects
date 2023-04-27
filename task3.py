swim = input("Please enter the completion time of the swimming stage in minutes")
cycle = input("Please enter the completion time of the cycling stage in minutes")
run = input("Please enter the completion time of the running stage in minutes")
total_time = int(swim) + int(cycle) + int(run)
print(total_time)
if total_time <= 100:
    print("Congratulations, you have completed the triathlon in qualifying time, and are rewarded with Provincial Colours")
elif (total_time >= 101) and (total_time <= 105):
    print("You have completed the triathlon within 5 minutes of qualifying time, and will be awarded Provincial Half Colours")
elif (total_time >= 106) and (total_time <=110):
    print("You have completed the triathlon within 10 minutes of the qualifying time, and will therefore recieve Provincial Scroll award")
else: print("Unfortunatly you will recieve no award this time")