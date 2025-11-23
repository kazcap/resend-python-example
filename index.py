import os
import resend

resend.api_key = os.environ["RESEND_API_KEY"]

html_body = """
<div style="
    background-color:#1b0033;
    padding:40px 20px;
    text-align:center;
    font-family:'Noto Serif JP','Hiragino Mincho ProN','Yu Mincho',serif;
    color:#ff66cc;
">

<div style="
    font-size:18px;
    font-weight:normal;
    line-height:1.7;
    margin-bottom:30px;
">
    アカウント登録に必要な認証コードをお送りします。<br>
    A#B%C&D@E
</div>

<a href="https://kawasaki-omiya.com/images/index.html"
    style="
        display:inline-block;
        padding:14px 28px;
        background:#ff66cc;
        color:#1b0033;
        text-decoration:none;
        font-size:14px;
        font-weight:700;
        border-radius:8px;
    ">
    召喚フォト工房
</a>
</div>
"""

params = {
    "from": "召喚フォト工房 <no-reply@kawasaki-omiya.com>",
    "to": ["kaz.zcap@gmail.com"],
    "subject": "Hello world",
    "html": html_body,
}

email = resend.Emails.send(params)  # type: ignore
print(email)
