# A simple Web Scraper

import webbrowser, sys, pyperclip

webbrowser.open('')
#Check if command line arguments were passed
if len(sys.argv) > 1:
  product = ' '.join(sys.argv[1:])
  product = product.replace(" ", "+")
  print (product)
  print ('https://www.amazon.ca/s?k='+product+'&ref=nb_sb_noss_1')
else:
  product = pyperclip.paste()
  print ("product")
#https://www.amazon.ca/s?k=<product>&ref=nb_sb_noss_1

webbrowser.open('https://www.amazon.ca/s?k='+product+'&ref=nb_sb_noss_1')
