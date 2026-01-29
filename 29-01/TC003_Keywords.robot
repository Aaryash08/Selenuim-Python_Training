*** Setting ***
Library    SeleniumLibrary

*** Keywords ***
Open Application
    Open Browser    https://www.google.com    chrome
    Maximize Browser Window


*** Test Cases ***
TC001.robot
    Open Application
    title should be    Google
    Close Browser
    
    