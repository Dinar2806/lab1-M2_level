import pytest
from src.modules.utils import *
# import sys
# import os
# sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

class TestInfixToPostfix:
    """Небольшие тесты преобразования инфиксной записи в обратную польскую нотацию"""
    
    def test_simple_operations(self):
        """Простые арифметические операции"""
        assert infix_to_rpn("2 + 3") == "2 3 +"
        assert infix_to_rpn("5 - 2") == "5 2 -"
        assert infix_to_rpn("4 * 3") == "4 3 *"
        assert infix_to_rpn("8 / 2") == "8 2 /"
    
    def test_operator_precedence(self):
        """Приоритет операций"""
        assert infix_to_rpn("2 + 3 * 4") == "2 3 4 * +"
        assert infix_to_rpn("2 * 3 + 4") == "2 3 * 4 +"
        assert infix_to_rpn("10 - 4 / 2") == "10 4 2 / -"
    
    def test_parentheses(self):
        """Выражения со скобками"""
        assert infix_to_rpn("(2 + 3) * 4") == "2 3 + 4 *"
        assert infix_to_rpn("2 * (3 + 4)") == "2 3 4 + *"
        assert infix_to_rpn("(1 + 2) * (3 - 4)") == "1 2 + 3 4 - *"
    
    def test_complex_expressions(self):
        """Сложные выражения"""
        assert infix_to_rpn("1 + 2 * 3 - 4 / 2") == "1 2 3 * + 4 2 / -"
        assert infix_to_rpn("(1 + 2) * 3 + 4 / (5 - 1)") == "1 2 + 3 * 4 5 1 - / +"
    
    def test_unary_operators(self):
        """Унарные операторы (если поддерживаются)"""
        assert infix_to_rpn("-5 + 3") == "5 ~ 3 +"
        assert infix_to_rpn("+2 * -3") == "2 3 ~ *"
    
    def test_whitespace_handling(self):
        """Обработка пробелов"""
        assert infix_to_rpn("  2  +  3  ") == "2 3 +"
        assert infix_to_rpn("2+3") == "2 3 +"


class TestEvaluatePostfix:
    """Тесты вычисления выражений в ОПН"""
    
    def test_simple_calculations(self):
        """Простые вычисления"""
        assert rpn_calculate("2 3 +") == 5
        assert rpn_calculate("5 2 -") == 3
        assert rpn_calculate("4 3 *") == 12
        assert rpn_calculate("8 2 /") == 4
    
    def test_complex_calculations(self):
        """Сложные вычисления"""
        assert rpn_calculate("2 3 4 * +") == 14  # 2 + 3 * 4
        assert rpn_calculate("1 2 + 3 *") == 9   # (1 + 2) * 3
        assert rpn_calculate("10 4 2 / -") == 8  # 10 - 4 / 2
    
    def test_float_results(self):
        """Дробные результаты"""
        assert rpn_calculate("5 2 /") == 2.5
        assert rpn_calculate("1 3 /") == 0.33
    

