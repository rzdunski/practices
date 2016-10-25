# vowels = ['a','e','i','o','u']
up_vowels = ['A', 'E', 'I', 'O', 'U', 'y']
down_vowels = ['a', 'e', 'i', 'o', 'u', 'y']
print up_vowels, down_vowels
print type(up_vowels), type(down_vowels)


# text = raw_input('Podaj text:')

def anti_vowel(text):
    new_text = []
    for char in text:
        new_text.append(char)
        for i in range(len(down_vowels)):
            if char == down_vowels[i] or char == up_vowels[i]:
                new_text.remove(char)
    return ''.join(new_text)


print anti_vowel("Hey you")
