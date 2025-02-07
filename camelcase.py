# Examples:
# "the-stealth-warrior" gets converted to "theStealthWarrior"
# "The_Stealth_Warrior" gets converted to "TheStealthWarrior"
# "The_Stealth-Warrior" gets converted to "TheStealthWarrior"

def to_camel_case(text):
    if not text:
        return ""
    text = text.replace('-', ' ').replace('_', ' ')
    words = text.split()
    return words[0].lower() + ''.join([word.capitalize() for word in words[1:]])


if __name__ == '__main__':
    print(to_camel_case('the-stealth-warrior'))
    print(to_camel_case('The_Stealth_Warrior'))
    print(to_camel_case('The_Stealth-Warrior'))
    print(to_camel_case('The_Stealth-Warrior-'))
    print(to_camel_case('The_Stealth-Warrior_'))
    print(to_camel_case('The_Stealth-Warrior_ '))
