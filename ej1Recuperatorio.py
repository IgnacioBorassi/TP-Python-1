letters = ["a","b","c","d","e","f","g","h","i","j","k","l","m","A","B","C","D","E","F","G","H","I","J","K","L","M","n","o","p","q","r","s","t","u","v","w","x","y","z","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
ROT13 = ["n","o","p","q","r","s","t","u","v","w","x","y","z","N","O","P","Q","R","S","T","U","V","W","X","Y","Z","a","b","c","d","e","f","g","h","i","j","k","l","m","A","B","C","D","E","F","G","H","I","J","K","L","M"]
text = input("Ingrese una frase: ")
word = text.split(" ")
def converter(texto):
    """Esta funcion se encarga de encriptar con la convencion ROT13"""
    phrase = ""
    qtyletters = len(text)
    for i in range (qtyletters):
        phrase = f"{phrase.strip()}{word[i].replace(letters[i], ROT13[i])}" 
    return f"la clave encriptada es:{phrase}"