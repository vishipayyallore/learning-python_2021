def string_challenge(string_input, search1, search2):
    found = False
    index = 0

    for character in string_input:

        if(character == search1):
            if((index + 4) < len(string_input)):
                if(string_input[index + 4] == search2):
                    found = True
                    break

        if(character == search2):
            if((index + 4) < len(string_input)):
                if(string_input[index + 4] == search1):
                    found = True
                    break

        index += 1

    return found


strings = ['Laura sobs', 'box apple', 'bass car', 'ahhhb', 'aoooba', 'boooaa', 'ababa', 'after badly']
search1 = 'a'
search2 = 'b'
for input in strings:
    retults = string_challenge(input, search1, search2)
    print(input, ' === ', retults)

