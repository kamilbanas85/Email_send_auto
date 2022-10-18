#### send emeial when outlook is installed 

import win32com.client as win32

outlook = win32.Dispatch('outlook.application')
mail = outlook.CreateItem(0)
mail.To = 'xxx@gmail.com'
mail.Subject = 'Message subject'
mail.Body = 'Message body'
mail.HTMLBody = '<h2>HTML Message body</h2>' #this field is optional

# To attach a file to the email (optional):
attachment = r"C:\\Users\\lng__usa.pdf"
mail.Attachments.Add(attachment)

mail.Send()
