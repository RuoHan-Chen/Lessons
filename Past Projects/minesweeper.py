from tkinter import *
from tkinter import ttk
import random
import time



#60 total squares

#On answer board:
#0: 0 bordering (blank)
#1: 1 bordering
#2: 2 bordering
#3: 3 bordering
#4: 4 bordering
#5: 5 bordering
#6: 6 bordering
#7: 7 bordering
#8: 8 bordering
#9: Bomb

#On View board:
#0: 0 bordering (blank dug)
#1: 1 bordering
#2: 2 bordering
#3: 3 bordering
#4: 4 bordering
#5: 5 bordering
#6: 6 bordering
#7: 7 bordering
#8: 8 bordering
#9: Bomb
#R: Blank Undug
#F: Flag

answerboard = []
flagged = []

totalbombs = 0
print('''
Welcome to Minesweeper!
Your goal is to find the location of every bomb,
without blowing it up.
If you click on a bomb square, you lose.
If the square isn't a bomb square,
it will show a number. That number is 
the amount of bombs that border it,
adjacently and diagonally.
You win when you have clicked on every non-bomb square.
For squares that you think or know are bombs, you can
right-click them for a flag. To remove the flag,
right click it again.
''')
customize = input('Would you like to customize your game? (y/n)')
if customize == "y":
  prob = int(input('A square has a one in (answer) chance of being a bomb.'))
  chanc = (prob) - 1
else:
  prob = 10
  chanc = (prob) - 1
for h in range (0,62):
  flagged.append(0)
  chance = random.randint(0,prob-1)
  if chance == 1:
    answerboard.append(9)
    totalbombs = totalbombs + 1
  else:
    answerboard.append("")
print('')
print("Good luck!")
print('Chance of bomb: 1/' + str(prob))
print("Total bombs: " + str(totalbombs - 1))

for h in range (0,62):
  if answerboard[h] != 9:
    bordering = 0
    if h < 60:
      if answerboard[h + 1] == 9:
        bordering = bordering + 1
    if answerboard[h - 1] == 9:
      bordering = bordering + 1
    if h < 52:
      if answerboard[h + 9] == 9:
        bordering = bordering + 1
    if answerboard[h - 9] == 9:
      bordering = bordering + 1
    if answerboard[h - 8] == 9:
      bordering = bordering + 1
    if answerboard[h - 10] == 9:
      bordering = bordering + 1
    if h < 51:
      if answerboard[h + 10]:
        bordering = bordering + 1
    if h < 53:
      if answerboard[h+8]:
        bordering = bordering + 1
    answerboard[h] = bordering

def getbombs():
  for h in range(0,7):
    nextb = random.randint(0,62)
    
turn = 0
buttons = []

#def setplayer():
  #if turn%2 == 0:
  #Button.config(text="h")
    

def newbutton(c, r, n, t, l):
  #print(flagged)
  def destroybutton():
    global squaresleft
    buttons[n-2].destroy()
    buttons.pop(n-2)
    if answerboard[n-2] == 9:
      twoadd = ttk.Button(frm, text="\n" + t + "\n", width=6)
      twoadd.grid(column=c, row=r)
      buttons.insert(n-2, twoadd)
      #print(len(buttons))
      print('''Result: You lose!''')
      #exit()
    else: 
      twoadd = ttk.Button(frm, text="\n" + t + "\n", width=6)
      twoadd.grid(column=c, row=r)
      buttons.insert(n-2, twoadd)
      squaresleft = squaresleft - 1
      if squaresleft == totalbombs:
        while True:
          print('Result: You win!')
        #exit()
    #print(buttons)
    #print(len(buttons))
  def addflag(h):
    def removeflag(h):
      #print(buttons[n-2])
      threeadd.destroy()
      #ttk.Button(frm, text="\n" + "" + "\n", width=6).grid(column=c, row=r)
      flagged.pop(n)
      flagged.insert(n, 0)
      #print(flagged)
    #buttons[n - 2].destroy()
    #NOTE: THIS BUTTON IS NOT PART OF THE BUTTONS LIST
    #to do: create new list for this button to do stuff
    #threeadd
    threeadd = ttk.Button(frm, text="\n" + "Flag" + "\n", width=6)
    threeadd.grid(column=c, row=r)
    threeadd.bind("<Button-3>", removeflag)
    flagged.pop(n)
    flagged.insert(n, 1)
    #print(flagged)
  #time.sleep(1)
  if buttonnum%20 == 21:
    global y
    global x
    global toadd
    #y = y + 1
    #x = -1
  if l == 2:
    if buttonnum < 62:
      toadd = (ttk.Button(frm, text="\n" + "" + "\n", width=6, command=destroybutton))
      toadd.grid(column=c, row=r)
      toadd.bind("<Button-3>", addflag)
      #toadd.bind("<Button-2>", removeflag)
      buttons.append(toadd)
  #print(buttons)
  #elif l == 1:
    #if buttonnum2 < 62:
      #ttk.Button(tfrm, text="\n" + t + "\n", width=6).grid(column=c, row=r)


  



def newbutton2():
  global x
  global y
  global buttonnum
  x = x+1
  y = y+0
  buttonnum = buttonnum+1
  for h in range(0,62):
    if answerboard[h] == 9:
      text = "BOMB"
    else:
      text = str(answerboard[h])
    newbutton(x, y, buttonnum, str(text), 2)
    x = x+1
    y = y+0
    buttonnum = buttonnum+1
    if buttonnum%9 == 1:
      y = y+1
      x = 0



def newbutton3():
  global x2
  global y2
  global buttonnum2
  x2 = 1
  y2 = 1
  for h in range(0,62):
    newbutton(x2, y2, buttonnum2, "top", 1)

buttonnum2 = 1
buttonnum = 1
x = 0
y = 0

def selfdestruct():
  root.destroy()
  print('Result: You lose!')

root = Tk()
frm = ttk.Frame(root, padding=10)
frm.grid()
frm.grid()
ttk.Button(frm, text="Mines" + "\n     by" + "\n", width=6).grid(row = 6, column=7)
ttk.Button(frm, text="weeper" + "\nme" + "\n", width=6).grid(row = 6, column=8)
ttk.Button(frm, text="  DO" + "\n NOT" + "\nCLICK", width=6, command=selfdestruct).grid(row = 0, column=0)
squaresleft = 60
newbutton2()
newbutton3()


root.mainloop()