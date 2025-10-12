stack = []

def push(stack: list[float], x: float) -> None: #Кладем элемент сверху
    stack.append(x)

def pop(stack: list[float]) -> float: #Снимаем верхний элемент
    if not stack:
        raise IndexError("pop from empty stack")
    return stack.pop()

def peek(stack: list[float]) -> float: #Смотрим, не снимая, верхний элемент
    if not stack:
        raise IndexError("peek from empty stack")
        
    return stack[-1]

def is_empty(stack: list[float]) -> bool: #Пуст ли стек
    return not stack

