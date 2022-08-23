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
        "CH3CH3OH + O2 --> CH3CO2H + H2O",
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
        first = r.reactant_formulas[0]
        second = r.reactant_formulas[-1]
        print(r.reactant_formulas)
        n1 = randint(1,100)
        n2 = randint(1,100)
        limiting = r.limiting_reagent(n1, n2)
        self.question = f"What is the limiting reagent in the reaction: {r.formula} \n Given I have {n1} grams of {first} and {n2} grams of {second}?"
        self.answer = limiting.formula
        self.reactions.remove(n)

class Flowchart(Question):
    #HCl = {"Descriptor": "Ppt", "Pb2+": "White ppt", "Ag+": "White ppt"}
    #Excess_NH3 = {"Ag+": "Ppt dissolves", "Pb2+": "Ppt doesnt dissolve"}
    #H2SO4 = {"Descriptor": "Ppt", "Ba2+": "White ppt", "Ca2+": "White ppt"}
    #NaOH = {"None": "No Ppt", "Mg2+": "White ppt", "Cu2+": "Blue ppt", "Fe2+": "Green Ppt", "Fe3+":"Brown ppt"}
    Tests = ["HCl" , "Excess_NH3","H2SO4","NaOH", "Flame"]
    Cations = ['Pb2+', 'Ag+', 'Ca2+', 'Ba2+', 'Mg2+', 'Fe2+', 'Fe3+', 'Cu2+']
    Pb2 = {'Identity': 'Pb2+','HCl' : True , 'H2SO4' : True, 'NaOH':True, 'Excess_NH3': True,"Flame":"N/A"}
    Ag =  {'Identity': 'Ag+','HCl':True, 'H2SO4':True,'NaOH':True, 'Excess_NH3': False}
    Ca2 = {'Identity': 'Ca2+','HCl':False, 'H2SO4':True,'NaOH': False, 'Excess_NH3': False,"Flame":"Brick Red"}
    Ba2 = {'Identity': 'Ba2+','HCl':False, 'H2SO4':True,'NaOH': False, 'Excess_NH3': False, "Flame":"Apple Green"}
    Mg2 = {'Identity': 'Mg2+','HCl':False, 'H2SO4':False,'NaOH': "White ppt", 'Excess_NH3': "White ppt","Flame":"White"}
    Fe2 = {'Identity': 'Fe2+','HCl':False, 'H2SO4':False,'NaOH': "Green ppt", 'Excess_NH3': "Green ppt", "Flame":"N/A"}
    Fe3 = {'Identity': 'Fe3+','HCl':False, 'H2SO4':False,'NaOH': "Brown ppt", 'Excess_NH3': "Brown ppt","Flame":"N/A"}
    Cu2 = {'Identity': 'Cu2+','HCl':False, 'H2SO4':False,'NaOH': "Blue ppt", 'Excess_NH3': "Blue ppt","Flame":"N/A"}
    Properties = [Pb2,Ag,Ca2,Ba2,Mg2,Fe3,Fe2,Cu2]
    cation = None

    def __init__(self,question,answer):
        super().__init__(question, answer)
    def create(self):
        self.cation = choice(self.Properties)
        self.question = f"Use a series of tests to identify the unknown cation.\n Possible cations: {self.Cations}\n Possible tests:\n"
        for i in range(len(self.Tests)):
           self.question += f"({i+1}) {self.Tests[i]}\n"
        self.answer = self.cation['Identity']
        print(self.answer)
        self.Properties.remove(self.cation)
    def check(self):
        limit = 4
        print(self.question)
        for i in range(limit):
            response = input(f'Guesses Remaining ({limit-i}): ')
            if response.isdigit() and int(response) > 0 and int(response) < len(self.Tests)+1:
                answer = self.Tests[int(response)-1]
                if self.cation[answer] == False:
                    print("No ppt")
                elif self.cation[answer] == True:
                    print("White ppt")
                else:
                    print(self.cation[answer])
            elif response == self.answer:
                print("Correct")
                break
            else:
                print("Invalid test and/or incorrect answer")

        #while response in self.cation:
            #print (self.cation[response])
            #response = input(self.question)
            #if response == str(self.answer):
                #print("Correct")
            #else:
                #print("Invalid test and/or incorrect answer")

q = Flowchart("Question","Answer")
q.create()
q.check()
#while q.check(input(q.question)) != "Correct":