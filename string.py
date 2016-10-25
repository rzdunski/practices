text = str(raw_input("Podaj string:"))


def reverse(text):
    lista = []
    #new_lista = []
    for i in range(len(text)):
        # print text[i]
        lista.append(text[(len(text) - 1) - i])
    return ''.join(lista)
    # lista.append(i)
    #print
    """
    print len(text)
    for i in range(len(lista)):
        print lista[(len(lista)-1)-i]
"""


print reverse(text)
