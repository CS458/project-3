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