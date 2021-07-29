# -- Function to check a correct sequence in a string
def CharSequenceChecker(string):
    # -- Make a dictionary with the close and open characters
    ocChar = {
        ')': '(',
        ']': '[',
        '}': '{'
    }
    # -- Make a list to remember what characters have been opened in the string
    charOpened = []
    # -- Iterate through the string
    for i in string:
        # -- Check if the character is a open character and append to the list
        if i == '(' or i == '[' or i == '{':
            charOpened.append(i)
        # -- Check if the character detected is a close character
        elif i == ')' or i == ']' or i == '}':
            # -- Check if the list is empty (it means bad sequence
            #    close character before open character)
            if len(charOpened) == 0:
                return 'Wrong sequence'
            # -- Check if the close character matches with the last open character opened
            #    in that case, deleted the last character opened because it was closed
            if ocChar[i] == charOpened[-1]:
                del charOpened[-1]
            # -- Otherwise, it means a wrong sequence
            else:
                return 'Wrong sequence'
    # -- If the for loop ends succesfully, it means, right sequence
    return 'Right sequence'
