# your code goes here!
class Anagram:
    def __init__(self, word):
        self.word = word
    def match(self, possible_anagram):
        sorted_word = "".join(sorted(self.word)) 
        matches = []
        for possible in possible_anagram:
            if sorted_word =="".join(sorted(possible)):
             matches.append(possible)

        return matches