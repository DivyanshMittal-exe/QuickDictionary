# Quick Dictionary

Someimes when reading a good book, you come accross a word whose meaning, you might not know. Looking up that meaning is a hastle and breaks your flow. Quick Dictionary is a pretty simple solution for this. Using AutoHotkey and Notion along with Tkinter, this small application searches the meaning of the word and opens a small window to dispay the various meanings of the words. This then also stores the meaning of the word on Notion an awesome note taking site, because thats how you'll most likely improve your vocabulary at the fastest pace, that is through repetition. 

## Installation guide 
1. Install python 
2. Install autohotkey
2. Install PyDictionary and notion via the comands `pip install notion` and `pip install PyDictionary`
3. Clone the repo
4. Create a new table page in Notion and copy its url and paste it in the code. The instructions given in the comments
5. Create 4 columns by the name "Word","Meaning1","Meaning2","Meaning3"
6. Now you need to extract a code by the name of "token_v2". Its like a long random strings of characters that helps the site identify you.
    1. On the notion website ,enter the developer console by pressing <kbd >Ctrl</kbd><kbd >Shift</kbd><kbd >I</kbd>
    2. Now go to the Networking tab (On the top there will be many tabs like Console,Elements,Sources,etc)
    3. Now inside the window, you will see various names like queryCollection , saveTransaction , etc (If you don,t try making any edit to the page without closing the console tab).
    4. Open any one of them and under request headers you will find cookie, this will have the token_v2 attribute, copy this (If it doesn't try another name , [Names like queryCollection , saveTransaction,getAssetsJsonV2 will surely have them ]) 
    5. Paste this in the required location inside the code [Comments will guide you further]

## Using the code
Fortunately using this is much much simpler.

Run the autohotkey script by doubleclicking it. Simply select the word whose meaning you want to know and press  <kbd >Ctrl</kbd><kbd >Q</kbd> . A popup will open with the meaning. Select the definations whom you wanna save (Upto 3) and press the Save button. If no meaning is ound the application simply returns no value found.

Once you restart your computer, you will have to again activate the script, but a simple workaround is to place the shortcut of the script in ` C:\Users\User\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Startup  ` directory. [Press <kbd >Win</kbd><kbd >R</kbd> and enter `shell:startup` to open this directory deirectly]
