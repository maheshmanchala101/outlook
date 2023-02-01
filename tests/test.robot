*** Settings ***
Library            QForce
Library            ${CURDIR}/../libraries/graph.py
Resource           ${CURDIR}/../resources/graph.resource
Suite Setup        Open Browser   about:blank    chrome
Suite Teardown     Close All Browsers

*** Test Cases ***
Check Email Content
    ${body}=  Get Email Content  ${client_id}  ${client_secret}  ${tenant_id}  ${email_address}  ${email_subject}
    Evaluate  "${body}" == "${email_body}"