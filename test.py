from selenium import webdriver
import time
import logging

logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')

logger = logging.getLogger(__name__)

def test_success_credentials(input):
    passed = False
    driver = webdriver.Chrome()
    identifier, password = input


    driver.get("http://127.0.0.1:5000/")
    time.sleep(3)

    identifier_input = driver.find_element("name", "identifier")
    password_input = driver.find_element("name", "password")

    identifier_input.send_keys(identifier)
    password_input.send_keys(password)

    submit_button = driver.find_element("name", "submit")
    submit_button.click()

    driver.implicitly_wait(10)
    time.sleep(3)

    if "http://localhost:3000" in driver.current_url:
        passed = True

    driver.quit()

    return passed

def test_google():
    passed = False
    driver = webdriver.Chrome()

    driver.get("http://127.0.0.1:5000/")
    time.sleep(3)


    submit_button = driver.find_element("id", "submit-g")
    submit_button.click()

    time.sleep(3)

    try:
        submit_button = driver.find_element("css", "css=.wLBAL")
        submit_button.click()
    except:
        pass

    if "Signing in will redirect you to: http://127.0.0.1:5000" in driver.page_source:
        passed = True



    driver.implicitly_wait(10)
    time.sleep(3)


    if "http://localhost:3000" in driver.current_url:
        passed = True

    driver.quit()

    return passed

def map_location_visible():
    passed = False
    driver = webdriver.Chrome()

    driver.get("http://localhost:3000/")
    time.sleep(3)

    if "area" in driver.page_source:
        passed = True

    time.sleep(3)

    return passed


def sea_distance_visible():
    passed = False
    driver = webdriver.Chrome()

    driver.get("http://localhost:3000/")
    time.sleep(3)

    try:
        driver.find_element("id", "sea-distance")
        passed = True
    
    except:
        pass

    time.sleep(3)

    return passed

def zoom_visible():
    passed = False
    driver = webdriver.Chrome()

    driver.get("http://localhost:3000/")
    time.sleep(3)

    if "gm-control-active" in driver.page_source:
        passed = True

    time.sleep(3)

    return passed

def navbar_works():
    passed = False
    driver = webdriver.Chrome()

    driver.get("http://localhost:3000/")
    time.sleep(3)

    submit_button = driver.find_element("id", "earth-to-sun")
    submit_button.click()
    time.sleep(3)

    if "http://localhost:3000/earth-to-sun" in driver.current_url:
        passed = True

    return passed

def sun_distance_visible():
    passed = False
    driver = webdriver.Chrome()

    driver.get("http://localhost:3000/earth-to-sun")
    time.sleep(3)

    try:
        driver.find_element("id", "sun-distance")
        passed = True
    
    except:
        pass

    time.sleep(3)

    return passed

if __name__=="__main__":
    #4.1.1 Valid Credentials with Phone
    if test_success_credentials(("+905540244745", "1234$cdA6578")):
        logger.info("4.1.1 PASSED")

    else:
        logger.error("4.1.1 FAILED")

    #4.2.3 Password does not match with entered email
    if not test_success_credentials(("sahandmoslemi@gmail.com", "1231234321")):
        logger.info("4.2.3 PASSED")

    else:
        logger.error("4.2.3 FAILED")

    #4.1.2 Valid Google Authentication:
    if test_google():
        logger.info("4.1.2 PASSED")

    else:
        logger.error("4.1.2 FAILED")

    #4.4.1 Email input format is not valid:
    if not test_success_credentials(("sahandmoslemi-gmail.com", "12345678")):
        logger.info("4.4.1 PASSED")

    else:
        logger.error("4.4.1 FAILED")

    #4.2.1 Email input does not match:
    if not test_success_credentials(("erengazi@gmail.com", "1231234321")):
        logger.info("4.2.1 PASSED")

    else:
        logger.error("4.2.1 FAILED")

    #4.2.2 Phone input does not match:
    if not test_success_credentials(("5333333333", "1231234321")):
        logger.info("4.2.2 PASSED")

    else:
        logger.error("4.2.2 FAILED")

    #4.3.1 Email/phone field is empty:
    if not test_success_credentials(("", "1231234321")):
        logger.info("4.3.1 PASSED")

    else:
        logger.error("4.3.1 FAILED")

    #4.3.2 Password field is empty:
    if not test_success_credentials(("sahandmoslemi@gmail.com", "")):
        logger.info("4.3.2 PASSED")

    else:
        logger.error("4.3.2 FAILED") 

    #4.4.2 Phone input format is not valid:
    if not test_success_credentials(("53a1234567", "12345678")):
        logger.info("4.4.2 PASSED")

    else:
        logger.error("4.4.2 FAILED") 

    #1.1 Map location is visible for valid user:
    if map_location_visible():
        logger.info("1.1 PASSED")

    else:
        logger.error("1.1 FAILED")

    #1.2 Test if map zoom(+) button exist
    if zoom_visible():
        logger.info("1.2 PASSED")

    else:
        logger.error("1.2 FAILED")

    #1.3 Test if sea distance exists
    if sea_distance_visible():
        logger.info("1.3 PASSED")

    else:
        logger.error("1.3 FAILED")

    #2.1 Test if navbar button changes route
    if navbar_works():
        logger.info("2.1 PASSED")

    else:
        logger.error("2.1 FAILED")

    #3.1 Test if distance to sun exists
    if sun_distance_visible():
        logger.info("3.1 PASSED")

    else:
        logger.error("3.1 FAILED")