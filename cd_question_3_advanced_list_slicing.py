# we have a list of tempreatures for one month.  We must extract specific data form it.
#We'll play around a litte, but won't do much.

#We take our list
temperatures = [72, 75, 78, 79, 80, 81, 82, 83, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100, 101, 102, 103, 104, 105, 106]

#now we do some voodoo that we do because the voodoo that we do must be done.  All hail the Omnisiah.

#Extract temps for seoncd week (index 7-13).  Why?  Because we can.

second_week= temperatures[7:14]
print ("Tempreatures for the second week were: ", second_week)

#Extract all temps above 100
wicked_hot = [temp for temp in temperatures if temp > 100]
print("All temps over 100: ", wicked_hot)

#Extract all days above 100 but pair it with its index value adjusted to correspond to it's day value (index + 1)

wicked_hot_with_days =[(index + 1, temp) for index, temp in enumerate(temperatures) if temp > 100]
print ("Days with temp above 100: ")
for day, temp in wicked_hot_with_days:
    print(f"Day {day}: {temp}°F")

#show highest temp
hottest_day = max(temperatures)
print("Higest temperature: ", hottest_day)

#show lowest temp
coldest_day = min(temperatures)
print("Lowest Temperature: ", coldest_day)

#show average for month
average_temp = sum(temperatures) / len(temperatures)
print(f"Average temperature: {average_temp:.2f}") #caps the result to 2 decimil places just because we want to be neat.

