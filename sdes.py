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
    for index in permutations[permutationName]: #uses the values from the dictionary
        result.append(charList[index - 1])
    return result

#performs the binary left shift by popping the first element and
#inserting it at the end
#calling it n times will perform left-shift-n
#returns the result as a list
def leftShift(arr):
    leftHalf = arr[: 5] #takes only the left side 5 digits
    rightHalf = arr[5: ] #takes only the right side 5 digits

    temp = leftHalf.pop(0) #removes the first element, stores it in temp
    leftHalf.append(temp) #inserts the temp at the end
    temp = rightHalf.pop(0) #removes the first element, stores it in temp
    rightHalf.append(temp) #inserts the temp at the end

    return leftHalf + rightHalf

def powerOf2(power):
    result = 1
    for i in range(power):
        result = 2 * result
    return int(result)
#performs binary XOR operation
#returns a list
def XOR(arr1, arr2):
    result = []
    for i in range(len(arr1)):
        if arr1[i] != arr2[i]: #if two digits are different, it appends 1
            result.append(1)
        else:
            result.append(0) #otherwise appends 0
    return result

#converts list containing binary numbers into its decimal base equivalent
def binToDec(arr):
    result = 0
    for i in range(len(arr)): #loops over the lenght of arr
        if arr[i] == 1:
            #this is basically this: result = result + 2 ^ position of 1 in arr
            result = result + powerOf2(len(arr) - i - 1)
    return int(result)

#takes a row and col integer and returns a value from the corresponding
#row and col in the 2d list S0
def valToS0(row, col):
    return S0[row][col]

#takes a row and col integer and returns a value from the corresponding
#row and col in the 2d list S1
def valToS1(row, col):
    return S1[row][col]

#the function that uses K1
#takes in an array, Key1 and a boolean value
def fk1(arr, K1, decryption = False):
    #takes the left-portion of arr and applies E/P
    rightEP = applyP(arr[4: ], "E_P")
    #then performs XOR on the returned value
    rightEP = XOR(rightEP, K1)
    r1 = []
    c1 = []
    #gets the row and col to fetch data from S0
    r1.append(rightEP[0])
    r1.append(rightEP[3])
    c1.append(rightEP[1])
    c1.append(rightEP[2])
    #gets the row and col to fetch data from S1
    r2 = []
    c2 = []
    r2.append(rightEP[4])
    r2.append(rightEP[7])
    c2.append(rightEP[5])
    c2.append(rightEP[6])

    #gets binary equivalent of the left part
    leftPart = decimalToBinary(valToS0(binToDec(r1), binToDec(c1)), 2)
    #gets binary equivalent of the right part
    rightPart = decimalToBinary(valToS1(binToDec(r2), binToDec(c2)), 2)

    temp = leftPart + rightPart
    temp = applyP(temp, "P4") #applies P4 on the result
    temp = XOR(temp, arr[: 4]) #applies XOR on temp and righ-portion of arr
    temp = temp + arr[4: ] #concatenates left-portion of arr with temp
    if decryption == True:
        #if decrypting then apply IP-1 and return the result
        tempIPinverse = applyP(temp, "IP-1")
        return tempIPinverse

    #otherwise perform switch and return the result
    switched = arr[4:] + temp
    return switched

#the function that uses K2
#takes in an array, Key2 and a boolean value
def fk2(arr, K2, decryption = False):
    #takes the left-portion of arr and applies E/P
    rightEP = applyP(arr[4: ], "E_P")
    #then performs XOR on the returned value
    rightEP = XOR(rightEP, K2)

    r1 = []
    c1 = []
    #gets the row and col to fetch data from S0
    r1.append(rightEP[0])
    r1.append(rightEP[3])
    c1.append(rightEP[1])
    c1.append(rightEP[2])

    r2 = []
    c2 = []
    #gets the row and col to fetch data from S1
    r2.append(rightEP[4])
    r2.append(rightEP[7])
    c2.append(rightEP[5])
    c2.append(rightEP[6])

    #gets binary equivalent of the left part
    leftPart = decimalToBinary(valToS0(binToDec(r1), binToDec(c1)), 2)
    #gets binary equivalent of the right part
    rightPart = decimalToBinary(valToS1(binToDec(r2), binToDec(c2)), 2)

    temp = leftPart + rightPart
    temp = applyP(temp, "P4") #applies P4 on the result
    temp = XOR(temp, arr[: 4]) #applies XOR on temp and righ-portion of arr
    if decryption == True:
        #if decrypting then perform switch and return the result
        switched = arr[4:] + temp
        return switched

    #otherwise perform concatenation with the left-portion of arr
    temp = temp + arr[4:]
    temp = applyP(temp, "IP-1") #apply IP-1 on temp and return temp
    return temp


def decrypt():
    #get use input for Ciphertext
    inputTEXT = input("Enter Ciphertext: ")
    inputArr = []
    for c in inputTEXT:
        inputArr.append(int(c))

    #get use input for Key
    inputKEY = input("Enter K: ")
    inputKey = []
    for c in inputKEY:
        inputKey.append(int(c))


    print("K1: ", end="")
    K1 = applyP(leftShift(applyP(inputKey, "P10")), "P8")
    print(K1)

    print("K2: ", end="")
    K2 = applyP((leftShift(leftShift(leftShift(applyP(inputKey, "P10"))))), "P8")
    print(K2)

    result = applyP(inputArr, "IP")

    result = fk2(result, K2, decryption = True)

    result = fk1(result, K1, decryption = True)
    print("Plaintext: ", end="")
    print(result)


# print(stringToList("A B C D E F G H I J"))
# print(applyP(stringToList("A B C D E F G H I J"), "IP"))
def encrypt():
    #get use input for Plaintext
    inputTEXT = input("Enter Plaintext: ")
    inputArr = []
    for c in inputTEXT:
        inputArr.append(int(c))

    #get user input for Key
    inputKEY = input("Enter Key: ")
    inputKey = []
    for c in inputKEY:
        inputKey.append(int(c))

    inputIP = applyP(inputArr, "IP")

    print("K1: ", end="")
    K1 = applyP(leftShift(applyP(inputKey, "P10")), "P8")
    print(K1)

    print("K2: ", end="")
    K2 = applyP((leftShift(leftShift(leftShift(applyP(inputKey, "P10"))))), "P8")
    print(K2)


    result = fk1(inputIP, K1)

    result = fk2(result, K2)

    print("Ciphertext: ", end="")
    print(result)


def showMenu():
    print("1. Encrypt.")
    print("2. Decrypt.")
    option = input(">> ")
    return int(option)

option = showMenu()
if option == 1:
    encrypt()
else:
    decrypt()
