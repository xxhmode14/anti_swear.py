import random
import json
import os
import string

answers = ["bad", "good"]
Points = [0,0]
bad = []
good = []
data = None
json_file = None

debuging = False

d_tools = {
    "auto_save": False,
    "Display_prints": True,
    "Simulation": False
}

def Debug_Tools(key,state):
    if key in d_tools.keys():
        if key == "auto_save":
            d_tools.update(auto_save = state)
        elif key == "Display_prints":
            d_tools.update(Display_prints = state)
        return d_tools.get(key)
    else:
        print("Invalid debug option,")
        print("list of the options:")
        for word in d_tools.keys():
            print(f"> {word}\n")


sp_chars = ["!","?","|","@","#","$","%","^","&","*","/","'",'"',":",";","\\","[","{","]","}","(",")","-","_","+","=","~","."]

def load():
    global data, json_file
    if debuging:
        print("loading file . . .")
    json_file = open("data.json", "r")
    data = json.load(json_file)
    if data["bad"] == None or data["good"] == None:
        print("error while loading json file. . .")
        return
    if debuging:
        print("done")
        return


load()

# saves the date to a json file.
def save_json():
    new_file = open("data.json", "w")
    new_file.write(str(data).replace("'", '"'))
    file = open("data.json", "r")
    json_file = json.load(file)
    if json_file["bad"] == None or json_file["good"] == None:
        print("error while saving the file!")
        return
    if debuging and d_tools.get("Display_prints"):
        print("data has been successfully saved")
        return


def is_bad(text):
    global json_file, good, bad, Points
    raw_text = text
    if text == string.whitespace:
        return False
    text = str(text).lower()
    if text == "end_sim" and debuging and d_tools.get("Simulation"):
        save_json()
    for sp in sp_chars:
        text = text.replace(sp,"")
    # the final value
    Final = None

    good = data["good"]
    bad = data["bad"]

    '''
    the possibility of being good/bad
    poss[0] is the possibility of being bad
    poss[1] is the possibility of being good
    '''
    poss = [0.5, 0.5]
    if debuging and d_tools.get("Display_prints"):
        print("Prossessing . . .")
    Current_Awns = []

    for word in bad:
        # Split the word into words
        # text is the input word
        splitted = text.split(" ")
        # word is the words in the list 'bad'
        splitted_word = word.split(" ")
        for words in splitted:
            # checking for bypass
            if words.replace("1", "l") in bad:
                poss[1] -= 0.5
                poss[0] += 0.15
            # removing white space
            no_White = words.translate({ord(c): None for c in string.whitespace})
            if no_White in word:
                poss[1] -= 0.5
                poss[0] += 0.15

        if word in splitted:
            poss[1] -= 0.5
            poss[0] += 0.15

        if text in splitted_word:
            poss[1] -= 0.35
            poss[0] += 0.15

    splitted = text.split(" ")
    if splitted in bad:
        poss[1] -= 0.15
        poss[0] += 0.5
    # removing whitespace and checking if the raw word is in the list 'bad'
    if text.translate({ord(c): None for c in string.whitespace}) in bad:
        poss[1] -= 0.35
        poss[0] += 0.5
    # checking if the input text is in the list 'bad'
    if text in bad:
        poss[1] -= 0.50
        poss[0] += 0.75
    # same as bad but good
    for word in good:
        splitted = text.split(" ")
        splitted_word = word.split(" ")
        for words in splitted:
            no_White = words.translate({ord(c): None for c in string.whitespace})
            if no_White in word:
                poss[0] -= 0.05
                poss[1] += 0.1
        if word in splitted:
            poss[0] -= 0.05
            poss[1] += 0.1
        if text in splitted_word:
            poss[0] -= 0.05
            poss[1] += 0.1
        if word in text:
            poss[0] -= 0.05
            poss[1] += 0.1

    splitted = text.split(" ")
    if splitted in good:
        poss[0] -= 0.05
        poss[1] += 0.1
    if text.translate({ord(c): None for c in string.whitespace}) in good:
        poss[0] -= 0.35
        poss[1] += 0.5
    if text in good:
        poss[0] -= 0.5
        poss[1] += 0.5

    if poss[0] > poss[1]:
        if debuging and d_tools.get("Display_prints") or debuging and d_tools.get("Simulation"):
            print(answers[0])
        Current_Awns = [text, answers[0]]
    elif poss[1] > poss[0]:
        if debuging and d_tools.get("Display_prints"):
            print(answers[1])
        Current_Awns = [text, answers[1]]
    else:
        Current_Awns = [text, random.choice(answers)]
        if debuging and d_tools.get("Display_prints"):
            print(Current_Awns[1])

    '''
    this thing just get data from the json file and set it to our local var
    '''
    data["good"] = good
    data["bad"] = bad
    if debuging and d_tools.get("Display_prints"):
        print(data["bad"])
        print(data["good"])
        print(poss)
    if Current_Awns[1] == "bad":
        Final = True
    elif Current_Awns[1] == "good":
        Final = False

    if debuging and d_tools.get("Simulation"):
        print(f"word - {text}")
        fit_num = input("num of Points (how good is it): ")
        Points[0] = Points[1]
        Points[0] += int(fit_num)
        if Points[0] > Points[1]:
            if Current_Awns[1] == "good" and Current_Awns[0] not in good:
                good.append(Current_Awns[0])
            elif Current_Awns[1] == "bad" and Current_Awns[0] not in bad:
                bad.append(Current_Awns[0])
        if Points[0] < Points[1]:
            if Current_Awns[1] == "bad" and Current_Awns[0] not in good:
                good.append(Current_Awns[0])
            elif Current_Awns[1] == "good" and Current_Awns[0] not in bad:
                bad.append(Current_Awns[0])
        if not d_tools.get("auto_save"):
            save = input("do you want to save the changes y-n : ")
            if save == "y" or save == "yes":
                save_json()
            elif save == "n" or save == "no":
                return Final
        else:
            save_json()
    return Final
