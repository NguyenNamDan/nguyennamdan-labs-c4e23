def remove_dollar_sign(char):
    char_remove = char.replace("$", "")
    return char_remove
char_new = remove_dollar_sign("toi co 1$")
print(char_new)  