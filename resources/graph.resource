*** Settings ***
Library            OperatingSystem
Library            Collections
Library            QForce
Library            ${CURDIR}/../libraries/graph.py

*** Variables ***
${client_id}        # Initialize these variables in Copado Robotic Testing test suite variables
${client_secret}    # and remember to crypt and hide.
${tenant_id}
${email_address}
${email_subject}
${email_body}