import os
from datetime import datetime
import urllib2
from bs4 import BeautifulSoup
import re
import sys


zodiacs = [(120, 'Capricorn'), (218, 'Aquarius'), (320, 'Pissces'), (420, 'Aries'), (521, 'Taurus'),
           (621, 'Gemini'), (722, 'Cancer'), (823, 'Leo'), (923, 'Virgo'), (1023, 'Libra'),
           (1122, 'Scorpion'), (1222, 'Sagitarius'), (1231, 'Capricorn')]

def get_zodiac_of_date(date):
    date_number = int("".join((str(date.date().month), '%02d' % date.date().day)))
    for z in zodiacs:
        if date_number <= z[0]:
            return z[1]

def horoscope(sign):
    url = 'http://my.horoscope.com/astrology/free-daily-horoscope-%s.html' % sign
    html_doc = urllib2.urlopen(url)
    soup = BeautifulSoup(html_doc.read())
    text = soup.find_all(id="textline")[1].get_text()
    date = soup.find_all(id='advert')[1].get_text()
    print "%s - %s\n\n%s" % (sign.capitalize(), date, text)

date = raw_input('What\'s your birth date ? (Format input dd/mm/aaaa): ')
zod =  get_zodiac_of_date(datetime.strptime(date,"%d/%m/%Y"))

horoscope(zod)


