*** Settings ***
Library     methods.py
Test Setup      get config

*** Variables ***

${test}     123

*** Keywords ***
get config
    log     开始获取配置
    set suite variable     ${config}       config

*** Test Cases ***
test
    log     ${config}

test1
    test