class TestFullCalculation:
    """Тесты полного цикла вычислений"""
    
    @pytest.mark.parametrize("expression,expected", [
        
        #Хаотичный набор выражений
        ("2 + 3", 5.0),
        ("10 - 4 * 2", 2.0),
        ("(10 - 4) * 2", 12.0),
        ("15 / 3 + 2", 7.0),
        ("1 + 2 * 3 - 4 / 2", 5.0),
        ("3 * (4 + 5)", 27.0),

        #Базовые выражения (уровень easy)
        ("1 + 1", 2.0),
        ("5 - 3", 2.0),
        ("4 * 6", 24.0),
        ("8 / 2", 4.0),
        ("10 + 20", 30.0),
        ("15 - 5", 10.0),
        ("7 * 8", 56.0),
        ("100 / 4", 25.0),

        #Выражения посложнее (уровень middle)
        ("2 + 3 * 4", 14.0),           # 2 + 12 = 14
        ("3 * 4 + 5", 17.0),           # 12 + 5 = 17
        ("10 - 4 / 2", 8.0),           # 10 - 2 = 8
        ("8 / 2 + 3", 7.0),            # 4 + 3 = 7
        ("1 + 2 * 3 - 4 / 2", 5.0),    # 1 + 6 - 2 = 5
        ("4 * 3 + 2 * 5", 22.0),       # 12 + 10 = 22
        ("20 / 4 - 2 * 1", 3.0),       # 5 - 2 = 3
        ("3 + 4 * 2 - 6 / 3", 9.0),

        #Выражения со скобками
        ("(2 + 3) * 4", 20.0),         # 5 * 4 = 20
        ("2 * (3 + 4)", 14.0),         # 2 * 7 = 14
        ("(10 - 4) / 2", 3.0),         # 6 / 2 = 3
        ("(1 + 2) * (3 - 4)", -3.0),   # 3 * (-1) = -3
        ("(5 * 2) + (3 * 4)", 22.0),   # 10 + 12 = 22
        ("(8 + 2) / (7 - 2)", 2.0),    # 10 / 5 = 2
        ("(1 + 2 * 3) - 4", 3.0),      # (1 + 6) - 4 = 3
        ("2 * (3 + 4 * 2)", 22.0),     # 2 * (3 + 8) = 22
        ("((1 + 2) * 3) - 4", 5.0),    # (3 * 3) - 4 = 5
        ("(5 - 3) * (4 + 2) / 2", 6.0), # 2 * 6 / 2 = 6

        #Выражения со вложенными скобками
        ("((2 + 3) * 4)", 20.0),
        ("(2 * (3 + 4))", 14.0),
        ("((1 + 2) * (3 - 4))", -3.0),
        ("(2 * (3 + (4 * 2)))", 22.0),
        ("((5 - 3) * (4 + 2)) / 2", 6.0),
        ("(1 + (2 * (3 + 1)))", 9.0),
        ("((8 / 2) + (3 * 2))", 10.0),

        #Дробные результаты
        ("5 / 2", 2.5),
        ("1 / 2", 0.5),
        ("3 / 4", 0.75),
        ("1 + 1 / 2", 1.5),
        ("3 * 2 / 4", 1.5),
        ("(1 + 2) / 4", 0.75),
        ("5 / 2 * 3", 7.5),
        ("1 / 3 + 1 / 3", 0.67),

        #Отрицательные числа
        ("-5 + 3", -2.0),
        ("5 + (-3)", 2.0),
        ("-2 * 3", -6.0),
        ("4 * (-2)", -8.0),
        ("-10 / 2", -5.0),
        ("(-4 + 6) * 2", 4.0),
        ("3 - (-2)", 5.0),
        ("-1 * (-1)", 1.0),

        #Комплексные выражения
        ("1 + 2 * 3 - 4 / 2 + 5", 10.0),           # 1 + 6 - 2 + 5 = 10
        ("(1 + 2) * 3 + 4 / (5 - 1)", 10.0),       # 3*3 + 4/4 = 9 + 1 = 10
        ("10 - 2 * 3 + 4 / 2 - 1", 5.0),           # 10 - 6 + 2 - 1 = 5
        ("2 * 3 + 4 * 5 - 6 / 3", 24.0),           # 6 + 20 - 2 = 24
        ("(2 + 3) * (4 - 1) / 3", 5.0),            # 5 * 3 / 3 = 5
        ("1 + 2 * (3 + 4 * (5 - 2))", 31.0),       # 1 + 2*(3 + 4*3) = 1 + 2*15 = 31
        ("100 / (2 * 5) + 3 * 4", 22.0),           # 100/10 + 12 = 10 + 12 = 22

        
    ])
    def test_calculate_integration(self, expression, expected):
        """Интеграционные тесты полного вычисления"""
        result = calculate(expression)
        assert result == expected
    
    def test_calculate_with_floats(self):
        """Вычисления с дробными числами"""
        assert calculate("5 / 2") == 2.5
        assert calculate("1.5 + 2.5") == 4.0
        assert calculate("3.2 * 2") == 6.4


class TestEdgeCases:
    """Тесты граничных случаев"""
    
    def test_single_number(self):
        """Одно число"""
        assert infix_to_rpn("42") == "42"
        assert rpn_calculate("42") == 42
        assert calculate("42") == 42
    
    def test_empty_expression(self):
        """Пустое выражение"""
        with pytest.raises(ValueError):
            infix_to_rpn("")
        
        with pytest.raises(ValueError):
            rpn_calculate("")
    
    def test_invalid_characters(self):
        """Недопустимые символы"""
        with pytest.raises(ValueError):
            infix_to_rpn("2 + a")
        
        with pytest.raises(ValueError):
            infix_to_rpn("2 @ 3")
    
    def test_mismatched_parentheses(self):
        """Непарные скобки"""
        with pytest.raises(ValueError):
            infix_to_rpn("(2 + 3")
        
        with pytest.raises(ValueError):
            infix_to_rpn("2 + 3)")


# Фикстуры для тестирования производительности
@pytest.fixture
def complex_expression():
    return "1 + 2 * 3 - 4 / 2 + (5 - 3) * 4"




if __name__ == "__main__":
    pytest.main([__file__, "-v"])