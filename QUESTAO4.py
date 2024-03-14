morse_code_dict = {
    'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.', 'G': '--.', 'H': '....', 'I': '..', 
    'J': '.---', 'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.', 'O': '---', 'P': '.--.', 'Q': '--.-', 'R': '.-.', 
    'S': '...', 'T': '-', 'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-', 'Y': '-.--', 'Z': '--..',
    '1': '.----', '2': '..---', '3': '...--', '4': '....-', '5': '.....', '6': '-....', '7': '--...', '8': '---..', 
    '9': '----.', '0': '-----', ' ': '/'
}

def text_to_morse(text):
    morse_code = ''
    for char in text.upper():
        if char in morse_code_dict:
            morse_code += morse_code_dict[char] + ' '
    return morse_code.strip()

def morse_to_text(morse_code):
    text = ''
    morse_code += ' ' 
    morse_char = ''
    for symbol in morse_code:
        if symbol != ' ':
            morse_char += symbol
        else:
            for key, value in morse_code_dict.items():
                if value == morse_char:
                    text += key
                    break
            else:
                if morse_char == '/':
                    text += ' '
                else:
                    text += '[?]'
            morse_char = ''
    return text


texto = str(input("Digite uma palvra: "))
codigo_morse = text_to_morse(texto)
print("Texto em código Morse:", codigo_morse)

texto_decodificado = morse_to_text(codigo_morse)
print("Texto decodificado:", texto_decodificado)
