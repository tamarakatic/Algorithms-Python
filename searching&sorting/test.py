from binary_search import binary_search
from linear_search import linear_search


def main():
    test_number = [2, 5, 8, 12, 16, 23, 38, 56, 72, 91]
    result = binary_search(test_number, 0, (len(test_number) - 1), 91)
    # test_number = [56, 3, 249, 518, 7, 26, 94, 651, 23, 9]
    # result = linear_search(test_number, 9)
    print "******************Binary search*******************"
    print "Result: ", result
    print "************************End***********************"

if __name__ == '__main__':
    main()
