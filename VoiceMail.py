from selenium import webdriver
import logging
import os
import subprocess
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import TimeoutException
from selenium.common.exceptions import NoAlertPresentException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import StaleElementReferenceException
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import ElementNotInteractableException
from dotenv import load_dotenv
import PIL
from PIL import Image
import io
import requests
from chromedriver_py import binary_path

# import environment variables
load_dotenv(".env")

# point logger to log file
logging.basicConfig(filename='./Log.log', level=logging.INFO)

# Create headless browser
chrome_options = Options()
chrome_options.add_argument("window-size=1920,1080")
chrome_options.add_argument("headless")
driver = webdriver.Chrome(executable_path=binary_path, options=chrome_options)
wait = WebDriverWait(driver, 20)

# Save screenshots
def __save_elem_screenshot(element, filename):
    try:
        image = element.screenshot_as_png
        imageStream = io.BytesIO(image)
        im = Image.open(imageStream)
        im.save(os.getcwd() + "/" + filename)
        logging.info("Screenshot Saved")
    except Exception as e:
        logging.error(f"Exception occured: {str(e)}", exc_info=True)

# Login to Voicemail Web Portal
def __login():
    try:
        driver.get(str(os.getenv("LINK")))
        frame = wait.until(EC.presence_of_element_located(
            (By.XPATH, "html/frameset/frame")))
        driver.switch_to.frame(frame)
        print("Focus switched to Frame")
        mailbox = wait.until(
            EC.presence_of_element_located((By.ID, "mailbox")))
        sec_code = wait.until(
            EC.presence_of_element_located((By.ID, "password")))
        mailbox.send_keys(os.getenv("NUM"))
        sec_code.send_keys(os.getenv("SEC_CODE"))
        print("Credentials Entered")
        submit = wait.until(EC.presence_of_element_located(
            (By.CLASS_NAME, "submit")))
        submit.click()
    except Exception as e:
        logging.error(f"Exception occured: {str(e)}", exc_info=True)

# Change voicemail to automated mode
def __change_settings():
    try:
        settings = wait.until(EC.presence_of_element_located(
            (By.ID, "menu_item_personal")))
        settings.click()
        out_office_checkbox = wait.until(
            EC.presence_of_element_located((By.ID, "enable_out_of_office")))
        out_office_checkbox.click()
        logging.info("Automated Voicemail Enabled")
        ok_button = wait.until(EC.presence_of_element_located((By.ID, "ok")))
        ok_button.click()
        logging.info("Out Of Office Confirmed")
        # Javascript to write date and time
        driver.execute_script("""var userInfo = document.getElementsByClassName('userInfo'); 
        	var d = new Date(); 
        	var month = d.getMonth() + 1; 
        	var day = d.getDate(); 
        	var year = d.getFullYear(); 
        	userInfo[0].innerText= month + '/' + day + '/' + year; 
    	"""
                              )
        driver.execute_script("""document.body.style.zoom='270%';""")
        logging.info("Timestamp Javascript executed")
        html = wait.until(
            EC.presence_of_element_located((By.TAG_NAME, "html")))
        __save_elem_screenshot(html, "Close.png")
        driver.execute_script(
            f"window.location.href='{str(os.getenv('LOGOUT'))}';")
        logging.info("Logged out of Webmail App")
        driver.close()
        driver.quit()
        logging.info("Browser Destroyed")
    except Exception as e:
        logging.error(f"Exception occured: {str(e)}", exc_info=True)

# login and change settings
def close():
    __login()
    __change_settings()

# main method
if __name__=="__main__":
    close()
