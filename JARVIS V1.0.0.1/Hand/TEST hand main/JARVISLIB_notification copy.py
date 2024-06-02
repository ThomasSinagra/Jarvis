import pync

def afunction():
    print("Done")

def sendnotification(message):
    pync.notify(message, title='JARVIS', sound='default', appIcon="JARVIS.png")

