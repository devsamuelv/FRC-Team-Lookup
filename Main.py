from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from util import util
from util import vars

# use this for email checking

driver_options = Options()

# headless turns off the window
driver_options.add_argument("--headless")
driver_options.add_argument("--disable-extensions")
driver_options.add_argument("--disable-gpu")
# driver_options.add_argument("--no-sandbox") # linux only

# start the driver and add options
driver = webdriver.Firefox(options=driver_options)

teamNumber = input("\033[33m" + "Input FRC Team Number >> ")

# checks if the element exists
def CheckExists(xpath):
    try:
        driver.find_element_by_xpath(xpath)
    except NoSuchElementException:
        return False
    return True

# this is the Main Function
def main():
    CurrentURL = vars.defaultURL + teamNumber

    info = ""
    From = ""
    website = ""
    name = ""
    robotName = ""

    if util.sendRequest(CurrentURL) == False:
        print("\033[31m" + "ERROR: Sorry That Team Number is Incorrect" + "\033[39m")
        driver.close()
        exit()
    else:
        driver.get(CurrentURL)
        pass

    if driver.current_url != CurrentURL:
        return

    if CheckExists(vars.teamInfoXPath) == False:
        info = "None"
    else:
        info = driver.find_element_by_xpath(vars.teamInfoXPath).text

    if CheckExists(vars.teamFromXPath) == False:
        From = "None"
    else:
        From = driver.find_element_by_xpath(vars.teamFromXPath).text

    if CheckExists(vars.teamWebsiteXPath) == False:
        website = "None"
    else:
        website = driver.find_element_by_xpath(vars.teamWebsiteXPath).text

    if CheckExists(vars.teamNameXPath) == False:
        name = "None"
    else:
        name = driver.find_element_by_xpath(vars.teamNameXPath).text

    if CheckExists(vars.robotNameXPath) == False:
        robotName = "None"
    else:
        robotName = driver.find_element_by_xpath(vars.robotNameXPath).text


    util.PrintPageData(name, From, robotName, website, info)

    driver.close()
    exit()

main()
