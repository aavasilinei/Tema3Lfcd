def finiteAutomata(myFile):

    states = []
    alphabet = []
    initial = None
    final = None

    with open(myFile) as file:
        states = file.readline()
        index = states.find('states: ')
        if index != -1:
            states = states[index + len('states: '):]

        alphabet = file.readline()
        index = states.find('alphabet: ')
        if index != -1:
            alphabet = alphabet[index + len('alphabet: '):]

        initial = file.readline()
        final = file.readline()
        uselessLine = file.readline()

        print("States:", states)
        print("Alphabet", alphabet)
        print("initial", initial)
        print("final", final)
        print("transitions: \n")

        for line in file:
            print(line)


finiteAutomata("finiteAutomata.txt")

