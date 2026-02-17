*** Settings ***
Library    SeleniumLibrary
Suite Setup    Open Browser To Registration Page
Suite Teardown    Close Browser

*** Variables ***
${URL}    file:    http://localhost:63342/Wipro_NGA/Labs/CaseStudy/casestudy3/patient.html?_ijt=475r26u1gli0njg01qj1avv1r&_ij_reload=RELOAD_ON_SAVE
${BROWSER}    Chrome

*** Keywords ***
Open Browser To Registration Page
    Open Browser    ${URL}    ${BROWSER}
    Maximize Browser Window

*** Test Cases ***
Register Patient
    Input Text    id=name    Aaryash
    Input Text    id=age     22
    Click Element    xpath=//input[@value='Male']
    Input Text    id=disease    Fever
    Select From List By Label    id=doctor    Dr. Sharma
    Click Button    Register
