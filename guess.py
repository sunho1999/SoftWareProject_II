import hangman
class Guess:

    def __init__(self, word):
        self.secretWord = word
        self.guessedChars = []
        self.numTries = 0
        self.current_val = []
        self.sc = self.secretWord
        for d in range(len(self.secretWord)):
            self.current_val.append('_')
        self.currentStatus = 0




    def display(self):
        print(self.current_val)
        print("Tries :",self.numTries)


    def guess(self, character):
#       character는 입력된 문자값
        self.guessedChars.append(character)
        sw = 0
        for i in self.sc:
            char_index = self.secretWord.find(character) #제거할 값의 인덱스
            cur_val = self.secretWord[char_index] #제거할 값
            if character in i:
                self.secretWord = self.secretWord.replace(cur_val, "*",1)
                self.current_val[char_index] = cur_val
                sw = 1
        if sw == 0:
            self.numTries += 1

        if "_" in self.current_val:
            pass
        else:
            return True
        if self.numTries >= 6:
            return False
        self.currentStatus = str(self.current_val)




