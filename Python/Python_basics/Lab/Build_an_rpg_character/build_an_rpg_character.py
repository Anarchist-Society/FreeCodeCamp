print('Build an RPG Character:\n')

full_dot = '●'
empty_dot = '○'

def create_character(name, strength, intelligence, charisma):

    # Si name no es un str devuelve error
    if not isinstance(name, str):
        return 'The character name should be a string'

    # Si name está vacío devuelve error
    if name == '':
        return 'The character should have a name'

    # Si la longitud de name es mayor que 10 devuelve error
    if len(name) > 10:
        return 'The character name is too long'

    # Si name contiene espacio devuelve error
    if ' ' in name:
        return 'The character name should not contain spaces'

    # Si strength o intelligence o charisma no es un int devuelve error
    if not isinstance(strength, int) or not isinstance(intelligence, int) or not isinstance(charisma, int):
        return 'All stats should be integers'

    # Si strength o intelligence o charisma es menor que 1 devuelve error
    if strength < 1 or intelligence < 1 or charisma < 1:
        return 'All stats should be no less than 1'

    # Si strength o intelligence o charisma es mayor que 4 devuelve error
    if strength > 4 or intelligence > 4 or charisma > 4:
        return 'All stats should be no more than 4'

    # Si la suma de strength e intelligence y charisma no es igual a 7 devuelve error
    if strength + intelligence + charisma != 7:
        return 'The character should start with 7 points'

    return name + "\nSTR " + full_dot * strength + empty_dot * (10 - strength) + "\nINT " + full_dot * intelligence + empty_dot * (10 - intelligence) + "\nCHA " + full_dot * charisma + empty_dot * (10 - charisma)

create_character('ren', 4, 2, 1)
create_character('robert', 1, 5, 1)
