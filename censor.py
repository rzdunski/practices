

def censor(text,word):
    new_text = text.split()
    #print new_text
    for index in range(len(new_text)):
        #print 'lenght:', len(new_text)
        #print 'index:', index
        #for item in new_text:
            #print 'item:', item
            if new_text[index] == word:
                print 'prownanie:', new_text[index]
                new_text[index] = '*' * len(word)
                print 'zamiana', new_text[index]

    return " ".join(new_text)

print censor('Hey you','you')
