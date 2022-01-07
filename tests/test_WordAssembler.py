from CodeTestLib import WordAssembler


def test_provided():
    words = [
        "albums",
        "barely",
        "befoul",
        "convex",
        "hereby",
        "jigsaw",
        "tailor",
        "weaver",
    ]
    word_parts = [
        "al",
        "bums",
        "bar",
        "ely",
        "be",
        "foul",
        "con",
        "vex",
        "here",
        "by",
        "jig",
        "saw",
        "tail",
        "or",
        "we",
        "aver",
    ]
    words_used = list()

    results = WordAssembler.pair_words(words, word_parts, print_result=False)

    for word in results.keys():
        results_list = results.get(word)
        found = False

        if word == "albums":
            for result in results_list:
                if result.is_match():
                    assert result.part_1 == "al"
                    assert result.part_2 == "bums"
                    found = True
            assert found
            words_used.append(word)

        if word == "barely":
            for result in results_list:
                if result.is_match():
                    assert result.part_1 == "bar"
                    assert result.part_2 == "ely"
                    found = True
            assert found
            words_used.append(word)

        if word == "befoul":
            for result in results_list:
                if result.is_match():
                    assert result.part_1 == "be"
                    assert result.part_2 == "foul"
                    found = True
            assert found
            words_used.append(word)

        if word == "convex":
            for result in results_list:
                if result.is_match():
                    assert result.part_1 == "con"
                    assert result.part_2 == "vex"
                    found = True
            assert found
            words_used.append(word)

        if word == "hereby":
            for result in results_list:
                if result.is_match():
                    assert result.part_1 == "here"
                    assert result.part_2 == "by"
                    found = True
            assert found
            words_used.append(word)

        if word == "jigsaw":
            for result in results_list:
                if result.is_match():
                    assert result.part_1 == "jig"
                    assert result.part_2 == "saw"
                    found = True
            assert found
            words_used.append(word)

        if word == "tailor":
            for result in results_list:
                if result.is_match():
                    assert result.part_1 == "tail"
                    assert result.part_2 == "or"
                    found = True
            assert found
            words_used.append(word)

        if word == "weaver":
            for result in results_list:
                if result.is_match():
                    assert result.part_1 == "we"
                    assert result.part_2 == "aver"
                    found = True
            assert found
            words_used.append(word)

    assert len(words) == len(words_used)
