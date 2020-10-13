import yagmail
yag=yagmail.SMTP("sender_mail")
yag.login()
yag.send(to=["receiver_mails"],
        subject="Testing Yagmail",
        attachments="",
        contents="Hello here is pic lit!:"
        )


