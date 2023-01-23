"""
File: coin_flip_runs.py
Name:
-----------------------
This program should simulate coin flip(s)
with the number of runs input by users.
A 'run' is defined as consecutive results
on either 'H' or 'T'. For example, 'HHHHHTHTT'
is regarded as a 2-run result.
Your program should stop immediately after your
coin flip results reach the number of runs!
"""

import random as r
import sys

def main():
	"""
	TODO:
	"""
	temp_T = 0
	temp_H = 0
	print('Let\'s filp a coin!')
	target = input('Number of runs: ')
	num = 0

	while True:
		temp = r.random()
		temp

		if temp <= 0.5:
			temp_T += 1
			temp_H = 0
			sys.stdout.write("H")

		else:
			temp_H += 1
			temp_T = 0
			sys.stdout.write("T")

		if temp_T == 2:
			num += 1

		if temp_H == 2:
			num += 1

		if num == int(target):
			break

# ---- DO NOT EDIT CODE BELOW THIS LINE ---- #

if __name__ == "__main__":
	main()
