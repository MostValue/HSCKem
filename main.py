from random import choice, randint
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

class MassPercent(Question):
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


class LimitingReagent(Question):
    reactions = [
        "N2O5 + H2O --> HNO3",
        "CO2 + H2O --> O2 + C6H12O6",
        "H2 + O2 --> H2O",
        "Ca + CO3 --> CaCO3",
        "H2 + N2 --> NH3",
        "CH3CH3OH + O2 --> CH3COOH + H2O",
        "CH4 + O2 --> H2O + CO2",
    ]

    def __init__(self,question,answer):
        super().__init__(question, answer)

    def create(self):
        n = choice(self.reactions)
        print(n)
        r = Reaction.by_formula(n)
        print(r)
        r.balance()
        first = r.reactant_formulas[1]
        second = r.reactant_formulas[2]
        n1 = randint(1,100)
        n2 = randint(1,100)
        limiting = r.limiting_reagent(n1, n2)
        self.question = f"What is the limiting reagent in the reaction: {r.formula} \n Given I have {n1} grams of {first} and {n2} grams of {second}?"
        self.answer = limiting.formula
        self.reactions.remove(n)


q = LimitingReagent("Question","answer")
q.create()
print(q.check(input(q.question)))
print(q.answer)
