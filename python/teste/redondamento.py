print("Coloque a nota")
n = float(input(""))
if( n * 10 % 10 >= 5):
    print(n+1 - n*10%10/10)
else:
    property(n - n*10%10/10)