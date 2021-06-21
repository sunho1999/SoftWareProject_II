from math import factorial as fact

romans = [
        (1000, 'M'), (900, 'CM'), (500, 'D'), (400, 'CD'),
         (100, 'C'),  (90, 'XC'),  (50, 'L'),  (40, 'XL'),
          (10, 'X'),   (9, 'IX'),   (5, 'V'),   (4, 'IV'),
           (1, 'I')
    ]
def factorial(numStr):
    try:
        n = int(numStr)
        r = str(fact(n))
    except:
        r = 'Error!'
    return r

def decToBin(numStr):
    try:
        n = int(numStr)
        r = bin(n)[2:]
    except:
        r = 'Error!'
    return r

def binToDec(numStr):
    try:
        n = int(numStr, 2)
        r = str(n)
    except:
        r = 'Error!'
    return r

def decToRoman(numStr):
    try:
        n = int(numStr)
    except:
        return 'Error!'
    
    if n>= 4000:
        return 'Error!'

    result = ''
    for value, letters in romans:
        while n >= value:
            result += letters
            n -= value
    
    return result



def romanToDec(numStr):
    n = 0
    for i in romans:
        if numStr.find('CM') != -1:
            n += 900
            numStr = numStr.replace('CM', "")
        elif numStr.find('CD') != -1:
            n += 400
            numStr = numStr.replace('CD', "")
        elif numStr.find('XC') != -1:
            n += 90
            numStr = numStr.replace('XC', "")
        elif numStr.find('XL') != -1:
            n += 40
            numStr = numStr.replace('XL', "")
        elif numStr.find('IX') != -1:
            n += 9
            numStr = numStr.replace('IX', "")
        elif numStr.find('IV') != -1:
            n += 4
            numStr = numStr.replace('IX', "")
        else:
            for value1, letter1 in romans:
                if len(numStr) == 0:
                    return n
                if letter1 == numStr[0]:
                    n += value1
                    numStr = numStr[1:len(numStr)]


