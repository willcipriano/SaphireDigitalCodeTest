class PairResult:
    """Represents a attempt to pair together a word from two elements"""

    def __init__(self, part_1: str, part_2: str, word: str):
        self.part_1 = part_1
        self.part_2 = part_2
        self.word = word

    def is_match(self):
        if self.part_1 + self.part_2 == self.word:
            return True
        else:
            return False

    def print(self):
        if self.is_match():
            print(f"Match: {self.part_1} + {self.part_2} == {self.word}")
        else:
            print(f"No Match: {self.part_1} + {self.part_2} != {self.word}")


def __create_word_pairs__(word: str, parts: list[str]) -> list[PairResult]:
    """Creates all possible word pairs for future review"""
    result: list[PairResult] = list()

    for first_part in parts:
        for second_part in parts:

            if first_part != second_part:
                result.append(PairResult(first_part, second_part, word))

    return result


def pair_words(words: list[str], parts: list[str], print_result=True) -> dict[str, list[PairResult]]:
    """Generates and prints all possible word pairs based on a list of words and word parts"""
    result: dict[str, list[PairResult]] = dict()

    for word in words:
        result[word] = __create_word_pairs__(word, parts)

    if print_result:
        for attempt_list in result.values():
            for attempt in attempt_list:
                attempt.print()

    return result
