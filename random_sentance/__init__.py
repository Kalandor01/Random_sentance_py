"""
This module can generate sentances with a random length from a range of words, or just a bunch of random letters.\n
It also contains a function for writing text out letter by letter at a specifiable speed and with a custom sound.
"""
__version__ = '1.5'

from numpy import random as npr
# exposed for custom seed
r = npr.RandomState()

# dictionarry
W_NOUN = [" this", " that", " car", " cat", " ice cream", " building", " house", " freezer", " doll", " art", " computer", " code", " table", " chair", " mouse", " keyboard", " monitor", " processor", " ram", " fruit", " vegetable", " desk", " pen", " pencil", " gun", " death", " paint", " brush", " shoe", " pants", " shirt", " glasses", " glass", " nose", " hair", " head", " eye", " leg", "arm", " sofa", " brain", " neuron", " dog", " parrot", " snake", " python", " hamster", " bird", " mamal", " human", " robot", " AI", " pig", " horse", " reptile", " box", " knee", " shoulder", " toe", " finger", " lamp", " rock", " mountain", " gease", " swan", " boulder", " spear", " phone", " letter", " word", " sentance", " board", " plane", " helicopter", " rocket", " space ship", " space station", " suit", " space suit", " sand", " concrete", " steel", " fire", " engine", " gas", " liquid", " water", " lava", " magma", " volcano", " universe", " galaxy", " star", " wood", " oxygen", " hydrogen", " door", " lazer", " Earth", " hat", " ball", " globe", " sphere", " Sun", " Europe", " Amerika", " moon", " city", " bridge", " village", " fuel", " explosion", " root", " tree", " plastic", " gold", " money", " diamond", " teeth", " glue", " medal", " cup"]
W_PRONOUN = [" I", " you", " he", " she", " it", " they", " them", " me", " we", " us"]
W_VERB = [" eat", " give", " take", " do", " make", " destroy", " code", " can", " slap", " kick", " leave", " go", " morn", " capture", " run", " walk", " jog", " climb", " move", " sense", " hear", " see", " taste", " lick", " die", " answer", " fight", " traver", " touch", " feel", " live", " become", " pray", " cry", " clap", " think", " kill", " build", " laugh", " train", " excercierse", " read", " teach", " count", " begin", " bend", " break", " drink", " disapear", " shout", " transform", " finish", " restart", " imagine", " create", " lift", " bounce", " fall", " reach"]
W_ADJECTIVE = [" a", " an", " the", " cute", " nice", " wrong", " medium", " big", " small", " hairy", " fat", " fast", " slow", " easy", " hard", " blue", " red", " green", " white", " black", " tall", " short", " wide", " thin", " angry", " happy", " sad", " growling", " surprised", " moved", " transparrent", " soft", " golden", " tough", " conductive", " light", " heavy", " pale", " matt", " shiny", " hungry", " full", " missing", " found", " interesting", " broken", " fixed", " trapped", " freed", " free", " boring", " automatic", " dramatic", " horifying", " agrovating", " stupid", " smart", " dumb"]
W_ADVERB = [" then", " quickly", " slowly", " now", " soon", " lately", " easily", " surprisingly", " accidentaly", " worryingly", " gently", " extremely", " carefully", " well", " amazingly", " totaly", " acrobaticly"]


W_ASK = [" who", " when", " why", " where", " what", " are", " is"]
W_END = [".", "!", "?", "?!", "!?", " :)", " :(", " :D", " :C", " XD", "", "..."]
W_END_QUESTION = ["?", "?!", "!?"]
W_BETWEEN = [" is", " with", " at", " on", " in", " are", " have"]
WORDS = [W_NOUN, W_PRONOUN, W_VERB, W_ADJECTIVE, W_ADVERB, W_ASK, W_BETWEEN, W_END, W_END_QUESTION]
#                      0         1       2         3         4        5        6       (7)    (8)      (9)
#                     noun    pronoun   verb   adjective   adverb     ask    between   end  end_ask  beginning
SENTANCE_STRUCTURE = [[2, 6], [2, 6], [0, 2, 6], [0, 1], [2, 3, 4], [3, 6], [0, 2, 3], [-2], [-1], [0, 1, 2, 3, 4, 5]]
ENDING_WORD = [0, 2]
# extra: 1, 


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


def _get_next_word(previous_type=0):
    """
    Returns the next random word, and it's type from the previous word type, according to the sentance structure array, and a 2D array of posible WORDS.
    """
    # next word type
    type_num = r.randint(0, len(SENTANCE_STRUCTURE[previous_type]))
    word_type = SENTANCE_STRUCTURE[previous_type][type_num]
    # next word
    word = WORDS[word_type][r.randint(0, len(WORDS[word_type]))]
    # input(f"{previous_type} {word_type}: {word}")
    return word_type, word


def structured_sentance(min_len=1, max_len=100, end_on_good_word=True):
    """
    Returns a random string that "tries" to match a sentance structure\n
    A Word length of 1 produces only a punctuation mark. (0 produces nothing)\n
    If end_on_good_word is True, the sentance will not end until the word type is an ending word.
    """

    text = "" 
    sentance_length = r.randint(min_len, max_len + 1)
    # nothing
    if sentance_length > 0:
        # just end
        beginning_word = -1
        if sentance_length > 1:
            # beggining
            previous_type, word = _get_next_word(len(SENTANCE_STRUCTURE) - 1)
            beginning_word = previous_type
            text += word.replace(" ", "").capitalize()
            # words
            curr_word_num = 0
            while curr_word_num < sentance_length - 2 or (not previous_type in ENDING_WORD and end_on_good_word):
                curr_word_num += 1
                previous_type, word = _get_next_word(previous_type)
                text += word
        # end
        if beginning_word == 5:
            text += _get_next_word(len(SENTANCE_STRUCTURE) - 2)[1]
        else:
            text += _get_next_word(len(SENTANCE_STRUCTURE) - 3)[1]
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

for _ in range(100):
    Typewriter((structured_sentance(1, 10) + "\n\n")).write()
# -231822330	sentance(2, 2)
# _test_run()
# t1 = Typewriter("Hello!\nWellcome!\nGood Morning!\n", 1, False)
# t1.write()
# t2 = Typewriter("How are...", 1, False, "sound.wav")
# t3 = Typewriter("YOU!!!\n", 1.5, False, sound="enter.wav", sound_wait=True)
# typewriter(t2, t3)
# input()
