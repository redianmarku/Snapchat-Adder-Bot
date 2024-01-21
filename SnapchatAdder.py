from appium import webdriver
from appium.options.android import UiAutomator2Options
from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep
import os

options = UiAutomator2Options().load_capabilities({
"platformName": "Android",
"platformVersion": "13",
"deviceName": "emulator-5554",
"appActivity": "com.snapchat.android.LandingPageActivity",
"appPackage": "com.snapchat.android",
"autoGrantPermissions": True,
"noReset" : True,
"fullReset": False,
"disableIdLocatorAutocompletion": True,
})

message = input("What message you want to send to people: ")

def click_element(driver,element_id,type=AppiumBy.ID):
    element = WebDriverWait(driver, 30).until(
    EC.element_to_be_clickable((type, element_id))
  
)
    element.click()

    
def type_element(driver,element_id,text):
    element = WebDriverWait(driver, 30).until(
    EC.element_to_be_clickable((AppiumBy.ID, element_id))
  
)
    element.click()
    element.send_keys(text)

    

driver = webdriver.Remote("http://127.0.0.1:4723", options=options)


while(True):
    click_element(driver,"com.snapchat.android:id/hova_header_add_friend_icon")
    for i in range(1,4):
        m = i-1
        click_element(driver,f"(//android.widget.Button[@content-desc=\"Add\"])[1]",AppiumBy.XPATH)
        sleep(1)
        try:
            msgButton = driver.find_elements(AppiumBy.ID,"scu_quick_add_chat")
            msgButton[m].click()
        except:
            continue
        type_element(driver,"com.snapchat.android:id/chat_input_text_field",message)
        driver.press_keycode(66) 
        click_element(driver,"com.snapchat.android:id/back_button")
    driver.press_keycode(4)

