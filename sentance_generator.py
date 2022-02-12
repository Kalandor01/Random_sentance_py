"""
This module can generate sentances with a random length from a range of words, or just a bunch of random letters.\n
It also contains a function for writing text out letter by letter at a specifiable speed, and another function if you want to write out multy-line text at varying speeds easily.
"""
import random as r


def unstructured_random(min_len=1, max_len=1000):
    """
    Returns a random number of random letters (and simbols).
    """
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ' ]
    text = ""
    num = r.randint(min_len, max_len)
    for _ in range(num):
        text += letters[r.randint(0, len(letters) - 1)]
    return text


def get_next_word(words, sentance_structure, type_pre=0):
    """
    Returns the next random word, and it's type from the previous word type, according to the sentance structure array, and a 2D array of posible words.
    """
    type_num = r.randint(0, len(sentance_structure[type_pre]) - 1)
    word_type = sentance_structure[type_pre][type_num]
    word = words[word_type][r.randint(0, len(words[word_type]) - 1)]
    # input(f"{type_pre} {word_type}: {word}")
    return word_type, word


def structured_sentance(min_len=1, max_len=100):
    """
    Returns a random string that "tries" to match a sentance structure\n
    A Word length of 1 produces only a punctuation mark. (0 produces nothing)
    """
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

    text = "" 
    sentance_length = r.randint(min_len, max_len)
    if sentance_length > 0:
        if sentance_length > 1:
            type_pre, word = get_next_word(words, sentance_structure, 7)
            text += word.replace(" ", "").capitalize()
            for _ in range(sentance_length - 2):
                type_pre, word = get_next_word(words, sentance_structure, type_pre)
                text += word
        text += get_next_word(words, sentance_structure, 6)[1]
    return text


# SENTANCE STRUCTURE
"""
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


def typewriter(text="", speed=4, is_speed_delay=True):
    """
    Writes out text like a typewriter with end="".\n
    Returns "" so it can be easily inserted into text.\n
    Speed controlls how long should it wait between writing out two letters in millisecond.\n
    If is_speed_delay is False, speed is how many seconds it should take to write out the entire text.\n
    """
    import time

    if is_speed_delay:
        for letter in text:
            print(letter, end="", flush=True)
            time.sleep(speed / 1000)
    else:
        for letter in text:
            print(letter, end="", flush=True)
            time.sleep(speed / len(text))
    return ""


def meta_typewriter(texts=[["Example ", 0.1], ["text!\nNewline!", 2]]):
    """
    Writes out multiline texts using the typewriter function.\n
    Accepts a list of texts that should have different speeds, and/or timing styles.\n
    [TEXT, SPEED, IS_SPEED_DELAY]\n
    If speed is not specified it asumes 4.
    If is_speed_delay is not specified it asumes True.
    """
    def_speed = 4
    def_delay_type = True
    for text in texts:
        if text != []:
            if len(text) == 1:
                text = [text[0], def_speed, def_delay_type]
            elif len(text) == 2:
                if type(text[1]) == int:
                    text.append(def_delay_type)
                else:
                    text = [text[0], def_speed, text[1]]
            typewriter(text[0], text[1], text[2])
        else:
            print("TEXT ERROR!")


def default_run():
    seed = r.randint(-1000000000, 1000000000)
    ans = input("Seed?: ")
    if ans != "":
        seed = int(ans)
    else:
        print(f"Seed: {seed}")
    r.seed(seed)

    ans = input("Random?(Y/N): ")
    if ans.upper() == "Y":
        input(unstructured_random(1, 1000))
    else:
        input(structured_sentance(2, 2))

# -231822330	sentance(2, 2)
# default_run()
# meta_typewriter([["Hello!\nWellcome!\nGood Morning!\n", 1, False], ["How are...", 1, False], ["YOU!!!\n", 1.5, False]])
