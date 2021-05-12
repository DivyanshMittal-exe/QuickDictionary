from logging import root
from tkinter import Button, Checkbutton, Label, Tk, Variable,messagebox
from typing_extensions import IntVar 
from PyDictionary import PyDictionary
from notion.client import NotionClient


#Components of Notion

## In the Developer Console of your broser (Open by pressing "Ctrl+Shift+I"), go to the Networks tab and locate the token_v2, it will be a really lonf string of random characters, copy this and paste it in between the "" below 

client = NotionClient(token_v2="")


## Replace the page url below in between the "" 


cv = client.get_collection_view("")


dictionary=PyDictionary()

all_meanings = []
boxes = []
var = []
meanings_save = []

win = Tk()
win.title("Quick Dictionary")


word = win.clipboard_get()
meanings_dict= dictionary.meaning(word)

def Save_Word():
    row = cv.collection.add_row()
    row.Word = word
    if(len(meanings_save) == 0):
        messagebox.showinfo("Umm...",  "No meaning selected")
    elif(len(meanings_save) == 1):
        row.Meaning1 = meanings_save[0]
        win.destroy()
    elif(len(meanings_save) == 2):
        row.Meaning1 = meanings_save[0]
        row.Meaning2 = meanings_save[1]
        win.destroy()
    elif(len(meanings_save) >  2 ):
        row.Meaning1 = meanings_save[0]
        row.Meaning2 = meanings_save[1]
        row.Meaning3 = meanings_save[2]
        win.destroy()
        


def show():
    j = 0
    for variable in var: 
        if variable.get() == '1':
            meanings_save.append(all_meanings[j])
        j+=1
    Save_Word()    


## Function for no meaning
def NoMeaning():
    MyWord = Label(win , text= word,  font=("Arial Bold", 30))
    MyWord.grid(row=1,column=1)
    
    NoWord = Label(win , text= "No Meaning Found")
    NoWord.grid(row=2,column=2)
    
    QuitButton = Button(win, text= "Quit" , command= win.destroy )
    QuitButton.grid(row = 3, column= 1)

def Meaning():
    
    ## Corrects the array
    for key in meanings_dict:
        for meaning in meanings_dict[key]:
            word_to_add = "(" + key + ") " + meaning
            all_meanings.append(word_to_add)
            
            
    i = 0
    ##Constructs the page
    MyWord = Label(win , text= word, font=("Arial Bold", 30))
    MyWord.grid(row=1,column=1)
    
    for some_mean in all_meanings:
        var.append( Variable())
        c=Checkbutton(win, text = some_mean,variable= var[i], anchor="w")
        c.deselect()
        c.grid(row=i+2,column=2, sticky="W")
        i+=1
        
    SaveButton = Button(win, text= "Save" , command= show)
    SaveButton.grid(row=i+2,column=1)
    


if not meanings_dict:
    NoMeaning()
else:
    Meaning()


win.mainloop()


# print(word + ":")
# row.Word = word
#meanings_byType = meanings_dict.values()
# for key in meanings_dict:
#     for meaning in meanings_dict[key]:
#         print(meaning)
#         # row.Meaning1 = meaning
#         word_to_add = "(" + key + ") " + meaning
#         all_meanings.append(word_to_add)

# for mean in all_meanings:
#     print(mean)

# i = 0

# MyWord = Label(win , text= word)
# MyWord.grid(row=1,column=1)
# for some_mean in all_meanings:
#     var.append( Variable())
#     c=Checkbutton(win, text = some_mean,variable= var[i])
#     c.deselect()
#     c.grid(row=i+2,column=2)
#     i+=1

# SaveButton = Button(win, text= "Save" , command= show)
# SaveButton.grid(row=i+2,column=2)
# win.mainloop()

#breach