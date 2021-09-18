# MCSkinRender

The Easiest Minecraft Skin Renderer!

## How To Get A Skin Hash

To get a Skin Hash, goto [NameMC's Skin Tab](https://namemc.com/minecraft-skins), and find a skin you like the look of. Click on the associated link and copy the piece of text after '/skin/' in the link.
For example, if my skin's link was [https://namemc.com/skin/c39310814f4bde6f](https://namemc.com/skin/c39310814f4bde6f), my Skin hash would be 'c39310814f4bde6f' (without the quotes).

## How To Get A Cape Hash

Getting a Cape Hash is done in very much the same way as getting a Skin Hash, but by navigating to the [NameMC Cape Tab](https://namemc.com/Capes) instead. Once there, click on the cape you would like to add to a skin. Then, to grab the hash, simply copy the piece of text after '/cape/'. So if my cape's link was [https://namemc.com/cape/1981aad373fa9754](https://namemc.com/cape/1981aad373fa9754), my Cape Hash would be '1981aad373fa9754' (without the quotes).

## How Renders Are Saved

Renders are saved in the 'Renders' folder, which is located in the root directory of the program. If for some reason the Renders folder does not exist, the program will create it upon finishing a succesful render. Renders are named in the following format:

`<Skin Hash>_<Cape Hash>.png`

or if your render has no cape:

`<Skin Hash>.png`

Examples of both of these name formats can be found in the 'Renders' folder when cloning the repository, or downloading a Release.

# Basic Usage

## Setup

To start off, let's clone the repository by navigating to our desired location and running `git clone https://github.com/53z/MCSkinRender`. Assuming you have Python installed, we can then run the program with the command `python3 main.py`.

## In The Program

Once you have run the program succesfully, you will be prompted to enter a "Skin Hash". This is a string of text which represents the skin you want to render. To find this string of text, please read [the "How To Get A Skin Hash" section](## How To Get A Skin Hash).
