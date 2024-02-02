def morse_translator(text):
    morse_code_dict = {
        "A": ".-", "B": "-...", "C": "-.-.", "D": "-..", "E": ".", "F": "..-.",
        "G": "--.", "H": "....", "I": "..", "J": ".---", "K": "-.-", "L": ".-..",
        "M": "--", "N": "-.", "O": "---", "P": ".--.", "Q": "--.-", "R": ".-.",
        "S": "...", "T": "-", "U": "..-", "V": "...-", "W": ".--", "X": "-..-",
        "Y": "-.--", "Z": "--.."
    }
    
    text = text.upper()
    
    morse_code = [] #此处新建了一个列表作为结果列表，也用于操作转化
    for char in text: #先一个一个过语句里的元素
        if char in morse_code_dict: #如果元素对应上摩斯电码则将其加入结果列表
            morse_code.append(morse_code_dict[char])
        elif char.isspace():
            morse_code.append("/")
    
    morse_text = ' '.join(morse_code)
    
    return morse_text

print(morse_translator("HELLO WORLD"))
print(morse_translator("Python"))
print(morse_translator("Morse Code"))

