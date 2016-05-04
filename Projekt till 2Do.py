import webbrowser
import urllib
import console
import time
import clipboard

# importerar text från urklippet
text_from_drafts = str(clipboard.get())

# delar texten från urklippen vid radbrytning och lägger till i lista
tasks = text_from_drafts.splitlines()

# definerar första objektet i listan tasks som projekt
project = tasks[0]

# definerar listan med projektets uppgifter
project_tasks = tasks[1:]

# loopar genom listan med projektets uppgifter och lägger till dem under projektet i 2Do
for t in project_tasks:
    encoced_task = urllib.quote(t)
    encoded_project = urllib.quote(project)
    webbrowser.open('twodo://x-callback-url/add?task=' + encoced_task + '&forlist=Inkorg&forparentname=' + encoded_project + '&x-success=pythonista://')
    time.sleep(1)
    while console.is_in_background():
        time.sleep(1)
    time.sleep(1)
    while console.is_in_background():
        time.sleep(1)
