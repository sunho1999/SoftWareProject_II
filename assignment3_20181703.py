import pickle
dbfilename = 'test3_4.dat'
def readScoreDB():
    try:
        fH = open(dbfilename, 'rb')
    except FileNotFoundError as e:
        print("New DB: ", dbfilename)
        return []

    scdb = []
    try:
        scdb =  pickle.load(fH)
    except:
        print("Empty DB: ", dbfilename)
    else:
        print("Open DB: ", dbfilename)
    fH.close()
    return scdb

# write the data into person db
def writeScoreDB(scdb):
    fH = open(dbfilename, 'wb')
    pickle.dump(scdb, fH)
    fH.close()

def doScoreDB(scdb):
    while(True):
        inputstr = (input("Score DB > "))
        if inputstr == "": continue
        parse = inputstr.split(" ")
        if parse[0] == 'add':
            try: 
                if parse[2].isdigit() and parse[3].isdigit():
                    record = {'Name':parse[1], 'Age':parse[2], 'Score':parse[3]}
                    scdb += [record]
                else:
                    print("나이와 점수는 숫자여야 합니다.")
            except IndexError:
                print("값은 이름, 나이, 점수 순으로 정확히 입력하세요")
        elif parse[0] == 'del': 
            try:
                for p in scdb:
                    if p['Name'] == parse[1]:
                        scdb.remove(p)
            except IndexError:
                print("값을 정확히 입력하세요.")
        elif parse[0] == 'show':
            try:
                sortKey ='Name' if len(parse) == 1 else parse[1]
                showScoreDB(scdb, sortKey)
            except:
                print("값을 정확히 입력해주세요")
        elif parse[0] == 'find':
            try:
                for i in scdb:
                    if i['Name'] == parse[1]:
                        print(i)
            except IndexError:
                print('값을 정확히 입력해주세요.')
        elif parse[0] == 'inc':
            count = 0
            try:
                if parse[2].isdigit():
                    for i in scdb:
                        if i['Name'] == parse[1]:
                            inc_value = scdb[count]['Score']
                            inc_value = int(inc_value) + int(parse[2])
                        i += 1
                else:
                    print("정수만 더할 수 있습니다.")
            except IndexError:
                print("값을 정확히 입력하세요.")
        elif parse[0] == 'quit':
            break  
        else:
            print("Invalid command: " + parse[0])


def showScoreDB(scdb, keyname):
    for p in sorted(scdb, key=lambda person: person[keyname]):
        for attr in sorted(p):
            print(attr + "=" + p[attr], end=' ')
        print()


scoredb = readScoreDB()
doScoreDB(scoredb)
writeScoreDB(scoredb)
