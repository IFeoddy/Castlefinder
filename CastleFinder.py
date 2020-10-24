import math
from colorama import init
from colorama import Fore, Back, Style
import os
init()

os.system("mode con cols=80 lines=15") # opens window in 80 * 15

def ctg (number): #function to find ctg
    return 1 / math.tan (number)
    
print(Fore.GREEN + ' _____   ___   _____ _____ _      _____  ______ _____ _   _______ ___________ ')
print(Fore.GREEN + '/  __ \ / _ \ /  ___|_   _| |    |  ___| |  ___|_   _| \ | |  _  \  ___| ___ \\')
print(Fore.GREEN + '| /  \// /_\ \\ `--.   | | | |    | |__   | |_    | | |  \| | | | | |__ | |_/ /')
print(Fore.GREEN + '| |    |  _  | `--. \ | | | |    |  __|  |  _|   | | | . ` | | | |  __||    / ')    
print(Fore.GREEN + '| \__/\| | | |/\__/ / | | | |____| |___  | |    _| |_| |\  | |/ /| |___| |\ \ ')
print(Fore.GREEN + ' \____/\_| |_/\____/  \_/ \_____/\____/  \_|    \___/\_| \_/___/ \____/\_| \_|' + Fore.WHITE)
print("")


x1 = float( input ('Enter 1st x cordinate: '))
z1 = float ( input ('Enter 1st z cordinate: '))
f1 = float( input ('Enter 1st angle of throw: '))

x2 = float( input ('Enter 2nd x cordinate: '))
z2 = float ( input ('Enter 2nd z cordinate: '))
f2 = float ( input ('Enter 2nd angle of throw: '))

p = math.pi / 180

if math.fabs ( f1 - f2 ) < 1 :
    print (Fore.RED + "Angles can`t be raw." + Fore.BLACK)
elif (( f1 < 0 ) and ( f2 > 0 )) or (( f1 > 0 ) and ( f2 < 0 ) and (Math.fabs(Math.fabs(Math.fabs(a1) - 180) - Math.fabs(a2)) < 1)):
    print (Fore.RED + 'Angles can\'t be reversed of them selfes.' + Fore.BLACK)
else:
    if (int (f1) == -180) or (int (f1) == 180) or (int (f1) == 0):
        x = int (x1)
        z = int (( ctg (( -1 * f2 ) * p) * x1 - ( x2 * ctg (( -1 * f2 ) * p) - z2 )))
        print (Fore.GREEN +"Castle x: ", x)
        print (Fore.GREEN +"Castle z: ", z, " " + Fore.BLACK)
        
        
    if (int (f1) == -90) or (int (f1) == 90):
        z = int (z1)
        x = int (( x2 * ctg ((-1 * f2) * p) - z2 + z1) / ctg ((-1 * f2) * p))
        print (Fore.GREEN +"Castle x: ", x)
        print (Fore.GREEN +"Castle z: ", z, " " + Fore.BLACK)
        
    if (int (f2) == -180) or (int (f2) == 180) or (int (f2) == 0):
        x = int (x2)
        z = int (( ctg (( -1 * f1 ) * p) * x2 - ( x1 * ctg (( -1 * f1 ) * p) - z1 )))
        print (Fore.GREEN +"Castle x: ", x)
        print (Fore.GREEN +"Castle z: ", z, " " + Fore.BLACK)
        
    if (int (f1) == -90) or (int (f1) == 90):
        z = int (z2)
        x = int (( x1 * ctg ((-1 * f1) * p) - z1 + z2) / ctg ((-1 * f1) * p))
        print (Fore.GREEN +"Castle x: ", x)
        print (Fore.GREEN +"Castle z: ", z, " " + Fore.BLACK)
        
    else:    
        x = int ((( x1 * ctg (( -1 * f1) * p) - z1) - ( x2 * ctg ( -1 * f2 * p) - z2)) / (ctg ((-1 * f1) * p) - ctg (( -1 * f2 ) * p)))  
        z = int ((ctg ((-1 * f1) * p) * x -( x1 * ctg ((-1 * f1 * p )) - z1 )))
        print (Fore.GREEN +"Castle x: ", x)
        print (Fore.GREEN +"Castle z: ", z, " " + Fore.BLACK)
input ()
    
