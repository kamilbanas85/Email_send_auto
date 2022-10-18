import base64

from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import (Mail, Attachment, FileContent, FileName, FileType, Disposition, ContentId)
# import sendgrid


message = Mail(
    from_email='xxx@gmail.com',
    to_emails='yyy@gmail.com',
    subject='Raport Tygodniowy',
    html_content = Mail_Tamplate_HTML
)

path_to_file = '/dbfs/FileStore/RAPORT_weekly/report.pdf'

with open(path_to_file, 'rb') as f:
    data = f.read()
    f.close()
encoded_file = base64.b64encode(data).decode()

attachedFile = Attachment(
    FileContent(encoded_file),
    FileName('RaportTygodniowy.pdf'),
    FileType('application/pdf'),
    Disposition('attachment')
)
message.attachment = attachedFile


Company_logo_path = "/dbfs/FileStore/RAPORT_weekly/pic/logo.jpg"
with open(Company_logo_path, 'rb') as fp:
    Company_logo = fp.read()
    fp.close()
    
encoded_Company_logo = base64.b64encode(Company_logo).decode()
  
Company_logo_attachment = Attachment(
                    FileContent(encoded_Company_logo),
                    FileName('logo.jpg'),
                    FileType('image/jpeg'),
                    Disposition('inline'),
                    ContentId("ID_IN_HTML")
                          )

message.attachment = Company_logo_attachment

# key from KeyValute
# SendGridKey = dbutils.secrets.get(scope = "scope_of_secret", key="sendgrid-key")
# sg = SendGridAPIClient( SendGridKey )

sg = SendGridAPIClient('SG.MyKey')  


response = sg.send(message)
print(response.status_code, response.body, response.headers)



### w HTML_contnet = <img width=135 height=50 src="cid:ID_IN_HTML"/>
