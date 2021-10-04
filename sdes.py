import numpy as np

IP = [2, 6, 3, 1, 4, 8, 5 , 7]
IPinverse = [4, 1, 3, 5, 7, 2, 8, 6]
P10 = [3, 5, 2, 7, 4, 10, 1, 9, 8, 6]
P8 = [6, 3, 7, 4, 8, 5, 10, 9]
E_P = [4, 1, 2, 3, 2, 3, 4, 1]
P4 = [2, 4, 3, 1]

# a dictionary to map the permutation name to the permutation list
permutations = {
    "P10" : P10,
    "P8" : P8,
    "P4" : P4,
    "E_P" : E_P,
    "IP" : IP,
    "IP-1" : IPinverse
}

#convert a decimal number into binary number and print it
def decimalToBinaryRecurse(n, binArray):

    if(n > 1):
        # divide with integral result
        # (discard remainder)
        decimalToBinaryRecurse(n//2, binArray)

    binArray.append(n%2)
    # print(n%2, end=' ')

#this is the helper function for the recurse function
#takes decimal base number as input
#returns a list containing the equivalent binary number
def decimalToBinary(n):
    binArray = [] #declaring the list here to pass it to the recurse function
    decimalToBinaryRecurse(n, binArray) #call the actual conversion function
    return binArray

#split input string of binary numbers into a list of binary numbers
#takes in a ' ' separated string
#returns a list
def stringToList(input):
    theList = input.split() #split based on space
    return theList

#takes in a list of string and a permutation name and applies it on
#the list of string and returns the result as a list
def applyP(charList, permutationName):
    result = []
    for index in permutations[permutationName]:
        result.append(charList[index - 1])
    return result

def leftShift(arr):
    item = arr.pop(0)
    arr.append(item)
    return arr

# print(stringToList("A B C D E F G H I J"))
# print(applyP(stringToList("A B C D E F G H I J"), "IP"))
binary = [1, 1, 0, 0, 1, 1, 0, 0]
print("Original T: ")
for i in range(len(binary)):
    print(f'{binary[i]}', end=" ")

print()

binary = applyP(binary, "IP")
print("IP on Text: ")
for i in range(len(binary)):
    print(f'{binary[i]}', end=" ")

print()

rightEP = applyP(binary[-4:], "E_P")
print("RightEP: ")
for i in range(len(rightEP)):
    print(f'{rightEP[i]}', end=" ")

print()
print()
print()

inputKey = [1,1,1,0,0, 1,1,0,0,0]
temp = applyP(inputKey, "P10")
print("on P10: ")
for i in range(len(temp)):
    print(f'{temp[i]}', end=" ")
print()
temp = leftShift(temp)
print("on LS: ")
for i in range(len(temp)):
    print(f'{temp[i]}', end=" ")
print()
temp = applyP(temp, "P8")
print("on P8: ")
for i in range(len(temp)):
    print(f'{temp[i]}', end=" ")

print()
K1 = applyP(leftShift(applyP(inputKey, "P10")), "P8")
print("K1: ")
for i in range(len(K1)):
    print(f'{K1[i]}', end=" ")

print()
K2 = applyP(leftShift(leftShift(applyP(inputKey, "P10"))), "P8")
print("K2: ")
for i in range(len(K2)):
    print(f'{K2[i]}', end=" ")
