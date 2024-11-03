#We have two lists.  1) Sutdents who have submitted assginments, and those who last attended class
# We must determine if Alice submitted her assignment *and* last attended class.
#********************************Task 1**************************************************
#                      Welcome my son.  Welcome to the machine.                         *
#****************************************************************************************
###############approach 1 (Assignment as written)****************************************

#We get our two lists

submitted = ["Alice", "Bob", "Charlie", "David"]
attended = ["Charlie", "Eve", "Alice", "Frank"]
disiplinary_list =[] #This is for later.

#We look for alice in both

if "Alice" in submitted and "Alice" in attended:
    print ("Alice submitted the assignment and attended class")
else:
    print ("Alice did not sumbit her work or did not attend class")

#********************************************version 2******************************************************************************
#Now we make it more useful.  Our goal here is to take student name as imput, save it as variable (aftger confirming it's
#valid).  And compare it to the two lists and see *where* tha specific student exists.  If we feel ambitious we may conver the name 
#to a standard format to keep everything valid and working.

# 1) using the same lists as above we get our input for the student to search for:

#***********************************************************************************************************************************
student_name = input("Please enter a student name to searchf for: ").strip().title()  #This makes sure the name matches list format

#Check which lists the entered student occupies.

if student_name in submitted and student_name in attended:
    print(f"{student_name} submitted the assignment and attended class.")
elif student_name in submitted:
    print(f"{student_name} submitted the assignment but did not attend class")
elif student_name in attended:
    print(f"{student_name} attended class but did not submit the assignment.")
else:
    print(f"{student_name} neither submitted the assignment nor attended class")
    print("*********************************************************************")
    #***********************************Now we follow up because there will be questions*********************************************
    print("Would you like to add the student to disciplinary list.") #make note of the naugty student.
    add_to_list =input("Answer y or n").strip().lower() #make answer consistently formatted
    if add_to_list == "y":
        student_name=disiplinary_list.append(student_name) #there will be questions
    elif add_to_list =='n':
        print("Ok, but we will add your name to the invesitgation list for failing to add student to disciplinary list.")#Thought you could get away
    else:
        print("Im sorry, your answer was incorrect.  Adding your name to disciplinary list for failing to answer correctly")
        #please assume the staff review position
