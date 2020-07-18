'''
Your function should take in a single parameter (a string `word`)
Your function should return a count of how many occurences of ***"th"*** occur within `word`. Case matters.
Your function must utilize recursion. It cannot contain any loops.
'''
def count_th(word):

    #create counter to keep track of 'th's found
    count = 0

    # If word is 1 character
    # base case
    if len(word) < 2:
        return 0

    

    #if the first two letters are 'th'
    if word[0] + word[1] == 'th':
        #increase count by 1 and send back the rest of the word
        count = 1 + count_th(word[1:]) 

    #If first two letters are not 'th'
    else:
        #send the word from index 1 to the last index into count
        return count_th(word[1:])
    return count




