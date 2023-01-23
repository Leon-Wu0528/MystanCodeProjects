"""
File: webcrawler.py
Name: 
--------------------------
This file collects more data from
https://www.ssa.gov/oact/babynames/decades/names2010s.html
https://www.ssa.gov/oact/babynames/decades/names2000s.html
https://www.ssa.gov/oact/babynames/decades/names1990s.html
Please print the number of top200 male and female on Console
You should see:
---------------------------
2010s
Male number: 10895302
Female number: 7942376
---------------------------
2000s
Male number: 12976700
Female number: 9208284
---------------------------
1990s
Male number: 14145953
Female number: 10644323
"""

import requests
from bs4 import BeautifulSoup


def main():
    for year in ['2010s', '2000s', '1990s']:
        print('---------------------------')
        print(year)
        url = 'https://www.ssa.gov/oact/babynames/decades/names'+year+'.html'
        
        response = requests.get(url)
        html = response.text
        soup = BeautifulSoup(html)

        # ----- Write your code below this line ----- #

        tags = soup.find_all('table', {'class': 't-stripe'})
        male_num = 0
        female_num = 0
        for tag in tags:
            n = 0
            rank = 1
            for tr in tag.tbody:
                if rank <= 200:
                    if n % 2 != 0:  # 排除掉基數行 剩有排名的lst
                        lst = tr.text.split()
                        n += 1
                        rank += 1
                        num_male = ''
                        num_female = ''
                        for i in lst[2]:  # 將有comma的字串轉成數字
                            if i != ',':
                                num_male += i
                        for i in lst[4]:  # 將有comma的字串轉成數字
                            if i != ',':
                                num_female += i
                        male_num += int(num_male)
                        female_num += int(num_female)
                    else:
                        n += 1

                else:
                    break

        print('Male Number:', male_num)
        print('Female Number:', female_num)


if __name__ == '__main__':
    main()
