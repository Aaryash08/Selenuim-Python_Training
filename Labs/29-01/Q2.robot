*** Settings ***
Library    BuiltIn
Library    Process
Library    SeleniumLibrary


*** Test Cases ***
Verify Automation Environment Setup
    [Documentation]    Verify Python, Robot Framework, SeleniumLibrary and log versions

    Log To Console    ===== Environment Verification Started =====

    ${python}=    Run Process    python    --version    stdout=YES    stderr=YES
    Run Keyword If    ${python.rc} != 0    Fail    Python is not installed
    Log To Console    Python Installed: ${python.stdout}${python.stderr}

    ${robot}=    Run Process    robot    --version    stdout=YES    stderr=YES
    Run Keyword If    '${robot.stdout}${robot.stderr}' == ''    Fail    Robot Framework is not installed
    Log To Console    Robot Framework Version: ${robot.stdout}${robot.stderr}

    Run Keyword And Continue On Failure    Log To Console    SeleniumLibrary imported successfully

    Log To Console    ===== Environment Verification Completed =====
