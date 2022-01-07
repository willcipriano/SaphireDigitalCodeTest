def locate_palindromic_substring(text: str) -> str:
    """Function that returns the longest substring within a string that is a palindrome."""
    size = len(text)
    result = ""

    for x in range(size):
        for y in range(size, x, -1):

            if len(result) >= y-x:
                break

            elif text[x:y] == text[x:y][::-1]:
                result = text[x:y]
                break

    return result
