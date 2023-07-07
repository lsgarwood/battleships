import tkinter
from colorama import Fore
from tkinter import font
import asynctkinter

#the grids
user1boats: list[list[int]] = [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                               [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                               [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                               [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                               [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                               [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                               [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                               [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                               [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                               [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]
user1grid = [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]
user2boats = [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
              [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
              [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
              [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
              [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]
user2grid = [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]

#function to display the grids
def displaygrid(cframe, grid: list[list[int]]):
  cframe.columnconfigure(0, weight=1, minsize=5)
  cframe.rowconfigure(0, weight=1, minsize=5)
  for j in range(1, len(grid[0]) + 1):
    frame = tkinter.Frame(cframe, borderwidth=0.5)
    frame.grid(row=0, column=j, padx=3, pady=1)
    label = tkinter.Label(frame, text=str(j))
    label.pack(padx=3, pady=1)
  for i in range(len(grid)):
    cframe.columnconfigure(i, weight=1, minsize=5)
    cframe.rowconfigure(i, weight=1, minsize=5)
    frame = tkinter.Frame(cframe, borderwidth=0.5)
    frame.grid(row=i + 1, column=0, padx=3, pady=1)
    label = tkinter.Label(frame, text=str(i + 1))
    label.pack(padx=3, pady=1)
    for j in range(len(grid[i])):
      frame = tkinter.Frame(cframe, borderwidth=0.5)
      frame.grid(row=i + 1, column=j + 1, padx=3, pady=1)
      label = tkinter.Label(frame, text=str(grid[i][j]))
      label.pack(padx=3, pady=1)


#placing user1's boats
placedboats = False
async def place_user1boats():
  btn2.config(state="disabled")
  btn1.config(state="disable")

  async def input(s: str):
    print(s)
    player1_entry.config(state="normal")
    store_player1_entry.set("")
    await asynctkinter.event(player1_entry, "<Return>")
    player1_entry.config(state="disabled")
    return store_player1_entry.get()

  for i in range(0, 4):
    rotation = ""
    while rotation != "d" and rotation != "a":
      print(Fore.WHITE + '\n\ndo you want boat', i + 1, 'to be down or along?')
      rotation = await input(' please type (d) or (a)')
      if rotation != "d" and rotation != "a":
        print(Fore.RED + "invalid boat direction. retry.")

    space = True
    while space == True:
      boatOk = True
      while boatOk == True:
        boat = (await input(
          Fore.WHITE +
          '\nwhere do you want to put ur boat? type in form (column,row)'))
        try:
          list = boat.split(',')
          user1col = int(list[0]) - 1
          user1row = int(list[1]) - 1
          boatOk = False
        except:
          print(
            Fore.RED +
            "there were issues converting your input. please ensure your co-ordinates are between 1 and 10, in the format (column,row)"
          )
        try:
          if rotation == 'a':
            for i in range(0, 4):
              user1boats[user1row][user1col] = 1
              user1col = user1col + 1

            displaygrid(box1, user1boats)
          elif rotation == 'd':
            for i in range(0, 4):
              user1boats[user1row][user1col] = 1
              user1row = user1row + 1

            displaygrid(box1, user1boats)
          space = False
        except:
          print(
            Fore.RED +
            "your boat would appear offscreen. please pick another co ordinate"
          )
  btn2.config(state="normal")

#placing user2's boats
async def place_user2boats():
  global placedboats
  btn4.config(state="disabled")
  btn3.config(state="disable")

  async def input(s: str):
    print(s)
    player2_entry.config(state="normal")
    store_player2_entry.set("")
    await asynctkinter.event(player2_entry, "<Return>")
    player2_entry.config(state="disabled")
    return store_player2_entry.get()

  for i in range(0, 4):
    rotation = ""
    while rotation != "d" and rotation != "a":
      print(Fore.WHITE + 'do you want boat', i + 1, 'to be down or along?')
      rotation = await input(' please type (d) or (a)')
      if rotation != "d" and rotation != "a":
        print(Fore.RED + "invalid boat direction.")

    space = True
    while space == True:
      boatOk = True
      while boatOk == True:
        boat = (await input('where do you want to put ur boat? type in form (column,row)'))
        try:
          list = boat.split(',')
          user2col = int(list[0]) - 1
          user2row = int(list[1]) - 1
          boatOk = False
        except:
          print(Fore.RED +"there were issues converting your input. please ensure your co-ordintaes are between 1 and 10, in the format (column,row)")
        try:
          if rotation == 'a':
            for i in range(0, 4):
              user2boats[user2row][user2col] = 1
              user2col = user2col + 1

            displaygrid(box2, user2boats)
          elif rotation == 'd':
            for i in range(0, 4):
              user2boats[user2row][user2col] = 1
              user2row = user2row + 1

            displaygrid(box2, user2boats)
          space = False
        except:
          print(Fore.RED +"your boat would appear offscreen. please pick another co ordintae")
  btn4.config(state='normal')
  placedboats = True
  print(placedboats)

#player1 guesses
async def player1_guesses():
  btn2.config(state="disabled")
  btn1.config(state="disable")
  async def input(s: str):
    print(s)
    player3_entry.config(state="normal")
    store_player3_entry.set("")
    await asynctkinter.event(player3_entry, "<Return>")
    player3_entry.config(state="disabled")
    return store_player3_entry.get()
  user1try = True
  while user1try == True:
    try:
      user1guess = (await input('user1. input ur guess in colum, row.'))
      list = user1guess.split(',')
      user1col = int(list[0]) - 1
      user1row = int(list[1]) - 1
      if user2boats[user1row][user1col] == 1:
        user1grid[user1row][user1col] = 7
        #hit1 = hit1 + 1
        for i in range(0, 10):
          displaygrid(box21,user1grid)
      elif user2boats[user1row][user1col] == 0:
        user1grid[user1row][user1col] = 5
        for i in range(0, 10):
          displaygrid(box21,user1grid)
      user1try = False
    except: 
      print(Fore.RED +"co-ordinate is incorrect formate, please try again")
      
  btn2.config(state='normal')
    

#player2 guesses
async def player2_guesses():
  btn4.config(state="disabled")
  btn3.config(state="disable")
  async def input(s: str):
    print(s)
    player4_entry.config(state="normal")
    store_player4_entry.set("")
    await asynctkinter.event(player4_entry, "<Return>")
    return store_player4_entry.get()
  user2try = True
  while user2try == True:
    try:
      user2guess = (await input('user2. input ur guess in colum, row.'))
      list = user2guess.split(',')
      user2col = int(list[0])-1
      user2row = int(list[1])-1
      if user1boats[user2row][user2col] == 1:
        user2grid[user2row][user2col] = 7
        #hit2 = hit2 + 1
        for i in range(0, 10):
          displaygrid(box22,user2grid)
      elif user1boats[user2row][user2col] == 0:
        user2grid[user2row][user2col] = 5
        for i in range(0, 10):
          displaygrid(box22,user2grid)
      player4_entry.config(state="disabled")
      user2try = False #
    except:
      print(Fore.RED +"co-ordinate is incorrect formate, please try again")
      
  btn4.config(state='normal')

# Define a function for switching the frames
def change_to_player1():
  player1.pack(fill='both', expand=1, side=tkinter.TOP)
  player2.pack_forget()

def change_to_player2():
  player2.pack(fill='both', expand=1, side=tkinter.BOTTOM)
  player1.pack_forget()

def change_to_Start1():
  start1.pack(fill='both', expand=1, side=tkinter.TOP)
  grids1.pack_forget()
  start2.pack_forget()
  grids2.pack_forget()
  btn1.config(state="normal")
  btn2.config(state="disabled")

def change_to_End1():
  grids1.pack(fill='both', expand=1, side=tkinter.BOTTOM)
  start2.pack_forget()
  start1.pack_forget()
  grids2.pack_forget()
  if placedboats:
    asynctkinter.start(player1_guesses())
    player3_entry.pack(fill='both', expand=1, side=tkinter.BOTTOM)
    player1_entry.pack_forget()
  else:
    asynctkinter.start(place_user1boats())
    player1_entry.pack(fill='both', expand=1, side=tkinter.BOTTOM)
    player3_entry.pack_forget()

def change_to_Start2():
  start2.pack(fill='both', expand=1, side=tkinter.TOP)
  grids2.pack_forget()
  start1.pack_forget()
  grids1.pack_forget()
  btn3.config(state="normal")
  btn4.config(state="disabled")

def change_to_End2():
  grids2.pack(fill='both', expand=1, side=tkinter.BOTTOM)
  start1.pack_forget()
  grids1.pack_forget()
  start2.pack_forget()
  if not placedboats:
    asynctkinter.start(place_user2boats())
    player2_entry.pack(fill='both', expand=1, side=tkinter.BOTTOM)
    player4_entry.pack_forget()
  else:
    asynctkinter.start(player2_guesses())
    player4_entry.pack(fill='both', expand=1, side=tkinter.BOTTOM)
    player2_entry.pack_forget()

#make the frame
root = tkinter.Tk()
root.title('BATTLESHIPS')

player1 = tkinter.Frame(root)
player2 = tkinter.Frame(root)

#player1
start1 = tkinter.Frame(player1)
grids1 = tkinter.Frame(player1)

boxup1 = tkinter.LabelFrame(player1, padx=0.5, pady=0.5)
box1 = tkinter.LabelFrame(grids1, text='user1boats', padx=0.5, pady=0.5)
box21 = tkinter.LabelFrame(grids1, text='user1grid', padx=0.5, pady=0.5)

#player2
start2 = tkinter.Frame(player2)
grids2 = tkinter.Frame(player2)

boxup2 = tkinter.LabelFrame(player2, padx=0.5, pady=0.5)
box2 = tkinter.LabelFrame(grids2, text='user2boats', padx=0.5, pady=0.5)
box22 = tkinter.LabelFrame(grids2, text='user2grid', padx=0.5, pady=0.5)

#making a font
font1 = font.Font(family='Helvetica', size='25', weight='bold')

#making the labels/grids player1
label1 = tkinter.Label(player1,text="Player1",foreground="red3",font=font1)
label1.pack(pady=5)
displaygrid(box1, user1boats)
displaygrid(box21, user1grid)

#making the labels/grids player2
label2 = tkinter.Label(player2,text="Player2",foreground="green3",font=font1)
label2.pack(pady=5)
displaygrid(box2, user2boats)
displaygrid(box22, user2grid)

#entry player1
store_player1_entry = tkinter.StringVar()
player1_entry = tkinter.Entry(grids1, textvariable=store_player1_entry)
player1_entry.pack(fill='x', expand=True, side=tkinter.BOTTOM, pady=10, padx=10)
player1_entry.focus()

#entry player2
store_player2_entry = tkinter.StringVar()
player2_entry = tkinter.Entry(grids2, textvariable=store_player2_entry)
player2_entry.pack(fill='x', expand=True, side=tkinter.BOTTOM, pady=10, padx=10)
player2_entry.focus()

#entry 3 for player 1's guesses
store_player3_entry = tkinter.StringVar()
player3_entry = tkinter.Entry(grids1, textvariable=store_player3_entry)
player3_entry.pack(fill='x', expand=True, side=tkinter.BOTTOM, pady=10, padx=10)
player3_entry.focus()

#entry 4 for player 2's guesses
store_player4_entry = tkinter.StringVar()
player4_entry = tkinter.Entry(grids2, textvariable=store_player4_entry)
player4_entry.pack(fill='x', expand=True, side=tkinter.BOTTOM, pady=10, padx=10)
player4_entry.focus()

#making the buttons
btn1 = tkinter.Button(boxup1,text="START",pady=10,padx=135,command=change_to_End1)
btn2 = tkinter.Button(boxup1,text="END",pady=10,padx=139,command=lambda: [change_to_Start2(), change_to_player2()])
btn3 = tkinter.Button(boxup2,text="START",pady=10,padx=135,command=change_to_End2)
btn4 = tkinter.Button(boxup2,text="END",pady=10,padx=139,command=lambda: [change_to_Start1(), change_to_player1()])

#pack() for all the the elements(this means that they will actualy update/display)
boxup1.pack(fill='x', side=tkinter.BOTTOM)
btn2.pack(pady=20, side=tkinter.RIGHT, fill='x')
btn1.pack(pady=20, padx=0, side=tkinter.LEFT, fill='x')
box1.pack(side=tkinter.LEFT)
box21.pack(side=tkinter.RIGHT)

boxup2.pack(fill='x', side=tkinter.BOTTOM)
btn4.pack(pady=20, side=tkinter.RIGHT, fill='x')
btn3.pack(pady=20, padx=0, side=tkinter.LEFT, fill='x')
box2.pack(side=tkinter.LEFT)
box22.pack(side=tkinter.RIGHT)

player1.pack()
player2.pack_forget()

#make start frame to display at the beginning
start1.pack(fill='both', expand=1, side=tkinter.TOP)
grids1.pack_forget()
start2.pack_forget()
grids2.pack_forget()
btn1.config(state="normal")
btn2.config(state="disabled")

root.mainloop()

win = '0'
hit1 = 0
hit2 = 0

while hit1 < 16 or hit2 < 16:
  print('this is not owrking yet')
  #user1
  #determins if u have won
if hit1 == 16:
  print('player 1 has won')
elif hit2 == 16:
  print('player 2 has won')
else:
  print('my code is broken')
