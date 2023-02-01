from O365 import Account, MSGraphProtocol
import bleach

# https://pypi.org/project/O365/
# Add App registration to your Azure AD
# - Set client secret
# - Add permissions (Mail.Read)
# Doesn't work with personal account, needs to be a corporate.

def  get_email_content(client_id: str,
                       client_secret: str,
                       tenant: str,
                       email: str,
                       subject: str):

    credentials = (client_id, client_secret)
    account = Account(credentials, 
                      auth_flow_type='credentials',
                      tenant_id=tenant)
    
    account.authenticate()
    mailbox = account.mailbox(resource=email)

    inbox = mailbox.inbox_folder()

    query = mailbox.new_query().on_attribute('subject').contains(subject)

    messages = inbox.get_messages(limit=25, query=query)
    message = list(messages)[-1]
    raw = bleach.clean(message.body,tags=[],strip=True)
    return raw.lstrip()
