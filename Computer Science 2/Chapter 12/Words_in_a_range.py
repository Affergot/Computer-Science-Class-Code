import time

while True:
    try:
        filename = input("Enter a filename: ")
        openfile = open("Computer Science 2/Chapter 12/" + filename + ".txt", "r")
        time.sleep(0.5)
        break
    except FileNotFoundError:
        time.sleep(0.5)
        print("File not found")

upperBoundery = (input("Enter the upper boundery: ")).lower()
lowerBoundery = (input("Enter the lower boundery: ")).lower()

tempList = []
tempList.append(upperBoundery)
tempList.append(lowerBoundery)
tempList.sort()

inRange = []
outofRange = []

for word in openfile.readlines():
    word = word.strip()
    tempList.append(word)
    tempList.sort()
    if word == tempList[1]:
        inRange.append(word)
    else:
        outofRange.append(word)
    tempList.remove(word)

print(" ")
print("The words IN the range are: ")
for word in inRange:
    print(word)
print(" ")
print("The words OUT of the range are: ")
for word in outofRange:
    print(word)