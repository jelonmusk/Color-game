import tkinter
import  random
import  sys
import  os
import numpy

colors = ['Red','Blue','Green','Pink','Black',
           'Yellow','Orange','White','Purple','Brown']
score = 0

timeleft=40
def restart_program():
    """Restarts the current program.
    Note: this function does not return. Any cleanup action (like
    saving data) must be done before calling this function."""
    python = sys.executable
    os.execl(python, python, * sys.argv)


#game starts
def startGame(event):
    if timeleft == 40:
        countdown()
    #elif timeleft == 0 :

    nextColor()

#colored text
def nextColor():

    global  score
    global timeleft
    if timeleft > 0:
        a.focus_set()

        if a.get().lower() == colors[1].lower():
            score += 1

        a.delete(0,tkinter.END)

        random.shuffle(colors)

        label.config(bg="#A3E4D7",fg=str(colors[1]),text=str(colors[0]))

        scorelbl.config(text="Score: "+str(score))





def countdown():
    global timeleft
    if timeleft > 0:
        timeleft-=1

        timeLabel.config(text="Time Left :"+ str(timeleft))

        timeLabel.after(1000,countdown)
    else :
        #show gameover label

        gameOverlbl = tkinter.Label(window, text="GAME OVER. PRESS RESTART TO TRY AGAIN",
                                    font=("Helvetica", 14),
                                     fg="#CD5C5C", bg="#A3E4D7").pack()
        #restart button
        tkinter.Button(window, text="Restart", command=restart_program).pack()



window =tkinter.Tk()
window.title("Shake it Off")
window.configure(bg="#A3E4D7")
window.geometry("640x480")

#rules/instructions
rules=tkinter.Label(window,text="Type in the colour"
                        " of the words, and not the word text!",
                    font=("Helvetica",14),fg="#CD5C5C",
                    pady=10,bd=15,bg="#A3E4D7")
rules.pack()

#score labels
scorelbl=tkinter.Label(window,text="Press Enter to Start",
                       font=("Helvetica",14),bg="#A3E4D7",fg="#F39C12",
                       height=3,padx=4)
scorelbl.pack()

## add a time left label
timeLabel = tkinter.Label(window,height=3,pady=2, bg="#A3E4D7",
                          text = "Time left: " + str(timeleft),
                          font = ('Helvetica', 14))
timeLabel.pack()



#label to display colored text
label=tkinter.Label(window,bg="#A3E4D7",font=('Helvetica',50))
label.pack()


#text entry input box for answers
a=tkinter.Entry()
a.place(width=40,height=400)
window.bind('<Return>',startGame)
a.pack()

a.focus_set()



while 1:
    window.mainloop()