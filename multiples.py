
# Ask for user inout
userNum = input("Tell me a number.")

# Convert to float.
userNum = float(userNum)

# Do the computation
for multiple in range(2,10):
	answer = userNum * multiple
	print("{} times {} is {}.".format(userNum, multiple, answer))