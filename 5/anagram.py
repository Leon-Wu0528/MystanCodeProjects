"""
File: anagram.py
Name: 吳竹孟
----------------------------------
This program recursively finds all the anagram(s)
for the word input by user and terminates when the
input string matches the EXIT constant defined
at line 19

If you correctly implement this program, you should see the
number of anagrams for each word listed below:
    * arm -> 3 anagrams
    * contains -> 5 anagrams
    * stop -> 6 anagrams
    * tesla -> 10 anagrams
    * spear -> 12 anagrams
"""

import time                   # This file allows you to calculate the speed of your algorithm

# Constants
FILE = 'dictionary.txt'       # This is the filename of an English dictionary
EXIT = '-1'                   # Controls when to stop the loop


def main():
    """
    TODO:
    """

    while True:
        print('Welcome to stanCode \"Anagram Generator\" (or -1 to quit)')
        s = input('Find anagrams for: ')
        start = time.time()
        if s != EXIT:
            print('Searching...')
            lst = find_anagrams(s)
            print(len(lst), 'anagrams: ', lst)
        else:
            break
        end = time.time()
        print('----------------------------------')
        print(f'The speed of your anagram algorithm: {end-start} seconds.')


def read_dictionary():
    # lst = {}
    lst = set()
    with open(FILE, 'r') as f:
        for line in f:
            lst.add(line.strip())
    return lst

    # lst = []
    # with open(FILE, 'r') as f:
    #     for line in f:
    #         lst.append(line.strip())
    # return lst


def find_anagrams(s):
    """
    :param s:
    :return:
    """
    dict_lst = read_dictionary()
    lst = find_anagrams_helper(s, '', dict_lst, [], [])
    return lst


def find_anagrams_helper(s, word, dct_list, lst, index_lst):
    if len(word) == len(s):
        if word in lst:
            pass
        else:
            if word in dct_list:
                print('Found: ', word)
                print('Searching...')
                lst.append(word)
                return lst
    else:
        for i in range(len(s)):
            if i not in index_lst:
                index_lst.append(i)
                word += s[i]
                # if word_determinator(word, s):
                if has_prefix(word, dct_list):
                    find_anagrams_helper(s, word, dct_list, lst, index_lst)
                index_lst.pop()
                word = word[:-1]
    return lst


def word_determinator(word, s):
    for i in word:
        if word.count(i) <= s.count(i):
            pass
        else:
            return False
    return True


def has_prefix(sub_s, dct_lst):
    """
    :param sub_s:
    :return:
    """
    for word in dct_lst:
        if word.startswith(sub_s):
            return True
    return False
    # dict_lst = read_dictionary()
    # return has_prefix_helper(sub_s, dict_lst)


def has_prefix_helper(sub_s, dct_lst):
    for word in dct_lst:
        if word.startswith(sub_s):
            return True
    return False


if __name__ == '__main__':
    main()
