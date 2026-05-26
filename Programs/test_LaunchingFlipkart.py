from selenium.webdriver import Chrome,ChromeOptions
from time import sleep

opts = ChromeOptions()
opts.add_experimental_option("detach",True)
opts.add_argument("--start-maximized")


driver = Chrome(opts)
driver.get("https://www.flipkart.com/")
# driver.maximize_window()
sleep(3)
search = driver.find_element("name","q")
search.send_keys("Iphone")
search.submit()
print("Successfully Launched")
sleep(3)
driver.close() # Used to close the browser