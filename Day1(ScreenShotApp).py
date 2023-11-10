import  time
import tkinter
import  pyautogui

def takeScreenShot():
    rname = int(round(time.time() * 1000))
    name = "{}.png".format(rname)
    time.sleep(1)
    img = pyautogui.screenshot(name)


root = tkinter.Tk()
appGUI = tkinter.Frame(root)
appGUI.pack()

srsbotton = tkinter.Button(appGUI, text="Take ScreenShot", activebackground="Green", command=takeScreenShot)
srsbotton.pack(side=tkinter.LEFT)

qbotton = tkinter.Button(appGUI, text="QUIT",  activebackground="Red", command=quit)
qbotton.pack(side=tkinter.RIGHT)

root.mainloop()
