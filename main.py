# This is a sample Python script.

# Press Maj+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # find the lowest difference between the elements of the array
    # Write a function that, given an array A of N integers, returns the smallest positive integer (greater than 0) that does not occur in A.
    # For example, given A = [1, 3, 6, 4, 1, 2], the function should return 0.
    # Given A = [1, 2, 3], the function should return 1.
    # Given A = [−1, −3], the function should return 2.
    # Write an efficient algorithm for the following assumptions:
    # N is an integer within the range [1..100,000];
    # each element of array A is an integer within the range [−1,000,000..1,000,000].

    A = [1,3,6,4,1,2,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,67,68,69,70,71,72,73,74,75,76,77,78,79,80,81,82,83,84,85,86,87,88,89,90,91,92,93,94,95,96,97,98,99,100,101,102,103,104,105,106,107,108,109,110,111,112,113,114,115,116,117,118,119,120,121,122,123,124,125,126,127,128,129,130,131,132,133,134,135,136,137,138,139,140,141,142,143,144,145,146,147,148,149,150,151,152,153,154,155,156,157,158,159,160,161,162,163,164,165,166,167,168,169,170,171,172,173,174,175,176,177,178,179,180,181,182,183,184,185,186,187,188,189,190,191,192,193,194,195,196,197,198,199,200,201,202,203,204,205,206,207,208,209,210,211,212,213,214,215,216,217,218,219,220,221,222,223,224,225,226,227,228,229,230,231,232,233,234,235,236,237,238,239,240,241,242,243,244,245,246,247,248,249,250,251,252,253,254,255,256,257,258]
    Am=[]
    print(A)
    # [1, 1, 2, 3, 4, 6]
    LowestDifference = 10000000
    for i in range(0, len(A)):
        for x in range(0, len(A)):
            Difference_Of_i= A[i]-A[x]
            Am.append(Difference_Of_i)
            if LowestDifference >= Difference_Of_i and Difference_Of_i>0:
                LowestDifference = Difference_Of_i
                NumberI=i
                NumberX=x
            else:
                continue
    print(LowestDifference)
    print(A[NumberI])
    print(A[NumberX])
    print(len(Am))
# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')
