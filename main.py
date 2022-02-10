import random as r


def unstructured_random(min_len=1, max_len=1000):
    """""
    Returns a random number of random letters (and simbols).
    """
    text = ""
    num = r.randint(min_len, max_len)
    for _ in range(num):
        text += letters[r.randint(0, len(letters) - 1)]
    return text


def get_next_word(type_pre=0):
    """""
    Returns the next random word, and it's type from the previous word type, according to the sentance structure array.
    """
    global sentance_structure
    global words
    type_num = r.randint(0, len(sentance_structure[type_pre]) - 1)
    word_type = sentance_structure[type_pre][type_num]
    word = words[word_type][r.randint(0, len(words[word_type]) - 1)]
    # input(f"{type_pre} {word_type}: {word}")
    return word_type, word


def structured_sentance(min_len=1, max_len=100):
    """""
    Returns a random string that "tries" to match a sentance structure\n
    A Word length of 1 produces only a punctuation mark. (0 produces nothing)
    """
    text = "" 
    sentance_length = r.randint(min_len, max_len)
    if sentance_length > 0:
        if sentance_length > 1:
            type_pre, word = get_next_word(7)
            text += word.replace(" ", "").capitalize()
            for _ in range(sentance_length - 2):
                type_pre, word = get_next_word(type_pre)
                text += word
        text += get_next_word(6)[1]
    return text

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ' ]
w_thing = [" car", " cat", " ice cream", " building", " house", " freezer", " doll", " art", " computer", " code", " table", " chair", " mouse", " keyboard", " monitor", " processor", " ram", " fruit", " vegetable", " desk", " pen", " pencil", " gun", " death", " paint", " brush"]
w_do = [" eat", " give", " take", " do", " make", " destroy", " code", " can", " slap", " kick", " leave", " go", " morn", " capture", " run", " walk", " jog", " climb"]
w_adj = [" cute", " nice", " wrong", " medium", " big", " small", " hairy", " fat", " fast", " slow", " easy", " hard"]
w_who = [" I", " you", " he", " she", " it", " they", " them", " her", " his", " me", " this", " that"]
w_ask = [" who", " when", " why", " where", " what", " are", " is"]
w_end = [".", "!", "?", "?!", "!?", " :)", " :(", " :D", " :C", " XD", "", "..."]
w_between = [" a", " an", " is", " the", " with", " at", " on", " in", " are", " have"]
# thing     do      adjective     who      ask     between    end      beginning
words = [w_thing, w_do, w_adj, w_who, w_ask, w_between, w_end]
sentance_structure = [[5], [0, 2, 5], [0], [1, 5], [3, 5], [0, 2, 3], [-1], [1, 3, 4, 5]]

# SENTANCE STRUCTURE
"""""
    thing   =   0
    do      =   1
    adj     =   2
    who     =   3
    ask     =   4
    between =   5
    (end    =   6)
    (beggining= 7)
    
    STRUCTURE:

    thing:
        -between
    
    do:
        -thing
        -adj
        -between

    adj:
        -thing
    
    who:
        -do
        -between
    
    ask:
        -who
        -between
    
    between:
        -thing
        -adj
        -who
"""

# seed
seed = r.randint(-1000000000, 1000000000)
ans = input("Seed?: ")
if ans != "":
    seed = int(ans)
else:
    print(f"Seed: {seed}")
r.seed(seed)

ans = input("Random?(Y/N): ")
# very random
if ans.upper() == "Y":
    input(unstructured_random(1, 1000))
else:   
    input(structured_sentance(1, 100))
