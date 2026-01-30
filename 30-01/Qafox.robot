*** Settings ***
Library           SeleniumLibrary
Library           DataDriver    file=Register.xlsx
Test Template     RegisterWithExcel

*** Variables ***
${URL}       https://tutorialsninja.com/demo/index.php?route=account/register
${BROWSER}   chrome

*** Test Cases ***
Register_Test_Using_Excel

*** Keywords ***
RegisterWithExcel
    [Arguments]    ${First Name}    ${Last Name}    ${E-Mail}    ${Telephone}    ${Password}    ${Password Confirm}

    Open Browser    ${URL}    ${BROWSER}
    Maximize Browser Window
    Wait Until Element Is Visible    name=firstname    10s

    Input Text    name=firstname    ${First Name}
    Input Text    name=lastname     ${Last Name}
    Input Text    name=email        ${E-Mail}
    Input Text    name=telephone    ${Telephone}
    Input Text    name=password     ${Password}
    Input Text    name=confirm      ${Password Confirm}
    Click Element    xpath=//input[@name='agree']
    Click Button    xpath=//input[@value='Continue']
    Sleep    3s
    Capture Page Screenshot    register_result.png
    Close Browser