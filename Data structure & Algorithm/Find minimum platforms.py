from sympy import arity


def findMinPlatforms(arrival ,  deprature):
    arrival.sort()
    departure.sort()
    count = 0
    platform = 0
    i = j = 0
    while i < len(arrival):
        if arrival[i] < departure[j]:
            count += 1
            platform = max(platform, count)
            i += 1
        else:
            count -= 1
            j += 1
    return platform




if __name__ == '__main__':
 
    arrival = [2.00, 2.10, 3.00, 3.20, 3.50, 5.00]
    departure = [2.30, 3.40, 3.20, 4.30, 4.00, 5.20]
 
    print("The minimum platforms needed is", findMinPlatforms(arrival, departure))
 
