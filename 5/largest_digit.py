"""
File: largest_digit.py
Name: 吳竹孟
----------------------------------
This file recursively prints the biggest digit in
5 different integers, 12345, 281, 6, -111, -9453
If your implementation is correct, you should see
5, 8, 6, 1, 9 on Console.
"""


def main():
	print(find_largest_digit(12345))      # 5
	print(find_largest_digit(281))        # 8
	print(find_largest_digit(6))          # 6
	print(find_largest_digit(-111))       # 1
	print(find_largest_digit(-9453))      # 9


def find_largest_digit(n):
	"""
	:param n:
	:return:
	"""
	n = abs(n)
	num = find_largest_digit_helper(n, 0)
	return num

	# 另一個寫法
	# n = abs(n)
	# last_digit = n % 10
	# second_last_digit = n // 10 % 10
	# if second_last_digit == 0:
	# 	return last_digit
	# elif second_last_digit > last_digit:
	# 	return find_largest_digit(n//10)
	# else:
	# 	return find_largest_digit(n // 10 - second_last_digit + last_digit)


def find_largest_digit_helper(n, num=0):
	# n = abs(n) 應該寫在上面 才不用重複跑
	if n != 0:
		if n - n // 10 * 10 > num:
			num = find_largest_digit_helper(n // 10, n - n // 10 * 10)
		else:
			num = find_largest_digit_helper(n // 10, num)
	return num


if __name__ == '__main__':
	main()
