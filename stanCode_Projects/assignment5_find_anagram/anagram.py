"""
File: anagram.py
Name: Ashton Yang
----------------------------------
This program recursively finds all the anagram(s)
for the word input by user and terminates when the
input string matches the EXIT constant defined
at line 28

If you correctly implement this program, you should see the
number of anagrams for each word listed below:
    * arm -> 3 anagrams
    * contains -> 5 anagrams
    * stop -> 6 anagrams
    * tesla -> 10 anagrams
    * spear -> 12 anagrams
"""


# 還沒想到has_prefix寫法
# input為'contains'時跑超慢...


import time                   # This file allows you to calculate the speed of your algorithm

# Constants
FILE = 'dictionary.txt'       # This is the filename of an English dictionary
EXIT = '-1'                   # Controls when to stop the loop


def main():
    lst = []                  # stores the input(which is a string) after it's converted into a list
    counts = {}               # counts the token in the above lst
    current_lst = []          # empty list
    ans = ''                  # empty string
    lst_of_anagram = []       # list of all anagrams
    print('Welcome to stanCode ''Anagram Generator'' (or -1 to quit)')
    word = input('Find anagrams for: ')
    start = time.time()

    if word is EXIT:
        pass
    else:
        dictionary_txt = read_dictionary()
        convert_to_lst_and_dict(word, lst, counts)
        find_anagrams(lst, counts, current_lst, ans, lst_of_anagram, dictionary_txt)

        num_of_anagrams = 0
        for i in lst_of_anagram:
            num_of_anagrams += 1
        print(num_of_anagrams, 'anagrams: ', lst_of_anagram)

    end = time.time()
    print('----------------------------------')
    print(f'The speed of your anagram algorithm: {end-start} seconds.')


def read_dictionary():
    dict_txt = []
    with open(FILE, 'r') as f:
        for line in f:                                 # line is a string
            tokens = line.split()                      # split() turns string into list (using space as delimiter)
            for token in tokens:                       # tokens are the elements in the list
                token = string_manipulation(token)     # after manipulation token's  a string with only alphabets/digits
                dict_txt.append(token)                 # append the token to the dict_txt (which is a list)
    return dict_txt                                    # return the list


def string_manipulation(token):
    ans = ''
    for ch in token:
        if ch.isalpha() or ch.isdigit():
            ans += ch
    return ans                                         # ans is a string


def convert_to_lst_and_dict(word, lst, counts):
    # creates a list containing the input word         # eg. word = 'stop'
    for ch in word:
        lst.append(ch)                                 # lst = ['s', 't', 'o', 'p']
    # counts the token in the list by creating key-value pairs in the 'counts' dictionary
    for token in lst:
        if token in counts:
            counts[token] += 1
        else:
            counts[token] = 1                          # counts = {'s':1, 't':1, 'o':1, 'p':1}


def find_anagrams(lst, counts, current_lst, ans, lst_of_anagram, dictionary_txt):
    # base case
    if len(lst) == len(current_lst):                   # eg. current_lst = ['p', 'o', 's', 't']
        for word in current_lst:
            ans += word                                # ans = 'post'
        if ans not in lst_of_anagram and ans in dictionary_txt:
            print('Searching...')
            print('Found: ', ans)
            lst_of_anagram.append(ans)                 # lst_of_anagram = ['post']
    # recursive
    else:
        for alphabet in lst:
            if counts[alphabet] > 0:
                current_lst.append(alphabet)
                counts[alphabet] -= 1
                find_anagrams(lst, counts, current_lst, ans, lst_of_anagram, dictionary_txt)
                counts[current_lst[len(current_lst)-1]] += 1
                current_lst.pop()


def has_prefix(sub_s, dictionary_txt):
    pass
    # for str in dictionary_txt:
    #     if str.startswith(sub_s):
    #         return True


if __name__ == '__main__':
    main()
