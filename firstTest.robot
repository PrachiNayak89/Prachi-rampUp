*** Settings ***
Library    Selenium2Library
Library  OperatingSystem

*** Variables ***

${URL}            https://www.google.co.in/
${BROWSER}        firefox

*** Test Cases ***
[TC-001]-Launching the browser and search and launch the Google.com
    Launch Browser
    Search for the amazon website
    Click on the Search Button
    

*** Keywords ***
Set Environment Variable  webdriver.gecko.driver  /home/prachi/Downloads/geckodriver.exe

Launch Browser
    Open Browser    ${URL}  ${BROWSER}
    Maximize Browser Window
    
Search for the amazon website
    Input Text    id=lst-ib    amazon.in

Click on the Search Button
    Click Button    name=btnG
    Close Browser


