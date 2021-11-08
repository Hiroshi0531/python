import smtplib, ssl, time
from email.mime.text import MIMEText
import pandas as pd

# 以下にGmailの設定を書き込む★ --- (*1)
gmail_account = "xxx@gmail.com"#gmail account e-mail adress
gmail_password = "mqbbi6ZbrUDRfY9"#gmail account password

#adress.csvファイルの読み込み
csv_input = pd.read_csv(filepath_or_buffer="address.csv",encoding="ms932",sep=",")

for i in range(0,len(csv_input)):
    # メールの送信先★ --- (*2)
    mail_to = csv_input.iloc[i,0]
    URL = csv_input.iloc[i,1]
    # メールデータ(MIME)の作成 --- (*3)
    subject = "hello"
    body = '''hello<br><br>
        click this url<br>
        '''
    body += URL
    msg = MIMEText(body, "html")
    msg["Subject"] = subject
    msg["To"] = mail_to
    msg["From"] = gmail_account
    # Gmailに接続 --- (*4)
    server = smtplib.SMTP_SSL("smtp.gmail.com", 465,context=ssl.create_default_context())
    server.login(gmail_account, gmail_password)
    server.send_message(msg) # メールの送信
    print("ok.")
    time.sleep(1)
