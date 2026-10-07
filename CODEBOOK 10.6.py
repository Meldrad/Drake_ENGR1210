CODEBOOK = [('A','-'),('B','-...'),('C','-.-.'),('D','-..'),('E','.'),('F','..-.'),('G','--.'),('H','....'),('I','..'),('J','.---'),('K','-.-'),('L','.-..'),('M','--'),('N','-.'),('O','---'),('P','.--.'),('Q','--.-'),('R','.-.'),('S','...'),('T','-'),('U','..-'),('V','...-'),('W','.--'),('X','-..-'),('Y','-.--'),('Z','--..')]
ENCODE_MAP ={letter: pat for letter, pat in CODEBOOK}
DECODE_MAP ={pat: letter for letter, pat in ENCODE_MAP.items()}

while True:
    text = input("Message>: ")

    if text.lower() == "quit":
        break
    morse = [ENCODE_MAP.get(c.upper(), '') for c in text]

    print(" ".join(morse))

while True:
    print("1) Encode 2) Count 3) Quit")
    choice = input("Choice: ")

    if choice == "1":
        text = input("  Text>  ")
        print(" ".join(ENCODE_MAP.get(c.upper(), '') for c in text))
    elif choice == "2": print (len(ENCODE_MAP), "letters")
    elif choice == "3": break
    else: print("pick 1, 2, or 3")

while True:
    raw = input ("how many times? ")

    try:
        count = int(raw)
        break
   
    except ValueError:
        print("Please enter a number.")

print ("repeating", count, "times")