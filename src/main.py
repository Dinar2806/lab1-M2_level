import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from src.modules.operations import *
from src.modules.stack import *
from src.modules.utils import *



def main():
    # inputExpr = ["2**(3          ulehrer+7)//3jawrlfheh-4*2/7",
    #          "2**(-3)**2",
    #          "(2+3*4+(5+6))+7",
    #          "+(1 + 2) * +3 + 4 / +(5 - 1)",
    #          "1 + 2 * 3 - 4 / 2",
    #          "-5 + 3",
    #          "5/2"]
    # #res = infix_to_rpn(tokenisation(inputExpr[1]))
    # value = inputExpr[6]
    # res = calculate(inputExpr[6])
    # rpn = infix_to_rpn(value)
    # rpn_calc = rpn_calculate("2 3")
    # #print(tokenisation(inputExpr[0]))
    # print(rpn_calc)
    # print(rpn)
    # print(len(rpn.split(' ')))
    # print(tokenisation(value))

    while True:

        try:
            expression: str = input("Введите ваше выражение (для выхода отправьте exit): ")
        except KeyboardInterrupt:
            exit(1)
        
        if expression == "exit":
            exit(0)
        try:
            result = calculate(expr=expression)
        except Exception:
            result = None
        
        print(result)

    

if __name__ == "__main__":
    main()


