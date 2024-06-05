import sys
from os.path import dirname, abspath
d = dirname(dirname(abspath(__file__)))
sys.path.append(d+'\\tp\\')
from tempo import *
print("Coloque a nota")
n = float(input(""))
t = crono_1()
if( n * 10 % 10 >= 5):
    print(n+1 - n*10%10/10)
else:
    print(n - n*10%10/10)
crono_2(t)