import tkinter
# pip install pillow
from PIL import Image, ImageTk


# Creates the window to be displayed
def createView(menuItems):
    window = tkinter.Tk()
    window.title("Lunch Specials")
    screenWidth = window.winfo_screenwidth()
    screenHeight = window.winfo_screenheight()
    window.geometry('{}x{}'.format(screenWidth, screenHeight))

    itemsFrame = tkinter.Frame(window)
    itemsFrame.pack(padx=50, pady=50)
    for i in range(len(menuItems)):
        item = menuItems[i]
        rawImage = 'images/{}.jpg'.format(i+1)
        itemPhoto = tkinter.PhotoImage(rawImage)
        itemImage = tkinter.Label(itemsFrame, image=itemPhoto)
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
