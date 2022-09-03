import subprocess
from tkinter.filedialog import askopenfilenames
from pathlib import Path
script_dir = Path( __file__ ).parent.absolute()



subprocess.call(['clear'])

print("Welcome to the Engage installer. To proceed press any key... \n")
input("")

def install_dependencies():
    subprocess.call(['pip3', 'install', 'py2app'])
    subprocess.call(['pip3', 'install', 'PyQt5'])
    subprocess.call(['brew', 'install', 'python-tk'])
    subprocess.call(['clear'])

def setup_lists():
    subprocess.call(['clear'])
    print("Please select the applications you would like to be opened by engage \n")
    apps_list = list(askopenfilenames(initialdir="/Applications/", title='Select your apps'))
    app_out_file = open("assets/apps.txt", "w")
    for element in apps_list:
        app_out_file.write(element + ",")
    app_out_file.close()

    subprocess.call(['clear'])
    print("Great, now please enter the URL's engage should open in the following format: \ngoogle.com,bing.com \nPress enter to submit \n")
    urls_input = input(":")
    url_out_file = open("assets/urls.txt", "w")
    url_out_file.write(urls_input)
    url_out_file.close()

def change_paths():
    engage_lines = open("engage.py", "r")
    list_lines = engage_lines.readlines()
    list_lines[9] = str(script_dir) + "/assets/urls.txt\n"
    list_lines[12] = str(script_dir) + "/assets/apps.txt\n"
    list_lines[15] = str(script_dir) + "/assets/jet.png\n"
    with open('engage.py', 'w') as file:
        file.writelines(list_lines)
        engage_lines.close
    setup_lines = open("setup.py", "r")
    list_lines = setup_lines.readlines()
    list_lines[4] = "'" + str(script_dir) + "/assets/urls.txt,'\n"
    list_lines[5] = "'" + str(script_dir) + "/assets/apps.txt,'\n"
    list_lines[6] = "'" + str(script_dir) + "/assets/jet.png\'\n"
    list_lines[9] = "'iconfile': '" + str(script_dir) + "/assets/jet.png\'\n"
    with open('setup.py', 'w') as file:
        file.writelines(list_lines)
        setup_lines.close

def build_application():
    subprocess.call(['python3', 'setup.py', 'py2app', '-A'])
    subprocess.call(['mv', 'dist/engage.app', '/Applications'])
    subprocess.call(['clear'])
    print("Engage has now been installed in your /Applications ! Feel free to exit this window and use your new app :)")


install_dependencies()
setup_lists()
change_paths()
build_application()