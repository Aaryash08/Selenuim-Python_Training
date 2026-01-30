*** Settings ***
Library    SeleniumLibrary


*** Variables ***
${url}      https://opensource-demo.orangehrmlive.com/web/index.php/auth/login
${browser}      chrome


*** Keywords ***
open orangehrm
    open browser    ${url}     ${browser}
    maximize browser window
orangehrmlogin
    [Arguments]    ${username}  ${password}
    Input text    name=username    ${username}
    input text      name=password    ${password}
    sleep           10s
     capture page screenshot    beforelogin5.png
    click button    xpath=//*[@id="app"]/div[1]/div/div[1]/div/div[2]/div[2]/form/div[3]/button
     sleep           10s
    capture page screenshot    afterlogin5.png
    close browser

*** Test Cases ***
TC005_DD.robot
    open orangehrm
    sleep    5s
    orangehrmlogin    Admin     admin123