import random

determiners = ["The", "One", "A", "Some" ]
nouns = ["boy", "girl", "cat", "dog", "bird", "house"]
verbs = ["laughed", "thought", "eats", "runs", "thinks", "writes"]

def main():
    '''Makes a randomly generated sentence and prints it.'''
    print(make_sentence())

def get_determiner(quantity):
    """Return a randomly chosen determiner. A determiner is
    a word like "the", "a", "one", "some", "many".
    If quantity is 1, this function will return either "a",
    "one", or "the". Otherwise this function will return
    either "some", "many", or "the".

    Parameter
        quantity: an integer.
            If quantity is 1, this function will return a
            determiner for a single noun. Otherwise this
            function will return a determiner for a plural
            noun.
    Return: a randomly chosen determiner.
    """
    if quantity == 1:
        words = ["a", "one", "the"]
    else:
        words = ["some", "many", "the"]

    # Randomly choose and return a determiner.
    word = random.choice(words)
    return word




    








def make_sentence():
    '''Assembles the sentence from the random words'''
    determiner = random_determiner()
    noun = random_noun()
    verb = random_verb()
    sentence = f"{determiner} {noun} {verb}"
    return sentence

main()