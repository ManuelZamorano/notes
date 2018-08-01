#!/usr/bin/python
import datetime


def main():
    i = datetime.datetime.now()
    note3_str = input('Enter note: ')
    
    print(i.strftime("%Y-%m-%d %H:%M:%S") + '-' + note3_str + '\n')
    f = open('notes.txt' , 'a')
    f.write(i.strftime("%Y-%m-%d %I:%M:%S %p") + ' - ' + note3_str + '\n')
    f.close()    
main()

