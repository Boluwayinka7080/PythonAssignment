alphabet = str(input("Enter any letter of choice: "))
vowel = "a" , "e" , "i" , "o" , "u"

letter = alphabet.lower()

if (letter >= 'a' and letter <= 'z'):
    if (letter == 'a' or letter == 'e' or letter == 'i' or letter == 'o' or letter == 'u'):
        print("Alphabet is a vowel")
    else: 
        print("Alphabet is a consonant")
else:
    print("Invalid input") 

