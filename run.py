from scraper import getMenuItems
from view import createView
import tkinter

window = tkinter.Tk()
window.title("Today's Specials")

label = tkinter.Label(window, text = "Loading, please wait.")
label.place(relx = 0.5, rely = 0.5)

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

label['text'] = "DONE, you can now close this window."
print('DONE')
