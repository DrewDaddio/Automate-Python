# webscraper example

import bs4, requests

def getAmazonPrice(productUrl):
    res = requests.get(productUrl)
    res.raise_for_status()

    soup = bs4.BeautifulSoup(res.text, 'html.parser')
    # select  the css path to copy by inspecting the element
    soup.select('<span id="myfcst-tempf">69°F</span> ')
    
    return elems[0].text.strip()
    
    

price = getAmazonPrice('https://www.amazon.com/dp/B06W58QKH6/ref=s9_acsd_bw_wf_a_dlpc28ae_cdi_0?pf_rd_m=ATVPDKIKX0DER&pf_rd_s=center-1&pf_rd_r=XNWNZTDAYWJ1R7KK9Z1D&pf_rd_t=101&pf_rd_p=0&pf_rd_i=283155')
print(' The price is ' + price)
