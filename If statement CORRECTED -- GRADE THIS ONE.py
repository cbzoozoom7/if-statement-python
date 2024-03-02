#7
one = raw_input("Do you want to continue?")
if one == "Y" or one == "Yes" or one == "OK" or one == "Sure" or one == "Why not":
    print "Ok"
elif one == "N" or one == "No":
    print "Teminating...(but not really)"
else:
    print "Bad Input."

#6
hours = input("How many hours did you work this week? ")
print ""
wage = input("What is your normal hourly wage? ")
print ""
if hours > 40:
    overtimeHours = hours-40
    overtimePay = overtimeHours*(wage*1.5)
    print "You worked overtime and should be paid $", overtimePay, "for a total of $", overtimePay+((hours-overtimeHours)*wage), "."
elif hours < 40:
    print 'You worked "undertime" and should be paid $', hours*wage, "."
else:
    print "You worked a full 40 hour week and should be paid $", hours*wage, "."

#5
one = raw_input("Enter a letter grade. ")
print ""
if one == "A" or one == "a":
    print "Numeric value is 4."
elif one == "B" or one == "b":
    print "Numeric value is 3."
elif one == "C" or one == "c":
    print "Numeric value is 2."
elif one == "D" or one == "d":
    print "Numeric value is 1."
elif one == "F" or one == "f":
    print "Numeric value is 0."
else:
    print "Invalid input."

#4
one = input("Enter a year. ")
print ""
if one%4 == 0:
    if one%100 == 0:
        if one%400 == 0:
            print "Yep, this is a leap year."
        else:
            print "This one's not leap year. Sorry, one less day for you"
    else:
        print "Yay, this one's a leap!"
else:
    print "Just a year like any other."

#3
one = input("What is the number? ")
print ""
if one%2 == 0:
    print "The number is even."
else:
    print "The number is odd."

#2
username = "thisIsTheCorrectUsername"
password = "thisIsNotASecureMethodOfStoringPasswords"
inputUsername = raw_input("What is your Username? ")
print ""
if username == inputUsername:
    inputPassword = raw_input("What is your password? ")
    print ""
    if password == inputPassword:
        print "Signing in (but not really)..."
else:
    print "User not found."

#1
one = input("What is the number? ")
print ""
if one > 0 or one < 0:
    print "Your number is not 0"
else:
    print "Your number is 0"