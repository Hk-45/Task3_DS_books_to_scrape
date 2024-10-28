import requests as rq
from bs4 import BeautifulSoup
import pandas as pd

bUrl = 'https://books.toscrape.com/'

bHeaders = {
      'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 Safari/537.36'
}

bResp = rq.get(url=bUrl, headers=bHeaders)
bSoup = BeautifulSoup(bResp.content,'html.parser')
books = bSoup.find_all('article', attrs={'class':'product_pod'})

titleName =[]
for bookTitle in books:
   title = bookTitle.h3.a["title"]
   #print('title =',title)

   titleName.append({'name':title})

# titleName = [{'Name':title} for bookTitle in books]

print('titleName :',titleName)

titleDf = pd.DataFrame(titleName)
titleDf.to_csv('bookTitle.csv')
print()

bookPricing = []
for bookPrice in books:
   price = bookPrice.find('p',attrs={'class':'price_color'}).text
   #print('bookPrice =',price)

   bookPricing.append({'pricing':price})

#pricing = [{'Price':price}for bookPrice in books]

print('bookPrice :',bookPricing)
priceDf = pd.DataFrame(bookPricing)
priceDf.to_csv('bookPrice.csv')
print()

booksRating =[]
for bookRating in books:
    rating = bookRating.find('p',attrs={'class':'star-rating'})['class']
    #print('bookRating =',rating)
    
    booksRating.append({'rating':rating})

print('bookRating :',booksRating)
ratingDf = pd.DataFrame(booksRating)
ratingDf.to_csv('bookRating.csv')





#   print('title=', title)
#   print('price =', price)
#   print('rating =', rating)

# for bookPrice in price:
#     print('bookPrice :',bookPrice.text)

# booksPrice = [ {'Price':bookPrice.text} for bookPrice in price]

# print('booksPrice',booksPrice)

# for bookRating in rating:
#     print('rating :',bookRating)

# booksRating =[{'rating':bookRating} for bookRating in rating]

# print('booksRating',booksRating)
