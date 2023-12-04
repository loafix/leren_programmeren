import random
def get_random_compliment(naam: str) -> str:
    MIJN_COMPLIMENT = ("je bent geweldig:", "je doet het super:", "niemand is zoals jij:", "beste van de beste:", "beter dan iedereen:",)
    compliment = random.choice(MIJN_COMPLIMENT)
    return f"{compliment} {naam}"

print (get_random_compliment("dylan"))