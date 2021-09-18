from PIL import Image
import requests
from io import BytesIO

print("""
███╗   ███╗ ██████╗     ██████╗ █████╗ ██████╗ ███████╗    ██████╗ ███████╗███╗   ██╗██████╗ ███████╗██████╗ 
████╗ ████║██╔════╝    ██╔════╝██╔══██╗██╔══██╗██╔════╝    ██╔══██╗██╔════╝████╗  ██║██╔══██╗██╔════╝██╔══██╗
██╔████╔██║██║         ██║     ███████║██████╔╝█████╗      ██████╔╝█████╗  ██╔██╗ ██║██║  ██║█████╗  ██████╔╝
██║╚██╔╝██║██║         ██║     ██╔══██║██╔═══╝ ██╔══╝      ██╔══██╗██╔══╝  ██║╚██╗██║██║  ██║██╔══╝  ██╔══██╗
██║ ╚═╝ ██║╚██████╗    ╚██████╗██║  ██║██║     ███████╗    ██║  ██║███████╗██║ ╚████║██████╔╝███████╗██║  ██║
╚═╝     ╚═╝ ╚═════╝     ╚═════╝╚═╝  ╚═╝╚═╝     ╚══════╝    ╚═╝  ╚═╝╚══════╝╚═╝  ╚═══╝╚═════╝ ╚══════╝╚═╝  ╚═╝                                                                                                                                                             

By RandomBackpack

""")

preview_image = True

height = "1000"
width = "400"
skin_hash = "c99e2a73aa0cdb54"
cape_hash = "8a6cc02cc86e43f1"
slim = ""
backwards_input = False
skin_hash = input("Enter your skin hash:\n")

slim_input = input("Would you like to render your skin in 'Slim' mode? [y/N]\n")

if backwards_input == False:
    backwards = ""
else:
    backwards = "&theta=210"

if slim_input == "y":
    slim = "&model=slim"

cape_input = input("Would you like to render a cape? [Y/n]\n")

if cape_input == "n":
    cape = ""
else:
    cape_hash = input("Enter your cape hash:\n")
    cape = f"&cape={cape_hash}"

base_url = f"https://render.namemc.com/skin/3d/body.png?skin={skin_hash}{cape}{backwards}{slim}&width={width}&height={height}"

response = requests.get(base_url)
img = Image.open(BytesIO(response.content))

if preview_image:
    img.show()

if cape_input != "n":
    img.save(f"./Renders/{skin_hash}_{cape_hash}.png")
else:
    img.save(f"./Renders/{skin_hash}.png")