from setuptools import setup

APP = ['engage.py']
DATA_FILES = [
'/Users/stuart/Desktop/engage/assets/urls.txt,'
'/Users/stuart/Desktop/engage/assets/apps.txt,'
'/Users/stuart/Desktop/engage/assets/jet.png'
]
OPTIONS = {'argv_emulation': True,
'iconfile': '/Users/stuart/Desktop/engage/assets/jet.png'
 }

setup(
    app=APP,
    data_files=DATA_FILES,
    options={'py2app': OPTIONS},
    setup_requires=['py2app'],
)