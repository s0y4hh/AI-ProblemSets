from logic import *
"""JAYSON ASIADO BSCS 1A"""
AKnight = Symbol("A is a Knight")
AKnave = Symbol("A is a Knave")

BKnight = Symbol("B is a Knight")
BKnave = Symbol("B is a Knave")

CKnight = Symbol("C is a Knight")
CKnave = Symbol("C is a Knave")
"""In 1978, logician Raymond Smullyan published “What is the name of this book?”, a book of logical puzzles. Among the puzzles in the book were a class of puzzles that Smullyan called “Knights and Knaves” puzzles.

In a Knights and Knaves puzzle, the following information is given: Each character is either a knight or a knave. A knight will always tell the truth: if knight states a sentence, then that sentence is true. Conversely, a knave will always lie: if a knave states a sentence, then that sentence is false.

The objective of the puzzle is, given a set of sentences spoken by each of the characters, determine, for each character, whether that character is a knight or a knave.

For example, consider a simple puzzle with just a single character named A. A says “I am both a knight and a knave.”

Logically, we might reason that if A were a knight, then that sentence would have to be true. But we know that the sentence cannot possibly be true, because A cannot be both a knight and a knave – we know that each character is either a knight or a knave, but not both. So, we could conclude, A must be a knave.

That puzzle was on the simpler side. With more characters and more sentences, the puzzles can get trickier! Your task in this problem is to determine how to represent these puzzles using propositional logic, such that an AI running a model-checking algorithm could solve these puzzles for us."""
# Puzzle 0
# A says "I am both a knight and a knave."
knowledge0 = And(
        # A is a knight or a knave but not both:
    And(Or(AKnight, AKnave), Not(And(AKnight, AKnave))),
    # If A is a knight then what A says is true
    Implication(AKnight, And(AKnight, AKnave)),
    # If A is a knave his sentence is false
    Implication(AKnave, Not(And(AKnight, AKnave)))
)

    

# Puzzle 1
# A says "We are both knaves."
# B says nothing.
knowledge1 = And(
    # If A is a knight, A and B are both knaves:
    Implication(AKnight, And(AKnave, BKnave)),
    # If A is a knave, his statement is false:
    Implication(AKnave, Not(And(AKnave, BKnave))),
    # A and B are knights or knaves but never be both
    And(Or(AKnight, AKnave), Not(And(AKnight, AKnave))),
    And(Or(BKnight, BKnave), Not(And(BKnight, BKnave))),

    
)

# Puzzle 2
# A says "We are the same kind."
# B says "We are of different kinds."
knowledge2 = And(
    # If A is a knight, A and B are both the same
    Implication(AKnight, Or(And(AKnight, BKnight), And(AKnave, BKnave))),
    # If A is a knave, his statement is false
    Implication(AKnave, Not(Or(And(AKnight, BKnight), And(AKnave, BKnave)))),
    # If B is a knight, A and B are not the same
    Implication(BKnight, Or(And(AKnight, BKnave), And(AKnave, BKnight))),
    # If B is a knave, his statement is false
    Implication(BKnave, Not(Or(And(AKnight, BKnave), And(AKnave, BKnight)))),
        # A and B are knights or knaves but not both:
    And(Or(AKnight, AKnave), Not(And(AKnight, AKnave))),
    And(Or(BKnight, BKnave), Not(And(BKnight, BKnave))),
)

# Puzzle 3
# A says either "I am a knight." or "I am a knave.", but you don't know which.
# B says "A said 'I am a knave'."
# B says "C is a knave."
# C says "A is a knight."
knowledge3 = And(

    # If B is a knight, then C is a knave, and B says "A said:  'I am a knave'"
    Implication(BKnight, CKnave),
    Implication(BKnight, And(
      # A then said "Or 'I am a Knave" So A can be a Knight or A Knave
      Implication(AKnight, AKnave),
      Implication(AKnave, Not(AKnave)),
    )),
    # If B is a knave, A said 'I am a knight' C is not a knave
    Implication(BKnave, Not(CKnave)),
    Implication(BKnave, And(
      # A then said 'I am a Knight', A Can be a Knight or a Knave
      Implication(AKnight, AKnight),
      Implication(AKnave, Not(AKnight))
    )),
    # If C is a knight, A is a knight
    Implication(CKnight, AKnight),
    # If C is a knave, A is not a knight
    Implication(CKnave, Not(AKnight)),
        # A, B and C are knights or knaves but not both
    And(Or(AKnight, AKnave), Not(And(AKnight, AKnave))),
    And(Or(BKnight, BKnave), Not(And(BKnight, BKnave))),
    And(Or(CKnight, CKnave), Not(And(CKnight, CKnave))),
)


def main():
    symbols = [AKnight, AKnave, BKnight, BKnave, CKnight, CKnave]
    puzzles = [
        ("Puzzle 0", knowledge0),
        ("Puzzle 1", knowledge1),
        ("Puzzle 2", knowledge2),
        ("Puzzle 3", knowledge3)
    ]
    for puzzle, knowledge in puzzles:
        print(puzzle)
        if len(knowledge.conjuncts) == 0:
            print("    Not yet implemented.")
        else:
            for symbol in symbols:
                if model_check(knowledge, symbol):
                    print(f"    {symbol}")


if __name__ == "__main__":
    main()
