# importing date class from datetime module.
from datetime import date


# defined a function which shows instructions.
def inst():
    print('''    -----------------------------------------------------------------------
    |                                                                     |
    |                           ENTER ( 1 or 0 )                          |
    |                                                                     |
    | 1. TO CALCULATE THE NUMBER OF DAYS YOU HAVE SURVIVED IN THIS WORLD. |
    |                                                                     |
    | 0. TO EXIT                                                          |
    |                                                                     |
    -----------------------------------------------------------------------''')

    print("")


# defined a function that will take value from the user and execute the process depending on the choice
def exe():
    # user enters " 1 or 0 " from above instruction.
    choose = int(input("    ENTER YOUR CHOICE : "))
    print("")
    print("")
    # if choice of user is 1 then the following program is execution.
    if choose == 1:
        print("    ~~~~~~~~~~~~~~~~~~~~~~~~ FILL THE BELOW DETAILS ~~~~~~~~~~~~~~~~~~~~~~~")
        print("")
        print("")

        # user enters his/her date of birth in the given format which is in the form of string.
        birth_date = input("    ENTER YOUR DATE OF BIRTH IN THE FORMAT \" DD/MM/YYYY \" : ")
        print("")

        # user enters current date in the given format which is in the form of string.
        current_date = input("    ENTER CURRENT DATE IN THE FORMAT \" DD/MM/YYYY \" : ")
        print("")

        # split() method splits the string from "/" into a list of substring.
        list1 = birth_date.split("/")
        list2 = current_date.split("/")

        # values are extracted from the list and are converted into integer and are stored in respective variables.
        day, month, year = int(list1[0]), int(list1[1]), int(list1[2])
        day_c, month_c, year_c = int(list2[0]), int(list2[1]), int(list2[2])

        # the variables are stored in the date class in the format YYYY-MM-DD( year - month - day ).
        a = date(year, month, day)
        b = date(year_c, month_c, day_c)

        # two dates are subtracted to get the number of days between them considering leap and non-leap years.
        n = b - a
        
        # as n contains timedelta object .i.e number of days, hours, minutes, seconds.
        # as we need only the number of days between the given dates.
        # we use n.days 
        print('''    ---------------------------------------------------------------------
    |                                                                   |
--->   THE NUMBER OF DAYS YOU HAVE SURVIVED IN THIS WORLD :-''', n.days, '''DAYS   <---  
    |                                                                   |
    ---------------------------------------------------------------------''')
        print("")
        print("")
        print("")
        print("    ***********************************************************************")
        print("")
        print("")
        # asking the user whether he/she wants to run the program again. 
        print("    CALCULATE AGAIN ?")
        print("")
        again = input("    ENTER \"YES\" OR \"NO\" : ")
        print("")
        if again == "YES" or again == "yes":
            # functions are called within a function (recursion).
            inst()
            exe()

# function is called.


inst()
exe()
