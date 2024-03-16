import pyfiglet
import pystyle
from pystyle import Colors, Colorate

name = input("Please Enter Your Name: ")
DreamJob = input("Please Enter Your Dream Job: ")

FancyName = pyfiglet.figlet_format(name, font='isometric1')
print(Colorate.Horizontal(Colors.rainbow, FancyName))

FancyJobName = pyfiglet.figlet_format(DreamJob, font='isometric1')
print(Colorate.Horizontal(Colors.rainbow, FancyJobName))

