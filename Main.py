from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.by import By
from util import util
from util import vars

# use this for email checking

driver_options = Options()

# headless turns off the window
driver_options.add_argument("--headless")
#driver_options.add_argument("--disable-extensions")
#driver_options.add_argument("--disable-gpu")
#driver_options.add_argument("--no-sandbox") # linux only

# start the driver and add options
driver = webdriver.Firefox(options=driver_options)

teamNumber = input("\033[33m" + "Input FRC Team Number >> ")


def main():
    CurrentURL = vars.defaultURL + teamNumber

    if util.sendRequest(CurrentURL) == False:
        print("\033[31m" + "ERROR: Sorry That Team Number is Incorrect" + "\033[39m")
        driver.close()
        exit()
    else:
        driver.get(CurrentURL)
        pass

    if driver.current_url != CurrentURL:
        return

    info = driver.find_element_by_xpath(vars.teamInfoXPath).text
    From = driver.find_element_by_xpath(vars.teamFromXPath).text
    website = driver.find_element_by_xpath(vars.teamWebsiteXPath).text
    name = driver.find_element_by_xpath(vars.teamNameXPath).text
    robotName = driver.find_element_by_xpath(vars.robotNameXPath).text

    util.PrintPageData(name, From, robotName, website, info)


main()


def PrintCurrentAddr():
    print(driver.current_url)
