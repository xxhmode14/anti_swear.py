#Anti_swear.py

***note i am a beginer on python so don't expect much of this.***

Hello there,
well this is my first actual github repo and i don't know and why thay write this readme thing but ok

i want ***your help*** to improve my project first i will explane my horrible code

```python
answers = ["bad", "good"]
Points = [0,0]
bad = []
good = []
data = None
json_file = None
sp_chars = ["!","?","|","@","#","$","%","^","&","*","/","'",'"',":",";","\\","[","{","]","}","(",")","-","_","+","=","~","."]
debuging = False

d_tools = {
    "auto_save": False,
    "Display_prints": True,
    "Simulation": False
}
```
calling some variables,
bad has all my bad words 
good have all my good words
debuging is just debug mode
and json_file is my json file that haves all my bad/good words
i am not sure about wy special chars var but it will work

```python3
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
```
this just loads my json file that haves my swear words and good words

```python
load()
```
calls the func

```python
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
```
lets go to the main function,
first storing the raw text value
then making the string to lowercase and removing any special char
and i defined the final value in the function

```python
poss = [0.5, 0.5]
Current_Awns = []
```
the poss var is the possibility of the word being bad or good
poss[0] is bad
poss[1] is good
don't warry about the second var you will figure it out soon

```python
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
```

explaned in the comments

```python
        if word in splitted:
            poss[1] -= 0.5
            poss[0] += 0.15

        if text in splitted_word:
            poss[1] -= 0.35
            poss[0] += 0.15
```
first i checked if a bad word is in  the splited text val
and in reverse

well there is alot of things but i am out of time.
**have a nice day bye.**
