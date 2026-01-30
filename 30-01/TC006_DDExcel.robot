*** Settings ***
Library    SeleniumLibrary
Library    DataDriver    Data.xlsx
Test Template    OrangeHRM Login With Excel


*** Variables ***
${URL}       https://opensource-demo.orangehrmlive.com/web/index.php/auth/login
${BROWSER}   chrome

*** Keywords ***


OrangeHRM Login With Excel
    Open Browser    ${URL}    ${BROWSER}
    Maximize Browser Window
    Sleep    5s
    [Arguments]    ${username}    ${password}
    Input Text    name=username    ${username}
    Input Text    name=password    ${password}
    Sleep    6s
    Capture Page Screenshot    beforelogin6.png
    Click Button    xpath=//button[@type='submit']
    Sleep    6s
    Capture Page Screenshot    afterlogin6.png
    click image    xpath=//*[@id="app"]/div[1]/div[1]/header/div[1]/div[3]/ul/li/span/img
    Sleep    6s
    click link    Logout
    Capture Page Screenshot    afterlogOut6.png
    Close Browser

*** Test Cases ***
TC006_DDExcel_Login
