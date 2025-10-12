from src.modules.stack import *

priority = { #Приоритет операторов
    '+': 2,
    '-': 2,
    '*': 3,
    '/': 3,
    '//': 3,
    '%': 3,
    '**': 4,
    '~': 5
    
}
associativity = { #Ассоциативность операторов
    '**': 'right',
    '~': 'right',
    '*': 'left',
    '/': 'left',
    '//': 'left',
    '%': 'left',
    '+': 'left',
    '-': 'left'
}

def is_operator(token):
     return token in associativity

def compare_priority(op1, op2):
        if priority[op1] > priority[op2]:
            return 1
        elif priority[op1] < priority[op2]:
            return -1
        else:
            if associativity[op1] == 'left':
                return 0
            else:
                return -1
            
def sum(stack):
    number1 = float(peek(stack))
    pop(stack)
    number2 = float(peek(stack))
    pop(stack)
    push(stack, number2 + number1)
    return stack

def subtraction(stack):
    number1 = float(peek(stack))
    pop(stack)
    number2 = float(peek(stack))
    pop(stack)
    push(stack, number2 - number1)
    return stack

def division(stack):
    number1 = float(peek(stack))
    pop(stack)
    number2 = float(peek(stack))
    pop(stack)
    try:
        push(stack, number2 / number1)
        return(stack)
    except ZeroDivisionError:
        print("Ошибка (деление на ноль)")
     
def multiplication(stack):
    number1 = float(peek(stack))
    pop(stack)
    number2 = float(peek(stack))
    pop(stack)
    push(stack, number2 * number1)
    return stack

def degree(stack):
    number1 = float(peek(stack))
    pop(stack)
    number2 = float(peek(stack))
    pop(stack)
    if number1 == 0 and number2 == 0:
        raise ValueError("0 в степени 0 - неопределенность")
    push(stack, number2**number1)
    return stack

def whole_part(stack):
    number1 = float(peek(stack))
    pop(stack)
    number2 = float(peek(stack))
    pop(stack)
    if number1 // 1 != number1 or number2 // 1 != number2:
        raise ValueError("Операции % и // применимы только к целым числам")
    try:
        push(stack, number2 // number1)
        return stack
    except ZeroDivisionError:
        print("Ошибка (деление на ноль!)")
    except ValueError:
        print("Операции % и // применимы только к целым числам")


def remainder(stack):
    number1 = float(peek(stack))
    pop(stack)
    number2 = float(peek(stack))
    pop(stack)
    if number1 // 1 != number1 or number2 // 1 != number2:
        raise ValueError("Операции % и // применимы только к целым числам")
    try:
        push(stack, number2 % number1)
        return stack
    except ZeroDivisionError:
        print("Ошибка (деление на ноль!)")
    except ValueError:
        print("Операции % и // применимы только к целым числам")

def unary_minus(stack):
    number1 = float(peek(stack))
    pop(stack)
    push(stack, -number1)
    return stack

