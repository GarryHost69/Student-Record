import json
from pathlib import Path
from enum import Enum

class Subject(Enum):
    Math = 0
    SocialScience = 1
    Science = 2
    English = 3

def InsertRecord():
    try:
        Record = json.load(open('C:/users/garry/Desktop/StudentRecord/stdRec.txt'))
    except:
        Record = {}
    Name = {}
    Marks = {}
    Percentage = {}
    M = []
    per = 0
    rno = input("\nEnter Student's Roll Number : ")
    Name['Name'] = input("\nEnter Student's Name : ")
    for i in range(4):
        M.append(int(input('\nEnter Marks in ' + str(Subject(i).name) + ' : ')))
    for m in M:
        per += m
    per /= 4
    Marks['Marks'] = M
    Percentage['Percentage'] = per
    Record[rno] = Name, Marks, Percentage
    json.dump(Record, open('C:/users/garry/Desktop/StudentRecord/stdRec.txt', 'w'))
    print('\nRecord Inserted')

def PrintToppersList():
    try:
        rec = json.load(open('C:/users/garry/Desktop/StudentRecord/stdRec.txt'))
        mathTopper = next(iter(rec))
        socialScienceTopper = next(iter(rec))
        scienceTopper = next(iter(rec))
        englishTopper = next(iter(rec))
        for i in rec:
            for j in range(4):
                if j == 0:
                    if rec[i][1]['Marks'][j] > rec[mathTopper][1]['Marks'][j]:
                        mathTopper = i
                elif j == 1:
                    if rec[i][1]['Marks'][j] > rec[socialScienceTopper][1]['Marks'][j]:
                        socialScienceTopper = i
                elif j == 2:
                    if rec[i][1]['Marks'][j] > rec[scienceTopper][1]['Marks'][j]:
                        scienceTopper = i
                elif j == 3:
                    if rec[i][1]['Marks'][j] > rec[englishTopper][1]['Marks'][j]:
                        englishTopper = i
        print('\nMath Topper : ' + rec[mathTopper][0]['Name'])
        print('\nSocial Science Topper : ' + rec[socialScienceTopper][0]['Name'])
        print('\nScience Topper : ' + rec[scienceTopper][0]['Name'])
        print('\nEnglish Topper : ' + rec[englishTopper][0]['Name'])
    except:
        print('\n\nEmpty File. Enter a record first\n\n')

def PrintStudentRecord():
    try:
        rec = json.load(open('C:/users/garry/Desktop/StudentRecord/stdRec.txt'))
        print('\nRollNo    Name        Math    SocialScience    Science    English    Percentage')
        for i in rec:
            r = i
            n = rec[i][0]['Name']
            m = rec[i][1]['Marks']
            p = rec[i][2]['Percentage']
            print(r, '       ', n, '    ', '            '.join([str(ls) for ls in m]), '    ', p)
        print()
    except:
        print('\n\nEmpty File. Enter a record first\n\n')

while True:
    f = Path('C:/users/garry/Desktop/StudentRecord/stdRec.txt')
    if f.is_file():
        uc = int(input('\nPress 1 to veiw existing Student Record\nPress 2 to Add a record\nPress 3 to get the list of Toppers in each Subject\nPress 4 to exit the Program\n\nEnter Your Choice : '))
        if uc == 1:
            PrintStudentRecord()
        elif uc == 2:
            InsertRecord()
        elif uc == 3:
            PrintToppersList()
        elif uc == 4:
            exit()
    else:
        temp = open('C:/users/garry/Desktop/StudentRecord/stdRec.txt', 'w')
        temp.close()
