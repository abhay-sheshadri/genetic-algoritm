import random
import string

phrase = "geneticevolution"


class Population(object):

    def __init__(self, phrase, number, variation):
        self.phrase = phrase
        self.length = len(phrase)
        self.size = number
        self.generation = 1
        self.variation = variation / 100
        self.members = []
        self.generateNLengthStrings()

    def generateNLengthStrings(self):
        for i in range(self.size):
            word = ""
            for x in range(self.length):
                word += random.choice(list(string.ascii_lowercase))
            self.members.append(word)

    def evolve(self):
        scores = []
        score_to_word = {}
        for word in self.members:
            word_score = self.score(word)
            score_to_word[word_score] = word
            scores.append(word_score)
        max_val = max(scores)
        scores.remove(max_val)
        sec_val = max(scores)
        self.members = []
        for i in range(self.size):
            new_member = ""
            for x in range(self.length):
                new_member += random.choice([score_to_word[max_val][x], score_to_word[sec_val][x]])
            self.members.append(new_member)
        self.mutate()

    def score(self, word):
        word_score = 0
        for i in range(self.size):
            if word[i] == phrase[i]:
                word_score += 1
        return word_score

    def mutate(self):
        for member in range(self.size):
            for i in range(self.length):
                if random.random() < self.variation:
                    new = self.members[member][:i] + random.choice(list(string.ascii_lowercase)) + self.members[member][i+1:]
                    self.members[member] = new


population = Population(phrase, 10, 1)
while phrase not in population.members:
    print(str(population.members)[1:-1])
    population.evolve()

print(str(population.members)[1:-1])
