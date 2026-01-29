*** Settings ***
Library    BuiltIn


*** Variables ***
${USERNAME}    Aaryash
${COUNT}       3
@{ITEMS}       Apple    Banana    Orange


*** Test Cases ***
Log User Information
    Log    Username is ${USERNAME}
    Log To Console    Hello ${USERNAME}, welcome to Robot Framework!
    Log    Count value is ${COUNT}

List Variable Demo
    Log    Items list is: ${ITEMS}
    Log To Console    First item is ${ITEMS}[0]
    ${item_count}=    Get Length    ${ITEMS}
    Log To Console    Total items: ${item_count}
