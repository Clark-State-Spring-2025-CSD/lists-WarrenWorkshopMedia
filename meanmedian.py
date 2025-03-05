#prompt the user to enter 5 numbers. Store them in a list.
#Display the list as entered, small to large, and large to small
#Calculate and display the mean and median
#This is a guided practice. You can follow the video or your instructor will go
#over this in class


TheList = []
#TheList = [0,0,0,0,0]

for i in range(5):
    TheList.append(int(input(f"Number {i+1}: ")))
    #TheList[i] = int(input(f"Numer{i+1}: "))

print("Original order: " + str(TheList))

TheList.sort()

print(f"small to large: {TheList}")

TheList.sort(reverse=True)

print(f"large to small: {TheList}")

median = TheList[2]

sum = 0

for i in range(5):
    sum += TheList[i]

#for value in TheList:
    #sum += value

average = sum / 5

print(f"the medium is {median} and the mean is {average}")