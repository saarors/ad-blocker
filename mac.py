from setuptools import setup

APP = ['adblocker.py']
OPTIONS = {
    'argv_emulation': True,
    'packages': [], 
}

setup(
    app=APP,
    options={'py2app': OPTIONS},
    setup_requires=['py2app'],
)
