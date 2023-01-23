"""
File: class_reviews.py
Name:
-------------------------------
At the beginning of this program, the user is asked to input
the class name (either SC001 or SC101).
Attention: your input should be case-insensitive.
If the user input "-1" for class name, your program would show
the maximum, minimum, and average among all the inputs.
"""


def main():
    """
    期末評分計算程式
    """
    SC001_max = 0
    SC001_min = float('inf')
    SC001_total = 0
    SC101_max = 0
    SC101_min = float('inf')
    SC101_total = 0
    SC001 = 0 # 判斷SC001有幾筆資料
    SC101 = 0 # 判斷SC101有幾筆資料
    first_input = 0 #判斷是否第一次就輸入-1


    while True:

        classnum = input('Which class? ')

        if classnum == '-1':
            print('No class scores were entered')
            break

        score = input('score: ')
        score = int(score)

        if classnum.upper() == 'SC001':
            first_input = 1
            SC001 += 1
            SC001_total += score
            if SC001_max < score:
                SC001_max = score
            if SC001_min > score:
                SC001_min = score

        if classnum.upper() == 'SC101':
            first_input = 1
            SC101 += 1
            SC101_total += score
            if SC101_max < score:
                SC101_max = score
            if SC101_min > score:
                SC101_min = score

    if first_input == 0:
        pass

    else:
        print('=============SC001=============')
        if SC001 == 0:
            print('No score for SC001')
        else:
            print('MAX (001): ', SC001_max)
            print('MIN (001): ', SC001_min)
            print('Avg (001): ', SC001_total / SC001)

        print('=============SC101=============')
        if SC101 == 0:
            print('No score for SC101')
        else:
            print('MAX (101): ', SC101_max)
            print('MIN (101): ', SC101_min)
            print('Avg (101): ', SC101_total / SC101)

# ---- DO NOT EDIT CODE BELOW THIS LINE ---- #

if __name__ == '__main__':
    main()
