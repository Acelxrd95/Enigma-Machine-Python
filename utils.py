from datastructs.map_struct import Map
import re


def roman2den(roman: str) -> int:
    r_dict = Map({"M": 1000, "D": 500, "C": 100, "L": 50, "X": 10, "V": 5, "I": 1})

    last, total = 0, 0
    for c in list(roman)[::-1]:
        if last == 0:
            total += r_dict[c]
        elif last > r_dict[c]:
            total -= r_dict[c]
        else:
            total += r_dict[c]
        last = r_dict[c]
    return total


def c2n(char: str) -> int:
    """
    Converts Number to a character
    """
    num = 0
    if char.isupper():
        num = ord(char) - 65
        cap = True
    elif char.islower():
        num = ord(char) - 97
        cap = False

    return num


def n2c(num: int, upper: bool = True) -> str:
    """
    Converts Number to a character
    """
    if num > 25:
        num %= 26
    if upper:
        char = chr(num + 65)
    else:
        char = chr(num + 97)
    return char


def sp2norm(char: str) -> str:
    sp_dict = {
        ".": "YY",
        ",": "ZZ",
        "(": "KK",
        ")": "KK",
        "{": "KK",
        "}": "KK",
        "[": "KK",
        "]": "KK",
        "?": "UD",
        '"': "XX",
        "'": "XX",
        "/": "XYX",
        "\\": "YXY",
    }
    char = sp_dict[char]
    return char


def num2word(number: str) -> str:
    nm_dict = {
        # "0": ("NULL", "ZERO"),
        "0": "NULL",
        "1": "ONE",
        "2": "TWO",
        "3": "THREE",
        "4": "FOUR",
        "5": "FIVE",
        "6": "SIX",
        "7": "SEVEN",
        "8": "EIGHT",
        "9": "NINE",
    }
    retNum = ""
    for num in number:
        retNum += nm_dict[num]
        retNum += "X"
    return f"JJ{retNum}JJ"


print(num2word("10234"))
