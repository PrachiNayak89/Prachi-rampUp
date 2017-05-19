*** Settings ***
Library    Selenium2Library
Library  OperatingSystem

*** Variables ***

${URL}            https://www.amazon.in
${BROWSER}        firefox

*** Test Cases ***
[TC-001]-Launching the browser and search and launch the Google.com
    Launch Browser

*** Keywords ***
Set Environment Variable  webdriver.gecko.driver  /home/prachi/Downloads/geckodriver.exe
Launch Browser
    Open Browser    ${URL}  ${BROWSER}
    Maximize Browser Window
    Close Browser

