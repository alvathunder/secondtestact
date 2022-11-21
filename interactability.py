import re
import pywhatkit
import random
import json_checkorcreate as file_check
import unknown_input as unknown

def input_accuracy(user_input, known_words, oneword_response=False, mandatory_words=[]): # Steve checks the if the user input is most likely a correct sentance or not
    message_certainty = 0 
    verified_scentence = True #if Steve can't detect required words, this will turn False

    #Checks how many words are present in each predefined message--
    for word in user_input: # Steve loops through the sentance to check the words
        if word in known_words: #if one of the words exist within the user input sentance, the certainty will increase by 1 
            message_certainty += 1 

    #Calculates the percentage of known words in the user input
    percentage = float(message_certainty) / float(len(known_words)) #Steve calculates the the certainty of the sentance (0-100%) 

    # Checks that the required words are in the string
    for word in mandatory_words:
        if word not in user_input: # if Steve can't detect any of the key words
            verified_scentence = False 
            break 

    # Must either have the required words, or be a single response
    if verified_scentence or oneword_response:
        return int(percentage * 100) #returns a percentage between 0-100
    else:
        return 0

def input_validation(user_input):
    most_likelylist = {}

    # Simplifies response creation / adds it to the dict
    def response(steve_response, list_of_words, oneword_response=False, mandatory_words=[]):
        nonlocal most_likelylist #dict from most_likelylist
        most_likelylist[steve_response] = input_accuracy(user_input, list_of_words, oneword_response, mandatory_words) #X

    #Steve will print the first string (as Hello!, See you! etc) when the user types the words listed within the list. Some of the responses will require certain words for a response to be made. So if Steve is going to respond "I\'m doing fine, and you?", the word "how" has to be stated in the user input. 
    response('Hello!', ['hello', 'hi', 'hey', 'sup', 'heyo'], oneword_response=True) #when specifying the single_response, Steve will not check has_required_words
    response('Ciao!', ['bye', 'goodbye'], oneword_response=True) 
    response('I\'m great! How about you?', ['how', 'are', 'you', 'doing'], mandatory_words=['how']) #when specifying the required_words, Steve will check has_required_words
    response('Anytime!', ['thank', 'thanks'], oneword_response=True)
    response('I suggest you do something, like trying to lick you elbow!', ['i\'m', 'bored',], mandatory_words=['bored'])
    response('Try google! Or reaching out to a friend!', ['give', 'advice'], mandatory_words=['advice'])
    response('I frickin love cookies! I eat them one byte at a time.', ['what', 'you', 'eat'], mandatory_words=['you', 'eat']) 

    response_match = max(most_likelylist, key=most_likelylist.get)

    return unknown.unknown() if most_likelylist[response_match] < 1 else response_match


#Collecting the response and breaks down the message into seperate words so that Steve can check for key words. We're also removing all of the commonly used symbols
def get_response(user_input):
    split_message = re.split(r'\s+|[,;?!.-]\s*', user_input.lower())
    if 'play' in user_input:
        # song = input('hi whats up')
        split_message = user_input.replace('play', '')
        print('Playing song..')
        pywhatkit.playonyt(split_message)
        print('Enjoy!')
    pass  # why does he return a unknown response?

    response = input_validation(split_message)
    return response

while True:
    print('Steve: ' + get_response(input('You: ')))
