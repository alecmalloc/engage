import subprocess
import webbrowser
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *


# Fetch list of apps and Urls.

url_install_path = """
/Users/stuart/Desktop/engage/assets/urls.txt
"""
app_install_path = """
/Users/stuart/Desktop/engage/assets/apps.txt
"""
icon_install_path = """
/Users/stuart/Desktop/engage/assets/jet.png
"""

url_path = url_install_path.replace('\n', '')
app_path = app_install_path.replace('\n', '')
icon_path = icon_install_path.replace('\n', '')


url_file = open(url_path, "r")
app_file = open(app_path, "r")
url_content = url_file.read()
app_content = app_file.read()
url_list = url_content.split(",")
app_list = app_content.split(",")

app = QApplication([])
app.setQuitOnLastWindowClosed(False)

# Function to open apps and urls by iterating over a list.
def work_mode():
    for i in app_list:
        subprocess.Popen(["/usr/bin/open", "-a", i])

    for i in url_list:
        url_full = "https://www." + i
        webbrowser.open_new(url_full)

# Create the icon
icon = QIcon(icon_path)

# Create the tray
tray = QSystemTrayIcon()
tray.setIcon(icon)
tray.setVisible(True)

# Create the menu
menu = QMenu()

# Execute work mode action on click
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