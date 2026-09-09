L = int(input("Masukan Nilai: "))
K = 1
while K <= L :
    if K % 3 == 0 and K % 5 == 0 :
        print("FizzzzzzzzzzBuzzzzzzzzzz")
    elif K % 5 == 0 :
        print("Buzzzzzzzzzz")   
    elif K % 3 == 0 :
        print("Fizzzzzzzzzz")
    else :
        print(K)
    K+=1