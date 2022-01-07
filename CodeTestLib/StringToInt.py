"""
StringToInt.py provides a few singleton lists and a StringInt class that can be used to convert
strings of words into integer values.
"""

__string_num_values__ = [
    "zero",
    "one",
    "two",
    "three",
    "four",
    "five",
    "six",
    "seven",
    "eight",
    "nine",
    "ten",
    "eleven",
    "twelve",
    "thirteen",
    "fourteen",
    "fifteen",
    "sixteen",
    "seventeen",
    "eighteen",
    "nineteen",
]

__string_tens_values__ = [
    "twenty",
    "thirty",
    "forty",
    "fifty",
    "sixty",
    "seventy",
    "eighty",
    "ninety",
]

__string_hundred_scales__ = {"hundred": 100, "thousand": 1000, "million": 1000000}


class InvalidInputException(Exception):
    """Thrown if invalid input is provided."""

    def __init__(self, value):
        super().__init__(value + " is not a known number string value.")


class StringInt:
    """This class creates a integer representation of a string that conforms to the provided specification."""

    def __init__(self, number_string: str):
        self.str_repr: str = number_string

        is_negative = False

        temp = 0
        result = 0

        for word in self.str_repr.split():

            if word in __string_num_values__:
                temp = __string_num_values__.index(word)
            elif word in __string_tens_values__:
                result += (__string_tens_values__.index(word) + 2) * 10
            elif word in __string_hundred_scales__.keys():
                result += temp * __string_hundred_scales__.get(word)
                temp = 0
            elif word == "negative":
                is_negative = True
            elif word != "and":
                raise InvalidInputException(word)

        result += temp

        if is_negative:
            self.int_repr = -abs(result)
        else:
            self.int_repr = result
