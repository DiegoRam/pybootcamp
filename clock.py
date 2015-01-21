import Tkinter
from time import strftime

clock = Tkinter.Label()
 
clock.pack()
clock['font'] = 'Helvetica 120 bold'
clock['text'] = strftime('%H:%M:%S')
 
def tictac():
    ahora = strftime('%H:%M:%S')
    if ahora != clock['text']:
        clock['text'] = ahora
    clock.after(100, tictac)
 
tictac()
clock.mainloop()