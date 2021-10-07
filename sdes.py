import numpy as np
import math

IP = [2, 6, 3, 1, 4, 8, 5 , 7]
IPinverse = [4, 1, 3, 5, 7, 2, 8, 6]
P10 = [3, 5, 2, 7, 4, 10, 1, 9, 8, 6]
P8 = [6, 3, 7, 4, 8, 5, 10, 9]
E_P = [4, 1, 2, 3, 2, 3, 4, 1]
P4 = [2, 4, 3, 1]

S0 = [
    [1, 0, 3, 2],
    [3, 2, 1, 0],
    [0, 2, 1, 3],
    [3, 1, 3, 2]
]

S1 = [
    [0, 1, 2, 3],
    [2, 0, 1, 3],
    [3, 0, 1, 0],
    [2, 1, 0, 3]
]

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
def decimalToBinary(n, digits):
    binArray = [] #declaring the list here to pass it to the recurse function
    decimalToBinaryRecurse(n, binArray) #call the actual conversion function
    if (digits > len(binArray)):
        for i in range(0, digits - len(binArray)):
            binArray.append(0)
        if (binArray[0] == 1):
            temp = binArray.pop(0)
            binArray.append(temp)
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
    leftHalf = arr[: 5]
    rightHalf = arr[5: ]

    temp = leftHalf.pop(0)
    leftHalf.append(temp)
    temp = rightHalf.pop(0)
    rightHalf.append(temp)

    return leftHalf + rightHalf

def XOR(arr1, arr2):
    result = []
    for i in range(len(arr1)):
        if arr1[i] != arr2[i]:
            result.append(1)
        else:
            result.append(0)
    return result

def binToDec(arr):
    result = 0
    for i in range(len(arr)):
        if arr[i] == 1:
            result = result + math.pow(2, len(arr) - i - 1)
    return int(result)

def valToS0(row, col):
    return S0[row][col]

def valToS1(row, col):
    return S1[row][col]

def tillSW(arr, leftHalf, rightHalf):
    r1 = []
    c1 = []
    r1.append(arr[0])
    r1.append(arr[3])
    c1.append(arr[1])
    c1.append(arr[2])

    r2 = []
    c2 = []
    r2.append(arr[4])
    r2.append(arr[7])
    c2.append(arr[5])
    c2.append(arr[6])


    leftPart = decimalToBinary(valToS0(binToDec(r1), binToDec(c1)), 2)
    rightPart = decimalToBinary(valToS1(binToDec(r2), binToDec(c2)), 2)

    print(leftPart)
    print(rightPart)

    temp = leftPart + rightPart

    temp = applyP(temp, "P4")

    temp = XOR(temp, leftHalf)

    switched = rightHalf + temp

    return switched

def finalSteps(switchedArr, K2):
    rightEP = applyP(switchedArr[4: ], "E_P")
    rightEP = XOR(rightEP, K2)
    print(rightEP)
    r1 = []
    c1 = []
    r1.append(rightEP[0])
    r1.append(rightEP[3])
    c1.append(rightEP[1])
    c1.append(rightEP[2])

    r2 = []
    c2 = []
    r2.append(rightEP[4])
    r2.append(rightEP[7])
    c2.append(rightEP[5])
    c2.append(rightEP[6])

    leftPart = decimalToBinary(valToS0(binToDec(r1), binToDec(c1)), 2)
    rightPart = decimalToBinary(valToS1(binToDec(r2), binToDec(c2)), 2)
    print(leftPart)
    print(rightPart)
    temp = leftPart + rightPart
    print(temp)
    temp = applyP(temp, "P4")
    print(temp)
    temp = XOR(temp, switchedArr[: 4])
    print(temp)
    temp = temp + switchedArr[4: ]
    print(temp)
    temp = applyP(temp, "IP-1")

    return temp

# print(stringToList("A B C D E F G H I J"))
# print(applyP(stringToList("A B C D E F G H I J"), "IP"))
def encrypt():
    binary = [1, 1, 0, 0, 1, 1, 0, 0]

binary = [1, 1, 0, 0, 1, 1, 0, 0]
print("Original T: ")
for i in range(len(binary)):
    print(f'{binary[i]}', end=" ")

print()

binaryIP = applyP(binary, "IP")
print("IP on Text: ")
for i in range(len(binaryIP)):
    print(f'{binaryIP[i]}', end=" ")
leftHalf = binaryIP[: 4]
rightHalf = binaryIP[4: ]
print()

rightEP = applyP(binaryIP[-4:], "E_P")
print("RightEP: ")
for i in range(len(rightEP)):
    print(f'{rightEP[i]}', end=" ")

print()

inputKey = [1,1,1,0,0, 1,1,0,0,1]

print()
K1 = applyP(leftShift(applyP(inputKey, "P10")), "P8")
print("K1: ")
for i in range(len(K1)):
    print(f'{K1[i]}', end=" ")

print()
K2 = applyP((leftShift(leftShift(leftShift(applyP(inputKey, "P10"))))), "P8")
print("K2: ")
for i in range(len(K2)):
    print(f'{K2[i]}', end=" ")

print()

print(rightEP)
result = XOR(rightEP, K1)
print(result)

switchedArr = tillSW(result, leftHalf, rightHalf)
print(switchedArr)

print("Final steps to ciphertext")
print(finalSteps(switchedArr, K2))

print()
print()
print("Decryption")
ciphertext = [1, 1, 1, 0, 0, 1, 0, 1]
uptoSW = finalSteps(ciphertext, K2)
print(uptoSW)
