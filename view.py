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
    dawsonLogoLabel = tkinter.Label(window, image=dawsonLogoPhoto, bg='purple')
    dawsonLogoLabel.image = dawsonLogoPhoto
    dawsonLogoLabel.grid(row=0, column=0)

    itemsFrame = tkinter.Frame(window)
    # itemsFrame.place(relx=0.1, rely=0.1, relheight=0.8, relwidth=0.8)
    itemsFrame.grid(row=1, column=0)
    for i in range(len(menuItems)):
        item = menuItems[i]
        rawImage = Image.open('images/{}.gif'.format(i+1))
        itemPhoto = ImageTk.PhotoImage(rawImage)
        itemImage = tkinter.Label(itemsFrame, image=itemPhoto, bg='black')
        itemImage.image = itemPhoto
        itemImage.grid(row=2*i, rowspan=2, column=0)
        # itemImage.place(relwidth=0.3, rely=i/len(menuItems), relx=0.0)
        itemName = tkinter.Label(
            itemsFrame, text=item['name'], fg='black', bg='green')
        itemName.grid(row=2*i, column=1, sticky='W')
        # itemName.place(relwidth=0.5, relheight=1 /
        #               len(menuItems), rely=i/len(menuItems)/2, relx=0.3)
        itemDescription = tkinter.Label(
            itemsFrame, text=item['description'], fg='gray', bg='red')
        itemDescription.grid(row=2*i+1, column=1, sticky='W')
        # itemDescription.place(relwidth=0.5, relheight=1/len(menuItems)/2,
        #                      rely=i/len(menuItems) + 0.1, relx=0.3)
        itemPrice = tkinter.Label(
            itemsFrame, text=item['price'], fg='black', bg='blue')
        itemPrice.grid(row=2*i, column=2, sticky='E')
        # itemPrice.place(relwidth=0.2, relheight=1 /
        #                len(menuItems), rely=i/len(menuItems), relx=0.8)

    window.mainloop()
