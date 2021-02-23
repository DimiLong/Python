translate = {'One' : 'Один', 'Two' : 'Два', 'Three' : 'Три', 'Four' : 'Четыре'}
separator = ' '
with open('input.txt') as inputFile:
    with open('output.txt', 'w') as outputFile:
        for i in inputFile:
            words = i.split(separator, 1)
            wordFortTanslate = words.pop(0)
            words.insert(0, translate[wordFortTanslate])
            outputFile.write(separator.join(words))