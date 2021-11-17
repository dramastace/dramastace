from random import randint

def verb():
    words = ["ran", "walked", "refered", "embarked on", "regulated", "murdered",
             "touched", "highlighted", "expressed", "showed", "counted", "borrowed",
             "isolated", "prayed", "split", "interviewed", "suggested", "classified",
             "offered", "helped", "tackled", "revealed", "smashed", "posed", "pressed",
             "swung", "granted", "engaged", "began", "benefited", "boiled", "shot",
             "deposited", "quoted", "sucked", "leaded", "armed", "chased", "climbed", "shipped",
             "fulfilled", "disagreed", "blocked", "sent", "earned", "pointed", "predicted"]
    
    index = randint(0, len(words)-1)
    return words[index]

def noun():
    words = ["property", "version", "mud", "statement", "cabinet", "apple",
             "foundation", "chapter", "information", "funeral","difficulty",
             "salad", "permission", "phone", "system", "opportunity", "selection",
             "combination", "supermarket", "heart", "dirt", "performance",
             "membership", "quantity", "possibility", "protection", "personality",
             "clothes", "insect", "economics", "steak", "director", "midnight",
             "percentage", "surgery", "manufacturer", "tradition", "office",
             "advice", "union", "death", "government", "management", "meth",
             "movie", "chocolate", "cancer", "airport", "way", "variation"]
    
    index = randint(0, len(words)-1)
    return words[index]

def adverb():
    words = ["fortunately", "more", "anxiously", "monthly", "truthfully",
             "yawningly", "carefully", "initially", "questionably", "loyally",
             "voluntarily", "almost", "wrongly", "abnormally", "positively",
             "enormously", "perfectly", "warmly", "frankly", "similarly",
             "separately", "fatally", "sweetly", "certainly"]
    
    index = randint(0, len(words)-1)
    return words[index]

def det():
    words = ["the", "a", "that", "this"]
    
    index = randint(0, len(words)-1)
    return words[index]

def pronoun():
    words = ["he", "she", "it", "they"]
    
    index = randint(0, len(words)-1)
    return words[index]

def adj():
    words = ["scintillating", "disgusted", "makeshift", "thirsty", "scary", "legal",
             "chunky", "curly", "woozy", "parallel", "lopsided", "low",
             "odd", "gaudy", "outstanding", "impossible", "loud", "clever",
             "rabid", "complete", "lively"]
    
    index = randint(0, len(words)-1)
    return words[index]

def name():
    words = ["McD", "Sabrina", "Amanda", "Steve", "Ericka", "Staci", "Tyree", "Rose", "Olivia"]
    
    index = randint(0, len(words)-1)
    return words[index]

print(name() + " " + verb() + " " + det() + " " + noun() + " " + adverb() +
      " and no one " + verb() + " " + det()  + " " + adj()+ " " + noun() +
      " more than " + name () + ".")
print(name() + " was " + adj() + " and now is " + adj() + " but " + adverb() +
      " " + pronoun() + " is not a " + noun()+".")
