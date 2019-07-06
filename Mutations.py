def mutate_string(string, position, character):
    strin = string[:position] + character + string[position+1:]
    return strin

