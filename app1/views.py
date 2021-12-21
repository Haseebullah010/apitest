from django.shortcuts import render

# Create your views here.
from django.http import JsonResponse

import json
import selenium
import time
from selenium import webdriver
import csv
from csv import reader
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from django.http import HttpResponse , HttpResponseRedirect

def vaidilty(request):
    chrome_options = Options()
    chrome_options.add_argument("--headless")


    try:
        driver = webdriver.Chrome(ChromeDriverManager().install(),options=chrome_options)
        driver.get('https://www.amazon.com/Razer-BlackShark-V2-Gaming-Headset/dp/B086PKMZ21?ref_=Oct_DLandingS_D_afd39db3_61&smid=ATVPDKIKX0DER')
        time.sleep(3)
        add_to_cart = driver.find_element_by_id("add-to-cart-button")
        add_to_cart.click()
        time.sleep(3)
        driver.get('https://www.amazon.com/gp/cart/view.html?ref_=nav_cart')
        time.sleep(3)
        a_input=driver.find_element_by_name("proceedToRetailCheckout")
        a_input.click()
        time.sleep(3)
        emial=driver.find_element_by_name("email")
        emial.clear()
        emial.send_keys("haseebtarar72@gmail.com")
        con=driver.find_element_by_id("continue")
        con.click()
        time.sleep(3)
        pas=driver.find_element_by_name("password")
        pas.clear()
        pas.send_keys("Haseebullah@12")
        signin = driver.find_element_by_id("signInSubmit")
        signin.click()
        time.sleep(3)

        proced=driver.find_element_by_class_name("a-button-inner")
        proced.click()
        time.sleep(5)

        promo=driver.find_element_by_class_name("a-expander-prompt")
        promo.click()
        time.sleep(5)

        prom=driver.find_element_by_name("ppw-claimCode")
        prom.clear()
        prom.send_keys("abc")
        time.sleep(5)

        apply_promo=driver.find_element_by_name("ppw-claimCodeApplyPressed")
        apply_promo.click()
        time.sleep(5)

        try:
            if driver.find_element_by_class_name("a-list-item").size != 0:
                jason_response= {
                    'value':"not valid",
                    'link':"https://www.amazon.com/gp/cart/view.html?ref_=nav_cart"
                    
                }
                return JsonResponse(jason_response)
            else:
                jason_response= {
                    'value':"not valid",
                    'link':"https://www.amazon.com/gp/cart/view.html?ref_=nav_cart"
                }

                return JsonResponse(jason_response)
        
        except:
            pass

    except:
        print("ok")

    return HttpResponse("o")    

def base(request):

    return render(request,"base.html")