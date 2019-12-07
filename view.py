import tkinter
from run import getMenuItems

# menuItems = getMenuItems()

# for testing purposes
menuItems = [{'name': 'Club Sandwich',
              'description': 'chicken breast, bacon, tomato, lettuce, cheese, avocado & aioli on turkish with chips',
              'price': '11.00'},
             {'name': 'Fish & Chips',
              'description': 'beer battered fish & chips with salad & tartare sauce',
              'price': '11.00'},
             {'name': 'Jalapeno Fish Tails & Chips',
              'description': 'crumbed jalapeno fish tails served with chips, salad & tartare sauce',
              'price': '11.00'}]

window = tkinter.Tk()
window.title("Lunch Specials")

itemsFrame = tkinter.Frame(window).pack()
indvItemFrames = []
for item in menuItems:
    fullFrame = tkinter.Frame(itemsFrame).pack()
    textFrame = tkinter.Frame(fullFrame).pack(side='left')
    itemName = tkinter.Label(
        textFrame, text=item['name'], fg='black').pack(side='left')
    itemDescription = tkinter.Label(
        textFrame, text=item['description'], fg='gray').pack(side='left')
    itemPrice = tkinter.Label(
        fullFrame, text=item['price'], fg='black').pack(side='right')
    indvItemFrames.append(fullFrame)

window.mainloop()
