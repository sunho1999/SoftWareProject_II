import random

class Word:

    def __init__(self, filename, word_length):
        self.words = []
        self.word_length = word_length
        f = open(filename, 'r')
        lines = f.readlines()
        f.close()

        self.count = 0
        for line in lines:
            word = line.rstrip()
            self.words.append(word)
            self.count += 1
        print('%d words in DB' % self.count)


    def test(self):
        return 'default'


    def randFromDB(self):
        while True:
            r = random.randrange(self.count)
            if len(self.words[r]) <= self.word_length:
                return self.words[r]

