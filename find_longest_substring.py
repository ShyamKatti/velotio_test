import argparse
from collections import defaultdict


class SubstringFinder(object):

    def __init__(self):
        self.__input_str = None
        self.__input_str_characters = []

    def find_longest_substring(self, input_str):
        if not isinstance(input_str, str) or len(input_str) == 0:
            raise ValueError("input_str should be a valid string value")
        self.__input_str = input_str
        return self.__find_unique_substring()

    def __find_unique_substring(self):
        if len(self.__input_str_characters) == 1:
            return self.__input_str_characters

        visited_char = {}
        output = ""
        start_index, end_index = 0, 0
        for curr_index, curr_char in enumerate(self.__input_str):
            if curr_char in visited_char:
                start_index = max(visited_char[curr_char] + 1, start_index)
            if len(output) < end_index - start_index + 1:
                output = self.__input_str[start_index:end_index+1]
            visited_char[curr_char] = curr_index
            end_index += 1
        return output

    __slots__ = (
        "__input_str",
        "__input_str_characters",
    )


if __name__ == "__main__":
    s = SubstringFinder()
    print(s.find_longest_substring("abca"))