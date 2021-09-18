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

height = "1000"
width = "400"
skin_hash = "c99e2a73aa0cdb54"
cape_hash = "8a6cc02cc86e43f1"
slim = ""

skin_hash = input("Enter your skin hash:\n")

slim_input = input("would you like to render your skin in 'Slim' mode? [y/N]\n")

if slim_input == "y":
    slim = "&model=slim"

cape_input = input("Would you like to render a cape? [Y/n]\n")

if cape_input == "n":
    cape = ""
else:
    cape_hash = input("Enter your cape hash:\n")
    cape = f"&cape={cape_hash}&theta=210"

base_url = f"https://render.namemc.com/skin/3d/body.png?skin={skin_hash}{cape}{slim}&width={width}&height={height}"

response = requests.get(base_url)
img = Image.open(BytesIO(response.content))
if cape_input == "y":
    img.save(f"./Renders/{skin_hash}_{cape_hash}.png")
else:
    img.save(f"./Renders/{skin_hash}.png")