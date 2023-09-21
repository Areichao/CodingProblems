def snt(a: str, b:str) -> bool:
    if len(a) != len(b):
        return False
    dicta = {}
    for letter in a:
        if letter in dicta:
            dicta[letter] += 1
        else:
            dicta[letter] = 1
    for letter in b:
        if (letter in dicta) and :
            dicta[letter] -= 1
        else:
            return False
    
 