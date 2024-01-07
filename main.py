# 1) import packages
from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
import time

DOWN_SPEED = None
UP_SPEED = None
EMAIL = "Twitter Email"
PASSWORD = "Twitter Password"


# 2) creating drive options
option = webdriver.ChromeOptions()
option.add_experimental_option("detach",True)
option.add_experimental_option("prefs",{
    "profile.default_content_setting_values.notifications": 1
})

# 3) creating drive
driver = webdriver.Chrome(options=option)
driver.maximize_window()
driver.get("https://www.speedtest.net/")

# continue
WebDriverWait(driver,100).until(EC.element_to_be_clickable((By.XPATH,'//*[@id="onetrust-accept-btn-handler"]'))).click()

# go
WebDriverWait(driver,100).until(EC.element_to_be_clickable((By.XPATH,'//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[1]/a'))).click()


time.sleep(50)
try:
    # get down speed
    DOWN_SPEED = driver.find_element(By.XPATH,'//*[@id="container"]/div/div['
                                                                         '3]/div/div/div/div[2]/div[3]/div[3]/div/div['
                                                                         '3]/div/div/div[2]/div[1]/div[1]/div/div['
                                                                         '2]/span')
    # get up speed
    UP_SPEED = driver.find_element(By.XPATH,'//*[@id="container"]/div/div['
                                                                         '3]/div/div/div/div[2]/div[3]/div[3]/div/div['
                                                                         '3]/div/div/div[2]/div[1]/div[2]/div/div['
                                                                         '2]/span')

except:
    # click close
    WebDriverWait(driver,100).until(EC.element_to_be_clickable((By.XPATH,'//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[8]/div/div/p[2]/button')))

    # get down speed
    DOWN_SPEED = driver.find_element(By.XPATH,'//*[@id="container"]/div/div['
                                                                         '3]/div/div/div/div[2]/div[3]/div[3]/div/div['
                                                                         '3]/div/div/div[2]/div[1]/div[1]/div/div['
                                                                         '2]/span')
    # get up speed
    UP_SPEED = driver.find_element(By.XPATH,'//*[@id="container"]/div/div['
                                                                         '3]/div/div/div/div[2]/div[3]/div[3]/div/div['
                                                                         '3]/div/div/div[2]/div[1]/div[2]/div/div['
                                                                         '2]/span')
else:
    print(f"Download speed {DOWN_SPEED.text}")
    print(f"Upload speed {UP_SPEED.text}")

# Tweet message
TWEET_TEXT = f"Hey @Internet_provider, i am getting just Downdload speed: {DOWN_SPEED.text} and Upload speed: {UP_SPEED.text}, where it is said to be 100mbps/s"

# Twitter login
driver.get("https://twitter.com/i/flow/login")

#  Email
WebDriverWait(driver,300).until(EC.element_to_be_clickable((By.XPATH,'//*[@id="layers"]/div/div/div/div/div/div/div['
                                                                     '2]/div[2]/div/div/div[2]/div['
                                                                     '2]/div/div/div/div[5]/label/div/div['
                                                                     '2]/div/input'))).send_keys(EMAIL)

#  Next
WebDriverWait(driver,300).until(EC.element_to_be_clickable((By.XPATH,'//*[@id="layers"]/div/div/div/div/div/div/div['
                                                                     '2]/div[2]/div/div/div[2]/div['
                                                                     '2]/div/div/div/div[6]/div'))).click()



try:
    # username
    WebDriverWait(driver,100).until(EC.element_to_be_clickable((By.XPATH,'//*[@id="layers"]/div/div/div/div/div/div/div['
                                                                         '2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div['
                                                                         '2]/label/div/div[2]/div/input'))).send_keys("Ej_065")

    #  Next
    WebDriverWait(driver,100).until(EC.element_to_be_clickable((By.XPATH,'//*[@id="layers"]/div/div/div/div/div/div/div['
                                                                         '2]/div[2]/div/div/div[2]/div[2]/div['
                                                                         '2]/div/div/div/div'))).click()

except:
    # Password
    WebDriverWait(driver,300).until(EC.element_to_be_clickable((By.XPATH,'//*[@id="layers"]/div/div/div/div/div/div/div['
                                                                         '2]/div[2]/div/div/div[2]/div[2]/div['
                                                                         '1]/div/div/div[3]/div/label/div/div[2]/div['
                                                                         '1]/input'))).send_keys(PASSWORD)
    # next
    WebDriverWait(driver,300).until(EC.element_to_be_clickable((By.XPATH,'//*[@id="layers"]/div/div/div/div/div/div/div['
                                                                         '2]/div[2]/div/div/div[2]/div[2]/div[2]/div/div['
                                                                         '1]/div/div/div'))).click()
else:
    # Password
    WebDriverWait(driver,300).until(EC.element_to_be_clickable((By.XPATH,'//*[@id="layers"]/div/div/div/div/div/div/div['
                                                                         '2]/div[2]/div/div/div[2]/div[2]/div['
                                                                         '1]/div/div/div[3]/div/label/div/div[2]/div['
                                                                         '1]/input'))).send_keys(PASSWORD)

    # next
    WebDriverWait(driver,300).until(EC.element_to_be_clickable((By.XPATH,'//*[@id="layers"]/div/div/div/div/div/div/div['
                                                                         '2]/div[2]/div/div/div[2]/div[2]/div[2]/div/div['
                                                                         '1]/div/div/div'))).click()



# tweet content
tweet = WebDriverWait(driver,300).until(EC.element_to_be_clickable((By.XPATH,'//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div/div/div[3]/div/div['
                                     '2]/div[1]/div/div/div/div[2]/div['
                                     '1]/div/div/div/div/div/div/div/div/div/div/label/div['
                                     '1]/div/div/div/div/div/div[2]/div/div/div/div')))
ActionChains(driver).click(tweet).perform()
tweet.send_keys(TWEET_TEXT)

# # tweet post
# WebDriverWait(driver,300).until(EC.element_to_be_clickable((By.XPATH,'//*[@id="react-root"]/div/div/div['
#                                                                      '2]/main/div/div/div/div/div/div[3]/div/div['
#                                                                      '2]/div[1]/div/div/div/div[2]/div[2]/div['
#                                                                      '2]/div/div/div/div'))).click()

