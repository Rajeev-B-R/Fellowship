#accept first name and reverse
firstName = input(str("Enter your first name : "))
firstName = firstName[::-1]

#accept last name and reverse
lastName = input(str("Enter your last name : "))
lastName = lastName[::-1]

print(lastName + " " + firstName)
