from pythonds.basic.stack import Stack

def parChecker(symbolString):
    s = Stack()
    balanced = True
    i = 0
    while i < len(symbolString) and balanced:
        symbol = symbolString[i]
        if symbol in "([{":
            s.push(symbol)
        else:
            if s.isEmpty():
                balanced = False
            else:
                top = s.pop()
                if not matches(top, symbol):
                    balanced = False
        i = i + 1
    if balanced and s.isEmpty():
        return True
    else:
        return False

def matches(open, close):
    opens = "([{"
    closers = ")]}"
    return opens.index(open) == closers.index(close)

if __name__ == '__main__':
    test_case1 = '{{([][])}()}';
    test_case2 = '([{})]'
    print "Correctly: ", parChecker(test_case1)
    print "Incorrectly: ", parChecker(test_case2)
