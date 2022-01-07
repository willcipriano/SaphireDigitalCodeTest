# Will Cipriano's Sapphire Digital Code Test

This repo contains CodeTestLib that in turn contains 3 modules:

## StringToInt

Converts a provided string into an integer representation.

Usage Example:
```
result = StringToInt.StringInt("one")
print(result.int_repr)
```
```
1
```

## PalindromeFinder

Locates the longest palindrome within a given text.

Usage Example:
```
result = PalindromeFinder.locate_palindromic_substring("Ilikeracecarsthatgofast")
print(result)
```
```
racecar
```

## WordAssembler

Assemble words from a given list with a given list of word parts.

Usage Example:
```
WordAssembler.pair_words(words, word_parts)
```
```
...
Match: bar + ely == barely
No Match: bar + be != barely
No Match: bar + foul != barely
No Match: bar + con != barely
No Match: bar + vex != barely
...
```

## Builds and Testing

Builds and the test suite are managed by tox, simply install tox and run the command tox to test.