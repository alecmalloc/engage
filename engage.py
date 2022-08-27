import subprocess
import webbrowser
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

url_file = open("urls.txt", "r")
app_file = open("app.txt", "r")
url_content = url_file.read()
app_content = app_file.read()
url_list = url_content.split(",")
app_list = app_content.split(",")

app = QApplication([])
app.setQuitOnLastWindowClosed(False)

# Define the applications to be opened
def work_mode():

    for i in app_list:
        app_route = "/Applications/" + i + ".app"
        subprocess.Popen(["/usr/bin/open", "-a", app_route])

    for i in url_list:
        webbrowser.open_new(i)

# Create the icon
icon = QIcon("jet.png")

# Create the tray
tray = QSystemTrayIcon()
tray.setIcon(icon)
tray.setVisible(True)

# Create the menu
menu = QMenu()

# Execute work mode action
wm = QAction("Engage work mode")
wm.triggered.connect(work_mode)
menu.addAction(wm)

# Add a Quit option to the menu.
quit = QAction("Quit")
quit.triggered.connect(app.quit)
menu.addAction(quit)

# Add the menu to the tray
tray.setContextMenu(menu)

app.exec_()