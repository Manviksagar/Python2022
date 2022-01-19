import configparser
import sys

con=configparser.RawConfigParser()
con.read(sys.path[1]+"\\configFiles\\config.ini")

#url=con['common']['baseURL']
url=con.get('common', 'baseURL')
print(url)
print(con.get('common','user'))
