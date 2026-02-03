*** Settings ***
Library    SeleniumLibrary

*** Variables ***
${URL}           file:///C:/Users/KIIT/OneDrive/Desktop/Wipro_NGA/Labs/Day14/Q2/demo.html
${BROWSER}        Chrome
${USERNAME}       JohnDoe
${GENDER_MALE}    id:gender-male
${NEWSLETTER}     id:subscribe-checkbox
${COUNTRY_DROPDOWN}    id:country-select

*** Test Cases ***
Verify Form Interaction And Logic
    [Documentation]    Test case to interact with web elements and use conditional logic.
    Open Browser To Form
    Fill Text Fields    ${USERNAME}
    Select Radio Button Option
    Handle Checkbox
    Select From Dropdown Menu
    Check Condition And Log Results
    Capture Page Screenshot
    [Teardown]    Close Browser

*** Keywords ***
Open Browser To Form
    Open Browser    ${URL}    ${BROWSER}
    Maximize Browser Window

Fill Text Fields
    [Arguments]    ${name}
    Input Text    id:username-box    ${name}

Select Radio Button Option
    Select Radio Button    gender    male

Handle Checkbox
    Select Checkbox    ${NEWSLETTER}

Select From Dropdown Menu
    Select From List By Label    ${COUNTRY_DROPDOWN}    United States

Check Condition And Log Results
    ${status}=    Get Text    id:status-message
    Run Keyword If    '${status}' == 'Success'    Log To Console    Form submitted successfully!
    ...    ELSE    Log To Console    Form submission pending or failed.
