#!/usr/bin/python3
from bs4 import BeautifulSoup
import requests
import sys
import re
#dependency: sudo pip3 install bs4
# usage: ./horoscope [your sign]
def get_horoscope(sign):
    if not isinstance(sign, str):
        return ("usage: ./horoscope [your sign]")
    horoscopes = {"aries": "1", "taurus": "2", "gemini": "3", "cancer": "4",
                   "leo": "5", "virgo": "6", "libra": "7", "scorpio": "8",
                   "sagittarius": "9", "capricorn": "10", "aquarius": "11",
                   "pisces": "12"}
    if sign.lower() not in horoscopes.keys():
        return("not a recognized sign")
    url = "https://www.horoscope.com/us/horoscopes/general/horoscope-general-daily-today.aspx?sign=" + horoscopes[sign.lower()]
    r = requests.get(url)
    soup = BeautifulSoup(r.text, 'html.parser')
    mydivs = soup.findAll('div', attrs={'class': "horoscope-content"})[0]
    result = mydivs.get_text()
    return(result.split('\n')[2])
if len(sys.argv) > 1:
    print(get_horoscope(sys.argv[1]))
else:
    print("usage: ./horoscope [your sign]")
