import time
import requests

DeBugging = False

def Delay(delay):
    time.sleep(delay)

def sendRequest(url):
    #post("http://bugs.python.org", data={'number': 12524, 'type': 'issue', 'action': 'show'})
    r = requests.get(url)

    # print stat code while in debuging
    if DeBugging == True:
        print(r.status_code)

    if r.status_code == 404:
        return False
    else:
        pass

def PrintPageData(teamName, teamFrom, RobotName, website, info):
    print(
        # the ansi codes are for coloring
        "\033[31m" + "Team Name: " + teamName + "\n" + "\033[39m"
        "\033[36m" + "Team From: " + teamFrom + "\n"+ "\033[39m"
        # "Rookie year " + RookieYear + "\n"
        "\033[35m" + "Robot Name: " + RobotName + "\n" + "\033[39m"
        "\033[32m" + "Website: " + website + "\n" + "\033[39m"
        "\033[33m" + "Team Info: " + info + "\n" + "\033[39m"
        #"GitHub " + "github" + "\n"
    )