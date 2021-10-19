import sys
import game


def test_equality(actual, expected):
    line_num = sys._getframe(1).f_lineno
    if actual == expected:    
        print(f'Test at line {line_num} OK')
    else:
        print(f'Test at line {line_num} FAILED. Expected {expected} but got {actual}')


def run_tests():
    result_0 = game.start_new(1, 5, 10)
    test_equality(result_0, ['b', 'b', 'b', 'b', 's', 's', 's', '_', '_', 'd', 'd', '_', '_', '_', '_', '_', '_', '_', '_', '_'])

    result_1 = game.get_ships()
    test_equality(result_1, ['b', 'b', 'b', 'b', 's', 's', 's', '_', '_', 'd', 'd', '_', '_', '_', '_', '_', '_', '_', '_', '_'])

    result_2 = game.make_guess(1)
    test_equality(result_2, 'h')

    result_3 = game.make_guess(15)
    test_equality(result_3, 'm')

    result_4 = game.get_guesses()
    test_equality(result_4, ['h', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', 'm', '_', '_', '_', '_', '_'])

run_tests()