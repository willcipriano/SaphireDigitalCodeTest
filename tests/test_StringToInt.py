from CodeTestLib import StringToInt


def test_single_digit_results():
    result_one = StringToInt.StringInt("one")
    assert result_one.int_repr == 1

    result_two = StringToInt.StringInt("two")
    assert result_two.int_repr == 2

    result_two = StringToInt.StringInt("six")
    assert result_two.int_repr == 6


def test_complex_results():
    result_one = StringToInt.StringInt("one hundred")
    assert result_one.int_repr == 100

    result_two = StringToInt.StringInt("negative seven hundred twenty nine")
    assert result_two.int_repr == -729

    result_three = StringToInt.StringInt("one million one hundred one")
    assert result_three.int_repr == 1000101


def test_exception_handling():
    caught_exception = None

    try:
        StringToInt.StringInt("This won't work")
    except StringToInt.InvalidInputException as ex:
        caught_exception = ex

    assert caught_exception is not None
