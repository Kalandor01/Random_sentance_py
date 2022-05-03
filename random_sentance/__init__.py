"""
This module can generate sentances with a random length from a range of words, or just a bunch of random letters.\n
It also contains a function for writing text out letter by letter at a specifiable speed and with a custom sound.
"""
__version__ = '1.4.99'

from numpy import random as npr
# exposed for custom seed
r = npr.RandomState()

def unstructured_random(min_len=1, max_len=1000, letters=None):
    """
    Returns a random number of random letters (and simbols).\n
    A characterset can be passed in as an array of characters to use.
    """
    if letters == None:
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
    # next word type
    type_num = r.randint(0, len(sentance_structure[type_pre]))
    word_type = sentance_structure[type_pre][type_num]
    # next word
    word = words[word_type][r.randint(0, len(words[word_type]))]
    # input(f"{type_pre} {word_type}: {word}")
    return word_type, word


def structured_sentance(min_len=1, max_len=100):
    """
    Returns a random string that "tries" to match a sentance structure\n
    A Word length of 1 produces only a punctuation mark. (0 produces nothing)
    """
    # dictionarry
    w_noun = [" this", " that", " car", " cat", " ice cream", " building", " house", " freezer", " doll", " art", " computer", " code", " table", " chair", " mouse", " keyboard", " monitor", " processor", " ram", " fruit", " vegetable", " desk", " pen", " pencil", " gun", " death", " paint", " brush", " shoe", " pants", " shirt", " glasses", " glass", " nose", " hair", " head", " eye", " leg", "arm", " sofa", " brain", " neuron", " dog", " parrot", " snake", " python", " hamster", " bird", " mamal", " human", " robot", " AI", " pig", " horse", " reptile", " box", " knee", " shoulder", " toe", " finger", " lamp", " rock", " mountain", " gease", " swan", " boulder", " spear", " phone", " letter", " word", " sentance", " board", " plane", " helicopter", " rocket", " space ship", " space station", " suit", " space suit", " sand", " concrete", " steel", " fire", " engine", " gas", " liquid", " water", " lava", " magma", " volcano", " universe", " galaxy", " star", " wood", " oxygen", " hydrogen", " door", " lazer", " Earth", " hat", " ball", " globe", " sphere", " Sun", " Europe", " Amerika", " moon", " city", " bridge", " village", " fuel", " explosion", " root", " tree", " plastic", " gold", " money", " diamond", " teeth", " glue", " medal", " cup"]
    w_pronoun = [" I", " you", " he", " she", " it", " they", " them", " me", " we", " us"]
    w_verb = [" eat", " give", " take", " do", " make", " destroy", " code", " can", " slap", " kick", " leave", " go", " morn", " capture", " run", " walk", " jog", " climb", " move", " sense", " hear", " see", " taste", " lick", " die", " answer", " fight", " traver", " touch", " feel", " live", " become", " pray", " cry", " clap", " think", " kill", " build", " laugh", " train", " excercierse", " read", " teach", " count", " begin", " bend", " break", " drink", " disapear", " shout", " transform", " finish", " restart", " imagine", " create", " lift", " bounce", " fall", " reach"]
    w_adjective = [" a", " an", " the", " cute", " nice", " wrong", " medium", " big", " small", " hairy", " fat", " fast", " slow", " easy", " hard", " blue", " red", " green", " white", " black", " tall", " short", " wide", " thin", " angry", " happy", " sad", " growling", " surprised", " moved", " transparrent", " soft", " golden", " tough", " conductive", " light", " heavy", " pale", " matt", " shiny", " hungry", " full", " missing", " found", " interesting", " broken", " fixed", " trapped", " freed", " free", " boring", " automatic", " dramatic", " horifying", " agrovating", " stupid", " smart", " dumb"]
    w_adverb = [" then", " quickly", " slowly", " now", " soon", " lately", " easily", " surprisingly", " accidentaly", " worryingly", " gently", " extremely", " carefully", " well", " amazingly", " totaly", " acrobaticly"]
    
    
    w_ask = [" who", " when", " why", " where", " what", " are", " is"]
    w_end = [".", "!", "?", "?!", "!?", " :)", " :(", " :D", " :C", " XD", "", "..."]
    w_between = [" is", " with", " at", " on", " in", " are", " have"]
    words = [w_noun, w_pronoun, w_verb, w_adjective, w_adverb, w_ask, w_between, w_end]
    #                      0          1         2         3        4         5        6       (7)      (8)
    #                     noun     pronoun     verb    adjective  adverb    ask     between   end    beginning
    sentance_structure = [[2, 6], [1, 2, 6], [0, 2, 6], [0, 1], [2, 3, 4], [3, 6], [0, 2, 3], [-1], [1, 3, 4, 6]]

    text = "" 
    sentance_length = r.randint(min_len, max_len + 1)
    # nothing
    if sentance_length > 0:
        # just end
        if sentance_length > 1:
            # beggining
            type_pre, word = _get_next_word(words, sentance_structure, len(sentance_structure) - 1)
            text += word.replace(" ", "").capitalize()
            # words
            for _ in range(sentance_length - 2):
                type_pre, word = _get_next_word(words, sentance_structure, type_pre)
                text += word
        # end
        text += _get_next_word(words, sentance_structure, len(sentance_structure) - 2)[1]
    return text


