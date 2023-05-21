def anagram(word, otherWord):
    if len(word) != len(otherWord):
        return false
    return sorted(word) == sorted(otherWord)
