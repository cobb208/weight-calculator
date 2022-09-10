from re import T
import sys

import barbellcalc as b


def mainLoop():
    n = len(sys.argv)
    errorSyntax = "Please enter your targeted weight, followed by the barbell weight, if it is a standard barbell you do not need to include the weight.\nex: main.py 255 65\nex2: main.py 365"

    if(n == 3):
        try:
            targetWeight = int(sys.argv[1])
            barbellWeight = int(sys.argv[2])
            if(barbellWeight):
                barbellCalc = b.BarbellCalc(targetWeight, barbellWeight)
            else:
                barbellCalc = b.BarbellCalc(targetWeight)

            barbellCalc.calculate()
        except:
            print(errorSyntax)
    elif(n == 2):
        try:
            targetWeight = int(sys.argv[1])
            print(f"target weight: {targetWeight}")
            barbellCalc = b.BarbellCalc(targetWeight).calculate()
        except:
            print(errorSyntax)
    else:
        print(errorSyntax)

if(__name__ == '__main__'):
    print(sys.argv)
    
    mainLoop()