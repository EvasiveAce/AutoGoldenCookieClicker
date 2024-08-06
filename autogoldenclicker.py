import os.path
import threading

from win32api import GetSystemMetrics
import win32gui
import pyautogui
import customtkinter
from PIL import Image
from PIL import ImageTk

#brown \/
color2 = (113, 70, 32)
color = (235, 226, 120)
#purple \/
#color = (217, 60, 240)

width = GetSystemMetrics(0)
height = GetSystemMetrics(1)

running = False



#def check_screen():
#    for y in range(30, height - 1, 100):
#        for x in range(10, width - 1, 50):
#            pos = w.GetPixel(w.GetDC(w.GetActiveWindow()), x, y)
            #pyautogui.moveTo(x, y, duration = 0)
#            print(w.GetPixel(w.GetDC(w.GetActiveWindow()), pyautogui.position().x, pyautogui.position().y))
#            if hex(pos) == 0xd93cf0:
#                print(pos)
#                position = pos
#                print(position)


def screen_shot():
    s = pyautogui.screenshot()
    for x in range(s.width):
        for y in range(s.height):
            if s.getpixel((x, y)) == color or s.getpixel((x, y)) == color2:
                pyautogui.click(x, y)
                return


def thread_to_run():
    while running:
        screen_shot()

w = win32gui

def button_start():
    global running
    running = True
    textDisplay.configure(text="Status: Clicking")
    threading.Thread(target=thread_to_run, args=(), daemon=True).start()

def button_stop():
    global running
    running = False
    textDisplay.configure(text="Status: Stopped")
    #window['status'].update('Status: Stopped')

basedir = os.path.dirname(__file__)

app = customtkinter.CTk()

app.title("Automatic Golden Cookie Clicker")
app.geometry("225x150")
app.wm_iconbitmap(False, os.path.join(basedir, "goldCookie.ico"))
textDisplay = customtkinter.CTkLabel(app, text="Status: Stopped", width=220)
textDisplay.grid(row=0, column=0, padx=0, pady=0)

startButton = customtkinter.CTkButton(app, text="Start", command=button_start, fg_color="#84542c", hover_color="#b6b075")
startButton.grid(row=1, column=0, padx=10, pady=10)
endButton = customtkinter.CTkButton(app, text="Stop", command=button_stop, fg_color="#d41c09", hover_color="#f24e16")
endButton.grid(row=2, column=0, padx=10, pady=10)

app.mainloop()

# sg.theme('SystemDefault')
#
# layout = [[sg.Text('Press start and open Cookie Clicker to begin.', size=(32, 1))],
#           [sg.Text('Status: Stopped', size=(16, 1), key='status')],
#           [sg.Button('Start'), sg.Button('Stop')]]
#
# window = sg.Window('Automatic Golden Cookie Clicker', layout, finalize=False)
#
# while True:
#     event, values = window.read()
#     if event == sg.WIN_CLOSED:
#         break
#     if event == 'Start':
#         window['status'].update('Status: Clicking')

#     if event == 'Stop':
#         running = False
#         window['status'].update('Status: Stopped')
#
#
# window.close()