from random import *
from termcolor import colored
d={'a':1,'b':2,'c':3,'d':4,'e':5,'f':6,'g':7,'h':8,'i':9,'j':10,'k':11,'l':12,'m':13,'n':14,'o':15,'p':16,'q':17,'r':18,'s':19,'t':20,'u':21,'v':22,'w':23,'x':24,'y':25,'z':26,'1':27,'2':28,'3':29,'4':30,'5':31,'6':32,'7':33,'8':34,'9':35,'0':36,'!':37,'@':38,'#':39,'$':40,'&':41,'-':42,'_':43,'~':44}
def myf():
    i=0
    rword=""
    while i <l:
        r_no=randint(1,44)
        for key,value in d.items():
            if r_no==value:
                rword=rword+key
        i=i+1
    return rword
a='''
 _ __   __ _ ___ ___        __ _  ___ _ __  
| '_ \ / _` / __/ __|_____ / _` |/ _ \ '_ \ 
| |_) | (_| \__ \__ \_____| (_| |  __/ | | |
| .__/ \__,_|___/___/      \__, |\___|_| |_|
|_|                        |___/  
'''
print(colored(a,'red'))
l=int(input("enter the length of password :\t"))
print()
print('password   :' , colored(myf(),'green'))
print()








