import tkinter
import os
# pip install pillow
from PIL import Image, ImageTk


# Creates the window to be displayed
def createView(menuItems):
    window = tkinter.Tk()
    window.title("Lunch Specials")
    screenWidth = window.winfo_screenwidth()
    screenHeight = window.winfo_screenheight()
    window.geometry('{}x{}'.format(screenWidth, screenHeight))

    dawsonLogoImage = Image.open('resources/DawsonLogo.gif')
    dawsonLogoPhoto = ImageTk.PhotoImage(dawsonLogoImage)
    dawsonLogoLabel = tkinter.Label(window, image=dawsonLogoPhoto)
    dawsonLogoLabel.image = dawsonLogoPhoto
    dawsonLogoLabel.grid(row=0, column=0)

    itemsFrame = tkinter.Frame(window)
    itemsFrame.grid(row=1, column=0)
    for i in range(len(menuItems)):
        item = menuItems[i]
        rawImage = Image.open('images/{}.gif'.format(i+1))
        itemPhoto = ImageTk.PhotoImage(rawImage)
        itemImage = tkinter.Label(itemsFrame, image=itemPhoto)
        itemImage.image = itemPhoto
        itemImage.grid(row=2*i, rowspan=2, column=0)
        itemName = tkinter.Label(
            itemsFrame, text=item['name'], fg='black')
        itemName.grid(row=2*i, column=1, sticky='W')
        itemDescription = tkinter.Label(
            itemsFrame, text=item['description'], fg='gray')
        itemDescription.grid(row=2*i+1, column=1, sticky='W')
        itemPrice = tkinter.Label(
            itemsFrame, text=item['price'], fg='black')
        itemPrice.grid(row=2*i, column=2, sticky='E')

    window.mainloop()
