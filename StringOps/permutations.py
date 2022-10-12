def permutation_count(string: str, pattern: str):
    """
    Given a reference string and a pattern, this function returns the number of permutations of that pattern that exist within the reference string.
    The key here is to compare the sorted characters in the sliding window with the sorted reference pattern. If they match, that means that the content
    in the sliding window is a permutation of the reference pattern (permutations have the common property of having the same sorted pattern)
    """
    permutation_count = 0
    string_as_list = list(string)
    pattern_as_list = list(pattern)
    sorted_pattern = sorted(pattern_as_list)

    for i in range(0, len(string_as_list) - len(pattern_as_list) + 1):
        window = string_as_list[i : i + len(pattern_as_list)]
        print(window)
        sorted_window = sorted(window)
        if sorted_window == sorted_pattern:
            permutation_count += 1
    print(permutation_count)
    return permutation_count


def permutation_generator(string: str):
    """
    This function uses recursion to generate all permutations of a given string
    Base case: string = "a" -> permutations = "a"
    Case string = "ab" -> permutations = "ab", "ba"
    Case string = "abc" -> permutations = "abc", "bca", "acb", "bac", "cab", "cba"

    Recursion opportunity:
        If "ab": start with "a", then place "b" in all possible positions around a.
        If "abc" : start with permutations of "ab" ("ab", "ba") and then place "c" in all possible positions around these permutations.
        So on and so forth.
    """
    pass


if __name__ == "__main__":
    permutation_count("cbabadcbabbabbcbabaabccbabc", "abbc")