# SENTANCE STRUCTURE
# http://www.butte.edu/departments/cas/tipsheets/grammar/parts_of_speech.html
# NOUN, PRONOUN, VERB, ADJECTIVE, ADVERB, PREPOSITION, CONJUNCTION, INTERJECTION
"""   
    STRUCTURE:

    noun:
        -between
        -verb
    
    verb:
        -noun
        -adjective
        -between

    adjective:
        -noun
    
    pronoun:
        -verb
        -between
    
    ask:
        -pronoun
        -between
    
    between:
        -noun
        -adjective
        -pronoun
"""


def typewriter(*texts):
    """
    Accepts n number of Typewriter objects, or a list of typewriter objects and prints them out.\n
    Returns "" so it can be inserted into a print.\n
    """
    texts = [x for x in texts]
    if len(texts) == 1 and type(texts[0]) != Typewriter:
        texts = texts[0]
    for text in texts:
        text.write()
    return ""


class Typewriter():
    """
    Object for writing out text letter-by-letter with a lot of controll.\n
    delay controlls how many millisecond it should wait between writing out two letters.\n
    If is_delay_per_letter is False, delay is how many seconds it should take to write out the entire text.\n
    sound and sound_begin are paths to .wav files. sound_begin will play before the text starts printing out and sound will play every time a letter is printed.\n
    Both sound variables have a bool that controlls if the function should wait for the sound to finnish playing before continuing.\n
    If the simpleaudio module is not avalible the sound will not play (by deffault).
    """
    def __init__(self, text, delay=4, delay_type=True, sound_begin="", sound="", sound_begin_wait=False, sound_wait=False, write_warning=False):
        self.text = str(text)
        self.delay = int(delay)
        self.delay_type = bool(delay_type)
        self.sound_begin = str(sound_begin)
        self.sound = str(sound)
        self.sound_begin_wait = bool(sound_begin_wait)
        self.sound_wait = bool(sound_wait)
        self.write_warning = bool(write_warning)
    

    def write(self):
        """
        Writes out the text with the settings from the object, and returns "" so it can be easily used in a print.
        """
        # imports
        from time import sleep
        # sound?
        if self.sound != "" or self.sound_begin != "":
            sound_error = False
            try:
                from simpleaudio import WaveObject
            except ModuleNotFoundError:
                if self.write_warning:
                    print("\nSimpleaudio module not found!!!\n")
                sound_error = True
        # begin sound
        if self.sound_begin != "" and not sound_error:
            b_sound = WaveObject.from_wave_file(self.sound_begin).play()
            if self.sound_begin_wait:
                b_sound.wait_done()
        # typewriter
        for x in range(len(self.text)):
            print(self.text[x], end="", flush=True)
            if x != len(self.text) - 1:
                # sound
                if self.sound != "" and not sound_error:
                    mid_sound = WaveObject.from_wave_file(self.sound).play()
                    if self.sound_wait:
                        mid_sound.wait_done()
                # delay type
                if self.delay_type:
                    sleep(self.delay / 1000)
                else:
                    sleep(self.delay / len(self.text))
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
        typewriter(Typewriter(unstructured_random(1, 1000), 5))
    else:
        typewriter(Typewriter(structured_sentance(1, 100), 5))
    input()

while True:
    Typewriter((structured_sentance() + "\n\n")).write()
# -231822330	sentance(2, 2)
# _test_run()
# t1 = Typewriter("Hello!\nWellcome!\nGood Morning!\n", 1, False)
# t1.write()
# t2 = Typewriter("How are...", 1, False, "sound.wav")
# t3 = Typewriter("YOU!!!\n", 1.5, False, sound="enter.wav", sound_wait=True)
# typewriter(t2, t3)
# input()
