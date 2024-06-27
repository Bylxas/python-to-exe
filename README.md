Make sure you also download the dependencies
--------------------------------------------------------
use this code in visual studios or what ever dont forget its python




import os
import subprocess
import sys

def install(package):
    subprocess.check_call([sys.executable, "-m", "pip", "install", package])

def main():
    
    if sys.platform.startswith('linux'):
        try:
            subprocess.check_call(['sudo', 'apt-get', 'install', 'python3-tk'])
        except subprocess.CalledProcessError:
            print("Fehler bei der Installation von tkinter. Bitte manuell installieren.")
    
    
    install("requests")
    install("pyinstaller")
    print("Alle benötigten Pakete wurden installiert.")

if __name__ == "__main__":
    main()
