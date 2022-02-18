"""
This module can generate sentances with a random length from a range of words, or just a bunch of random letters.\n
It also contains a function for writing text out letter by letter at a specifiable speed and with a custom sound.
"""
__version__ = '1.3'

from numpy import random as npr
r = npr.RandomState()

def unstructured_random(min_len=1, max_len=1000):
    """
    Returns a random number of random letters (and simbols).
    """
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ' ]
    text = ""
    num = r.randint(min_len, max_len + 1)
    for _ in range(num):
        text += letters[r.randint(0, len(letters))]
    return text


def _get_next_word(words, sentance_structure, type_pre=0):
    """
    Returns the next random word, and it's type from the previous word type, according to the sentance structure array, and a 2D array of posible words.
    """
    type_num = r.randint(0, len(sentance_structure[type_pre]))
    word_type = sentance_structure[type_pre][type_num]
    word = words[word_type][r.randint(0, len(words[word_type]))]
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
    sentance_length = r.randint(min_len, max_len + 1)
    if sentance_length > 0:
        if sentance_length > 1:
            type_pre, word = _get_next_word(words, sentance_structure, 7)
            text += word.replace(" ", "").capitalize()
            for _ in range(sentance_length - 2):
                type_pre, word = _get_next_word(words, sentance_structure, type_pre)
                text += word
        text += _get_next_word(words, sentance_structure, 6)[1]
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

def _typewriter_line(text="", delay=4, is_delay_per_letter=True, sound=""):
    """
    Writes out text like a typewriter with end="".\n
    Returns "" so it can be easily inserted into text.\n
    Delay controlls how many millisecond it should wait between writing out two letters.\n
    If is_delay_per_letter is False, delay is how many seconds it should take to write out the entire text.\n
    You can also specify a sound that will play every time a letter is printed.
    """
    from time import sleep
    if sound != "":
        from simpleaudio import WaveObject
    
    for letter in text:
        print(letter, end="", flush=True)
        if sound != "":
            WaveObject.from_wave_file(sound).play()
        if is_delay_per_letter:
            sleep(delay / 1000)
        else:
            sleep(delay / len(text))
    return ""


def typewriter(*texts):
    """
    Can write out multiline texts letter by letter. (using the typewriter function)\n
    Accepts n number of lists each contaning a text that can have an int delay, a bool delay type and a string sound name.\n
    [TEXT, DELAY, IS_DELAY_PER_LETTER, SOUND]\n
    (delay=4, is_delay_per_letter=True, sound="")\n
    Returns "" so it can be inserted into a print.\n
    delay controlls how many millisecond it should wait between writing out two letters.\n
    If is_delay_per_letter is False, delay is how many seconds it should take to write out the entire text.\n
    sound is a path to a .wav file that will play every time a letter is printed.
    """
    texts = [x for x in texts]
    def_delay = 4
    def_delay_type = True
    def_sound = ""
    for text in texts:
        if text != []:
            if len(text) == 1:
                text = [text[0], def_delay, def_delay_type, def_sound]
            elif 1 < len(text) < 4:
                text_repair = [text[0], def_delay, def_delay_type, def_sound]
                for x in range(1, len(text)):
                    if type(text[x]) == int or type(text[x]) == float:
                        text_repair[1] = text[x]
                    elif type(text[x]) == bool:
                        text_repair[2] = text[x]
                    elif type(text[x]) == str:
                        text_repair[3] = text[x]
                text = text_repair
            _typewriter_line(text[0], text[1], text[2], text[3])
        else:
            print("TEXT ERROR!")
    return ""


def _test_run():
    seed = r.randint(0, 1000000000)
    ans = input("Seed?: ")
    if ans != "":
        seed = int(ans)
    else:
        print(f"Seed: {seed}")
    r.seed(seed)

    ans = input("Random?(Y/N): ")
    if ans.upper() == "Y":
        typewriter(unstructured_random(1, 1000), 5)
    else:
        typewriter(structured_sentance(1, 100), 5)
    input()

# -231822330	sentance(2, 2)
# _test_run()
typewriter()
#typewriter(["Hello!\nWellcome!\nGood Morning!\n", 1, False], ["How are...", 1, False], ["YOU!!!\n", 1.5, False, "close.wav"])
