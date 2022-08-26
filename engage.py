import subprocess
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

app = QApplication([])
app.setQuitOnLastWindowClosed(False)

# Define the applications to be opened
def work_mode():
    subprocess.Popen(["/usr/bin/open", "-a", "/Applications/Spotify.app"])
    subprocess.Popen(["/usr/bin/open", "-a", "/Applications/Brave Browser.app"])

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