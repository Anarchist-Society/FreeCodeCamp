# Función para cifrar o descifrar un texto con el cifrado caesar
def caesar(text, shift, encrypt=True):

    # Si shift no es un número devuelve error
    if not isinstance(shift, int):
        return 'Shift must be an integer value.'

    # Si shift es menor que 1 o mayor que 25 devuelve error
    if shift < 1 or shift > 25:
        return 'Shift must be an integer between 1 and 25.'

    # Alfabeto normal
    alphabet = 'abcdefghijklmnopqrstuvwxyz'

    # Si encrypt=False convertimos en negativo el shift
    if not encrypt:
        shift = - shift

    # Creamos el alfabeto desplazado según el shift
    shifted_alphabet = alphabet[shift:] + alphabet[:shift]

    # Creamos una tabla que relaciona cada posición/letra del alfabeto con el alfabeto desplazado
    translation_table = str.maketrans(alphabet + alphabet.upper(), shifted_alphabet + shifted_alphabet.upper())

    # Reemplazamos cada letra de "text" con el alfabeto desplazado
    encrypted_text = text.translate(translation_table)

    return encrypted_text

# Función para encriptar con el cifrado caesar
def encrypt(text, shift):
    return caesar(text, shift)

# Función para descifrar con el cifrado caesar
def decrypt(text, shift):
    return caesar(text, shift, encrypt=False)

encrypted_text = encrypt('hola', 1)
print(encrypted_text)

decrypt_text = decrypt(encrypted_text, 1)
print(decrypt_text)
