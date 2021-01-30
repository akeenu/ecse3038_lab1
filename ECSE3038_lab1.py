#Question1
def hello():
	return ('ECSE3030 - Engineering IoT Systems')

print(hello())

#Question2
def validatePassword(password):
	if len(password) >= 8 and password.isalnum():
		return True
	else:
		return False

print(validatePassword("abc123"))
print(validatePassword("password"))
print(validatePassword("GreetingsFellowKids"))


#Question3and
def sumUpToN(number):
    sum = 0

    if number > 1:
        for i in range(1, number+1):
            sum += i
    else:
        sum = -1

    return sum 

print(sumUpToN(14))