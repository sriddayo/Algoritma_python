n = int(input("masukkan angka batasan: "))
i = 1
while i <= n :
   if i % 3 == 0 and i % 5 == 0 :
    print("fizzbuzzzzzzz")
   elif i % 5 == 0:
    print("buzzzz")
   elif i % 3 == 0:
    print("fizzzz")
   else :
    print (i)
   i+=1