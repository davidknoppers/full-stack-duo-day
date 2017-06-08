#!/usr/bin/python3
from bs4 import BeautifulSoup
import requests
import sys
import re
#dependency: sudo pip3 install bs4
# usage: ./horoscope [your sign]


def get_horoscope(sign):
    url = "https://www.horoscope.com/us/horoscopes/general/horoscope-general-daily-today.aspx?sign=" + sign
    r = requests.get(url)
    soup = BeautifulSoup(r.text, 'html.parser')
    mydivs = soup.findAll('div', attrs={'class': "horoscope-content"})[0]
    result = mydivs.get_text()
    print(result.split('\n')[2])


def get_elle_horoscope(sign):
    url = "http://www.elle.com/horoscopes/daily/a98/{}-daily-horoscope/".format(sign.lower())
    r = requests.get(url)
    soup = BeautifulSoup(r.text, 'html.parser')
    print(soup.find('p', attrs={'class': "body-el-text standard-body-el-text"}).get_text())


if __name__ == "__main__":
    if len(sys.argv) < 1 :
        print("usage: ./horoscope [your sign]")
    elif not isinstance(sys.argv[1], str):
        print("usage: ./horoscope [your sign]")
    else:
        sign = sys.argv[1].lower()
        horoscopes = {"aries": "1", "taurus": "2", "gemini": "3", "cancer": "4",
                      "leo": "5", "virgo": "6", "libra": "7", "scorpio": "8",
                      "sagittarius": "9", "capricorn": "10", "aquarius": "11",
                      "pisces": "12"}
        if sign not in horoscopes.keys():
            print("not a recognized sign")
        else:
            print("first horoscope")
            get_horoscope(horoscopes[sign])
            print("")
            print("second horoscope")
            get_elle_horoscope(sign)
