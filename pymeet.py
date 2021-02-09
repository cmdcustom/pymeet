import pyautogui as pg, os, time

def micOff():
    oldPos = pg.position()
    micButton = pg.locateOnScreen("mic_logo-pyrecog.png")
    pg.moveTo(micButton)
    pg.click()
    pg.moveTo(oldPos)
    
def micOn():
   oldPos = pg.position()
   offMicButton = pg.locateOnScreen("ofm.png")
   pg.moveTo(offMicButton); pg.click(); pg.moveTo(oldPos)

def pullChat():
    chat = pg.locateOnScreen("chat-pyrecog.png")
    pg.moveTo(chat)
    pg.click()


   
    
