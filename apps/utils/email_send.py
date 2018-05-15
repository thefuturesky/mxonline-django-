from users.models import EmailVerifyRecord
from random import Random
from django.core.mail import send_mail
from mxonline.settings import EMAIL_FROM

def send_register_email(email,send_type="register"):
    email_record = EmailVerifyRecord()
    random_code =generate_random_str(16)
    email_record.code = random_code
    email_record.email=email
    email_record.send_type= send_type
    email_record.save()

    if send_type == "register":
        email_title = "慕学在线网注册激活链接"
        email_body = "请点击下面的链接激活你的账号:http://127.0.0.1:8000/active/%s" % random_code

        send_tatus = send_mail(email_title,email_body,EMAIL_FROM,[email])
        if send_tatus:
            pass

    if send_type == "forget":
        email_title = "慕学在线网密码重置链接"
        email_body = "请点击下面的链接重置你的密码:http://127.0.0.1:8000/reset/%s" % random_code

        send_tatus = send_mail(email_title, email_body, EMAIL_FROM, [email])
        if send_tatus:
            pass



def generate_random_str(random_length=8):
    str = ""
    chars = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz123456790"
    length = len(chars)-1
    random = Random()
    for i in range(random_length):
        str += chars[random.randint(0,length)]
    return str