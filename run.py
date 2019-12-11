from scraper import getMenuItems
from view import createView
# pip install tkinter
from tkinter import *


def getAndCreateView():
    menuItems = getMenuItems()
    '''
    # for testing purposes
    menuItems = [{'name': 'Club Sandwich',
                  'description': 'chicken breast, bacon, tomato, lettuce, cheese, avocado & aioli on turkish with chips',
                  'price': '11.00'},
                 {'name': 'Fish & Chips',
                  'description': 'beer battered fish & chips with salad & tartare sauce',
                  'price': '11.00'},
                 {'name': 'Jalapeno Fish Tails & Chips',
                  'description': 'crumbed jalapeno fish tails served with chips, salad & tartare sauce',
                  'price': '11.00'}]'''
    createView(menuItems)
    return


getAndCreateView()

window = Tk()
window.title("Today's Specials")
window.geometry("400x200")

status = Label(window, text="DONE")
status.pack()

done = Label(window, text="You can now close this window.")
done.pack()

window.mainloop()

print('DONE')
