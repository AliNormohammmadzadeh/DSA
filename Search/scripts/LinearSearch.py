def Linear_Search(array, n , k):
    for j in range(0,n):
        if (array[j] ==  k):
            return j+1
    return -1 

def Make_array(word):
    array = word.split()
    n = len(array)
    return array , n


# text = "ali normohammadzade hastam az mashad 21 sale dar hale kos kalak bazi ."
# print(Make_array(text))
def run():
    text = input("Enter your text : ")
    search = input("kalame barai search ra vared konid : ")
    array , n =  Make_array(text)
    if (Linear_Search(array, n , search) == -1):
        print("kalame vared shode dar text nabod")
    else:
        print("kalame vared shode dar index shomare " +str(Linear_Search(array, n , search))+  " mibashad")

if __name__ == "__main__":
    run()
