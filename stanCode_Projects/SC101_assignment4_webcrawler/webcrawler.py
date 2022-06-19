"""
File: webcrawler.py
Name: Ashton Yang
--------------------------
This file collects more data from
https://www.ssa.gov/oact/babynames/decades/names2010s.html
https://www.ssa.gov/oact/babynames/decades/names2000s.html
https://www.ssa.gov/oact/babynames/decades/names1990s.html
Please print the number of top200 male and female on Console
You should see:
---------------------------
2010s
Male Number: 10895302
Female Number: 7942376
---------------------------
2000s
Male Number: 12976700
Female Number: 9208284
---------------------------
1990s
Male Number: 14145953
Female Number: 10644323
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
        soup = BeautifulSoup(html, 'html.parser')

        # ----- Write your code below this line ----- #

        td = soup.find('tbody').text
        lst = td.split()
        # print(lst)
        boy_numbers = []
        for i in range(200):
            num = lst[2 + 5*i]
            int_ = int(num.replace(',', ''))
            boy_numbers.append(int_)
        # print(boy_number)
        boy_total = 0
        for boy_number in boy_numbers:
            boy_total += boy_number
        print('Male Number: ', boy_total)
        girl_numbers = []
        for j in range(200):
            num_2 = lst[4 + 5*j]
            int_2 = int(num_2.replace(',', ''))
            girl_numbers.append(int_2)
        girl_total = 0
        for girl_number in girl_numbers:
            girl_total += girl_number
        print('Female Number: ', girl_total)


if __name__ == '__main__':
    main()
