#Given a list of grades.  Process and nalyze these grades.
#Tastk 1: Given the list of grades sort them in descending order and prit the sorted list.
#********************************Task 1**************************************************
#                              We do what we're told                                    *
#****************************************************************************************
###############approach 1 (sorted in new list then printed)

# Initialze the list with supplied scores
grades = [85, 90, 78, 88, 76, 95, 89, 80, 72, 93]
#use sorted function in a new list
sorted_grades =  sorted(grades, reverse=True)
print(f"Sorted grades in decending order (using sorted()), {sorted_grades}")

###########################approach 2 (sorted and printed in place)
print(f"sorted grades using in-place sort: {sorted(grades, reverse=True)}")

#*****************************************************************************************
#Take the same list of grades and calculate the average, then print the average.
# I mean we could just not tell anybody, keep it a secret.  Why do they need to know?
# It can be just between you and me.  I won't tell if you won't
#******************************************************************************************

#**********************************Task 2*************************************************
#                         This space for rent                                            *
#*****************************************************************************************

#As a precaution we will always work on a copy of the list to make sure we don't mess the original data up.

grades_copy = grades
grades_average = sum(grades_copy) / len(grades_copy)
print (f"The average of the all the grades is: {grades_average}")

#***************************Task 2.5*******************************************************
#              Because it's no fun if we don't try something weird                        *
#******************************************************************************************

#now lets show off a little..jsut a little I promise
# Were gonna do this with a) a function that b) filters out bad entries on the list and
# b) prevents calculation on an empty list, and goes as gracefully as I can do with
# no sleep and needing to feed the dog before she starts nibbling on me

# We start, as all ambitious things do, with a function.

def calculate_average(digits):
    #we make a list to store only numeric values from the list
    numbers_only =[]

    #we make sure we avoid any non numerical items in the list
    for digit in digits:
        try:
            numbers_only.append(float(digit)) # Used a float just bcause grades can be floats and I didn't want to discriminate
        except ValueError:
            print(f"Skippig non-numberic value: {digit}")
    #If list is blank retun a 0 so we don't cause a hemmorage in the function
    if not numbers_only:
        return 0
    return sum(numbers_only)/ len(numbers_only)

    
#make a result with a bad test case first to make sure the funciton works
grades_bad= [85, 90, 78, "A", 88, "B", 76, 95, 89, 80, "C", 72, 93]
grades_good = [85, 90, 78, 88, 76, 95, 89, 80, 72, 93]
list_average= calculate_average(grades_bad)
print("*************************bad data test*********************")
print (f"Average by the function is: {list_average}")
print("************************************************************")
print("**************************good data test*********************")
list_average_good = calculate_average(grades_good)
print(f"Average by the function is {list_average_good}")