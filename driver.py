#Use command "pythonw driver.py" in this directory to run 24/7

#imports
from plyer import notification
from bs4 import BeautifulSoup
import requests

if __name__ == "__main__":


    notification.notify(title = 'hiol', 
                    message = 'hello', 
                    app_icon = "uofm.ico", 
                    timeout = 10, 
                    ticker = 'r',
                    toast = False
                    )


