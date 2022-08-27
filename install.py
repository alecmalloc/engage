import subprocess
from tkinter.filedialog import askopenfilenames

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
    print("Please select the applications you would like to be opened by engage")
    apps_list = list(askopenfilenames(initialdir="/Applications/", title='Select your apps'))
    app_out_file = open("assets/app.txt", "w")
    for element in apps_list:
        app_out_file.write(element + ",")
    app_out_file.close()

    subprocess.call(['clear'])
    print("Great, now please enter the URL's engage should open in the following format: \n google.com,bing.com \n Press enter to submit \n")
    urls_input = input("")
    app_out_file = open("assets/urls.txt", "w")
    app_out_file.write(urls_input)

    




    





setup_lists()
