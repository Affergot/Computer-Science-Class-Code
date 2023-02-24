from math import comb
from CharByChar import *

charByChar("How many types of cookies are there?\n:")
num_cookie_types = int(input())
charByChar("How many cookies do you want to choose?\n:")
num_cookies_to_choose = int(input())

possible_combinations = comb(num_cookie_types, num_cookies_to_choose)
# + num_cookies_to_choose - 1
charByChar(f"There are {possible_combinations} ways to choose {num_cookies_to_choose} cookies from {num_cookie_types} types of cookies.")
