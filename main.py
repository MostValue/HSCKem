from random import choice
from chemlib import *

class Question:
    def __init__(self, question, answer):
        self.question = question
        self.answer = answer
    def check(self, response):
        if response == str(self.answer):
            return "Correct"
        return "You're Dumb"
    def create(self):
        pass

class Mass(Question):
    compounds = ["H2O", "H2SO4", "Na2SO3", "Na2PO4"]

    def __init__(self,question,answer):
        super().__init__(question, answer)

    def create(self):
        x = choice(self.compounds)
        compound = Compound(x)
        element = choice(list(compound.occurences.keys()))
        self.question = f"What is the percentage composition of {element} in {x} to the nearest %?:"
        self.answer = round(compound.percentage_by_mass(element))
        self.compounds.remove(x)



q = Mass("Question","answer")
q.create()
print(q.check(input(q.question)))
print(q.answer)
