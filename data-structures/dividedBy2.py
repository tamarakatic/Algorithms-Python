from pythonds.basic.stack import Stack

def dividedDecNumBy2(decNumber):
    remaindersStack = Stack()

    while decNumber > 0:
        remainer = decNumber % 2
        remaindersStack.push(remainer)
        decNumber = decNumber // 2

    binaryResult = ""
    while not remaindersStack.isEmpty():
        binaryResult = binaryResult + str(remaindersStack.pop())

    return binaryResult

if __name__ == "__main__":
    print "Result of decimal number 62 divided by 2 is: ", dividedDecNumBy2(72)
