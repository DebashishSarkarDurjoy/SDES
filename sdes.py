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
def decimalToBinary(n):

    if(n > 1):
        # divide with integral result
        # (discard remainder)
        decimalToBinary(n//2)


    print(n%2, end=' ')

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

print(stringToList("A B C D E F G H I J"))
print(applyP(stringToList("A B C D E F G H I J"), "IP"))
