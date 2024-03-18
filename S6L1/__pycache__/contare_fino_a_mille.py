def translate_to_20(n):
    if n > 19:
        return "out of range"

    NUMBERS = ["","uno", "due", "tre", "quattro", "cinque", "sei", "sette",
               "otto", "nove", "dieci", "undici", "dodici", "tredici",
               "quattordici", "quindici", "sedici", "diciassette",
               "diciotto", "diciannove"]
    return NUMBERS[n]

def translate_to_100(n):
    if n < 20:
        return translate_to_20(n)
    if n > 99:
        return "out of range"
    DECADES = ["venti", "trenta", "quaranta", "cinquanta", "sessanta",
               "settanta", "ottanta", "novanta"]
    decade =  n // 10
    unit = n % 10
    return DECADES[decade-2] + translate_to_20(unit)

def translate_to_1000(n):
    if n < 100:
        return translate_to_100(n)
    if n > 1000:
        return "Out of range"
    elif n == 1000:
        return "mille"
    hundreds = n // 100
    remainder = n % 100
    if remainder == 0:
        return translate_to_20(hundreds) + "cento"
    else:
        return translate_to_20(hundreds) + "cento" + translate_to_100(remainder)

def translate_number(n):
    return translate_to_1000(n)

for x in range(1, 1002):
    print(translate_number(x))