from logic import *
rain = Symbol("rain")
hagrid = Symbol("Hagrid")
dumbledore = Symbol("Dumbledore")

knowledge = And(
    Implication(Not(rain), hagrid),
    Or(hagrid, dumbledore),
    Not(And(hagrid, dumbledore)),
    dumbledore
)

print(knowledge.formula())