import math

def run():
    print("Binary Search")
    inputArray = input("Enter Your Array :").split()
    for i in range(len(inputArray)):
        inputArray[i] = int(inputArray[i])
    h = len(inputArray)
    l = 0
    search= int(input("Enter Your Search :"))
    BinarySearch(inputArray, h, l, search)
    
def BinarySearch(Array, h, l, search):
    mid = math.floor((h + l)/2)
    while(l<=h):
        if(Array[mid]< search):
            l = mid + 1
        elif(Array[mid] == search):
            print('Object has found , at index : '+str(mid))
            break
        else:
            h = mid - 1
        mid = math.floor((h + l)/2)
    if(l>h):
        print('Object Not Found')

if __name__ == "__main__":
    run()
    
    