import os

try:
    os.system('pyinstaller backdoor.py --onefile --noconsole && rm -rf build __pycache__ && rm backdoor.spec ')
except:
    os.system('pyinstaller backdoor.py --onefile --noconsole && rm -rf build && rm backdoor.spec ')