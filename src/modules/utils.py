import re

from src.modules.operations import *
from src.modules.stack import *

def input_checker(inputExpr: str):
    """
    Функция для проверки выражения на неизвестные символы.
    Если найден символ, не имеющий отношения к выражению, бросается ошибка.
    Входные данные: expr: string (выражение).
    Результат: выражение, если прошло валидацию и ошибка ValueError, если нет.
    """
    alphabet = "0123456789-+*/()%. "
    
    for i in inputExpr:
        if not alphabet.__contains__(i):
            raise ValueError
        else: continue
    return inputExpr
    

def input_corrector(inputExpr):       
    """
    Функция корректирует входное выражение, игнорируя 
    все символы, которые не имеют отношения к выражению
    Входные данные: inputExpr: string
    Выходные данные: откорректиррованная строка(выражение)
    """

    output = "" 
    alphabet = "0123456789-+*/()%. "
    inputExpr = inputExpr.replace(' ', '')

    for i in inputExpr:
        if alphabet.__contains__(i):
            output += i
        else: continue

    return output

def str_to_float_round(token: str, n: int) -> float: #Преобразование токена во float с n знаков после запятой
    try:
        return round(float(token), n)
    except ValueError:
        return "Ошибка"
            
def infix_to_rpn(expr: str) -> str:
        """
        Перевод инфиксной записи выражения в обратную польскую нотацию,
        входные данные: expr: string
        """
        expr = input_checker(expr)
        
        if expr == "":
            raise ValueError("Ошибка: пустое выражение")
        
        tokens = tokenisation(expr)
        stack = []
        output = []
        for token in tokens:
            if token.isdigit() or token.replace(".", "").isdigit():
                output.append(token)
            elif is_operator(token):
                while (stack and stack[-1] != '(' and 
                       is_operator(stack[-1]) and
                       compare_priority(stack[-1], token) >= 0):
                    output.append(stack.pop())
                stack.append(token)
            elif token == "(":
                    stack.append(token)
            elif token == ")":
                while stack and stack[-1] != '(':
                    output.append(stack.pop())
                if stack and stack[-1] == '(':
                    stack.pop()  # Удаляем открывающую скобку
                else:
                    raise ValueError("Несбалансированные скобки")
            elif token == '':
                continue
        while stack:
            if stack[-1] == '(':
                raise ValueError("Несбалансированные скобки")
            output.append(stack.pop())
        
        return ' '.join(output) 

def tokenisation(expr: str) -> list[str]: #разбиваем выражение на токены (операторы и операнды)
    """
    Разбитие выражения на отдельные токены,
    входные данные: expr: string
    """
    TOKEN_RE_EXT = re.compile(r"""
    \s*
    (
        \d+(?:\.\d+)?
    | \*\*
    | //
    | [%()+\-*/~]
        )
    """, re.VERBOSE)

    tokens = [m.group(1) for m in TOKEN_RE_EXT.finditer(expr)]
    if tokens[0] == '-':
         tokens[0] = tokens[0].replace('-', '~')
    for i in range(1, len(tokens)):
        if tokens[i] == '-' and not ((tokens[i-1].isdigit() or tokens[i-1].replace('.', '').isdigit()) or tokens[i-1] == ')'):
            tokens[i] = tokens[i].replace('-', '~')
        else: continue
    if tokens[0] == '+':
         tokens[0] = tokens[0].replace('+', '')
    for i in range(1, len(tokens)):
        if tokens[i] == '+' and not ((tokens[i-1].isdigit() or tokens[i-1].replace('.', '').isdigit()) or tokens[i-1] == ')'):
            tokens[i] = tokens[i].replace('+', '')
        else: continue

    return tokens


def rpn_calculate(rpn_expr: str):   #Считаем входное выражение (строку) в постфиксной польской нотации
    """
    Вычисление входного постфиксного выражения в RPN.
    Входные данные: rpn_expr: string (Выражение в обратной польской записи).
    Возврат: числовое значение, округленное до 2-х знаков после запятой
    """
    
    if rpn_expr == "":
        raise ValueError("Ошибка: пустое выражение")
    
    stack = []
    postfixExpr = rpn_expr.split()
    try:
        for item in postfixExpr:
            if item.isdigit() or item.replace(".", "").isdigit():
                push(stack, item)
            else:
                match item:
                    case "+":
                        stack = sum(stack)

                    case "-":
                        stack = subtraction(stack)

                    case "/":
                        stack = division(stack)
                        
                    case "*":
                        stack = multiplication(stack)

                    case "**":
                        stack = degree(stack)

                    case "//":
                        stack = whole_part(stack)

                    case "%":
                        stack = remainder(stack)

                    case "~": 
                        stack = unary_minus(stack)

    except IndexError:
        return "Ошибка во время вычисления выражения в обратной польской нотации"
    except ValueError:
        return "Ошибка во время вычисления выражения в обратной польской нотации"
    return stack[0]

def calculate(expr):
    """
    Функция представляет собой полный цикл этапов от получения выражения 
    до выдачи результата.
    Входные данные: expr:string (выражение).
    Выходные данные: результат, округленный до 2-х знаков после запятой

    """
    expr = input_corrector(expr)
    rpn_writing = infix_to_rpn(expr)
    rpn_calculated = rpn_calculate(rpn_writing)        
    #return f"{expr} = {rpn_calculated}"
    return str_to_float_round(rpn_calculated, 2)


