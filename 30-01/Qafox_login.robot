*** Settings ***
Library           SeleniumLibrary
Library           DataDriver    file=Register.xlsx
Test Template     LoginWithExcel

*** Variables ***
${URL}       https://tutorialsninja.com/demo/index.php?route=account/login
${BROWSER}   chrome

*** Test Cases ***
Login_Test_Using_Excel

*** Keywords ***
LoginWithExcel
    [Arguments]    ${username}    ${password}
    Open Browser    ${URL}    ${BROWSER}
    Maximize Browser Window

    Wait Until Element Is Visible    name=username    10s

    Input Text    name=username        ${username}
    Input Text    name=password     ${password}

    Click Button    xpath=//input[@value='Login']

    Sleep    3s
    Capture Page Screenshot    login_result.png
    Close Browser