import random

def gen_pass(pass_length):
    elements = "+-/*!&$#?=@<>abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890" 
    password = ""

    for i in range(pass_length):
        password += random.choice(elements)

    return password

def gen_emodji():
    emodji = ["\U0001f600", "\U0001f642", "\U0001F606", "\U0001F923"]
    return random.choice(emodji)


def flip_coin():
    flip = random.randint(0, 2)
    if flip == 0:
        return "CARA"
    else:
        return "CRUZ"
 
def plantaR():
    Planta = random.randint(0,3)

    if Planta == 0:
        Planta = "Cactus"
    
    elif Planta == 1:
        Planta = "Floral"

    elif Planta == 2:
        Planta = "Anturio"

    else:
        Planta = "Arbol"

    return Planta