import os
choose = input("Choose your environment: [0] pip / [1] pip3 : ")
if choose == "0":
    os.system('pip install colorama')
    os.system('pip install pyinstaller')
    os.system('pip install nuitka')
elif choose == "1":
    os.system('pip3 install colorama')
    os.system('pip3 install pyinstaller')
    os.system('pip3 install nuitka')