def letter_morse(given, dictionary):
    letters = list(given.upper())
    morse_code = ""
    for letter in letters:
        for character in dictionary:
            if character == letter:
                morse_code += dictionary[character] + " "
    # morse_str = ' '.join(str(elem) for elem in morse_code)
    print("MORSE CODE: " + morse_code)


def morse_letter(given, dictionary):
    morse_code = given.split(" ")
    morse_word = ""
    for value in morse_code:
        try:
            morse_word += (dictionary[value])
        except KeyError:
            print("** Unrecognised Morse !ERROR! **")
    print("MESSAGE: " + morse_word)


def main(input_value):
    morse = {
        "A": "*-", "B": "-***", "C": "-*-*", "D": "-**",
        "E": "*", "F": "**-*", "G": "--*", "H": "****",
        "I": "**", "J": "*---", "K": "-*-", "L": "*-**",
        "M": "--", "N": "-*", "O": "---", "P": "*--*",
        "Q": "--*-", "R": "*-*", "S": "***", "T": "-",
        "U": "**-", "V": "***-", "W": "*--", "X": "-**-",
        "Y": "-*--", "Z": "--**",

        "1": "*----", "2": "**---", "3": "***--", "4": "***-",
        "5": "*****", "6": "-****", "7": "--***", "8": "---**",
        "9": "----*", "0": "-----",

        ".": "*-*-*-", ",": "--***--", ":": "---***", "?": "**--**",
        "!": "*----*", "-": "-****-", "/": "-**-*", "()": "-*--*-",
        "??": "*-**-*", " ": "/"
    }

    reverse_morse = dict(map(reversed, morse.items()))

    while input_value == "1":
        print("Press the '@' button to return to previous menu.")
        msg = input("Enter Message: ")
        if msg != "@":
            letter_morse(msg, morse)
        else:
            
            other_intro = input("Press 1 for converting words to morse and 2 for converting morse to words: ")
            main(other_intro)
    while input_value == "2":
        print("Press the '@' button to return to previous menu.")
        msg = input("Enter Morse: ")
        if msg != "@":
            morse_letter(msg, reverse_morse)
        else:
            other_intro = input("Press 1 for converting words to morse and 2 for converting morse to words: ")
            main(other_intro)

    else:
        print("Input !ERROR!")
        other_intro = input("Press 1 for converting words to morse and 2 for converting morse to words: ")
        main(other_intro)


intro = input("Press 1 for converting words to morse and 2 for converting morse to words: ")
main(intro)
