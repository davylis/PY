from copy import deecopy

weekdays_1 = ["Branch 1", ["Monday", "Wednesday", "Friday"]]

weekdays_2 = deecopy(weekdays_1)
weekdays_2[0] = "Branch 2" 
weekdays_2[1].insert(1, "Tuesday")

print(*weekdays_1)
print(*weekdays_2)