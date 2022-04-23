import requests
import bs4

#Function that checks if item is in stock 
def footlocker_monitor():
    #requesting session connect and getting url
    
    session = requests.Session()
    #headers acts as if a real computer is connecting to site
    headers = {  'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36'
    }
    #url to site
    url = 'Insert footlocker item link here'
    #requests the page
    
    res = requests.get(url, headers=headers)
    
    
    res.raise_for_status()
    #checks if link and connection goes through 
    
    soup = bs4.BeautifulSoup(res.content, 'html.parser')
    
    cart = soup.find(class_='Button ProductDetails-form__action').text
    
    #gets the price and if item is in stock 
    price = soup.find(class_='ProductPrice').text   
    print('the price is', price)
    print(cart)
    
    if cart == ('Add To Cart'):
        print('in stock')
    else:
        print('out of stock')
footlocker_monitor()


    
    
    
    