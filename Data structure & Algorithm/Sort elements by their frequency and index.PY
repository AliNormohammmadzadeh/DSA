class Data:
    def __init__(self,value,index ,count=0):
        self.value = value
        self.index = index
        self.count = count
    
    def __repr__(self):
        return "value = " + str(self.value) + "; index = " + str(self.index) + "; count = " + str(self.count) + ""

def sortByFrequencyAndIndex(arr):
    if arr is None or len(arr) < 2 :
        return 
    
    hm ={}       
    for i in range(len(arr)):
        hm.setdefault(arr[i],Data(arr[i],i)).count += 1
        print(hm[arr[i]])
    
    values = [*hm.values()]
    print("Value is : " ,values)

    values.sort(key=lambda x : (-x.count,x.index))
    print("Value is : " ,values)
    k = 0
    for data in values:
        for j in range(data.count):
            arr[k] = data.value
            k += 1
    
if __name__ == '__main__':
 
    arr = [3, 3, 1, 1, 1, 8, 3, 6, 8, 7, 8]
    sortByFrequencyAndIndex(arr)
    print(arr)
 