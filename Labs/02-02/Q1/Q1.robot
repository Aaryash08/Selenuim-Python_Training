*** Settings ***
Documentation     Example suite for Setup/Teardown and Tagging.
Suite Setup       Log    Preparing the entire test suite environment...
Suite Teardown    Log    Cleaning up the entire suite environment...
Test Setup        Log    Starting an individual test case.
Test Teardown     Log    Finished an individual test case.

*** Test Cases ***
Login To Portal
    [Tags]    Regression    Smoke
    Log    Executing login logic...
    Should Be True    ${True}

Check User Profile
    [Tags]    Regression
    Log    Checking profile details...
    Should Be Equal    1    1

#*** Keywords ***
## Custom keywords could go here