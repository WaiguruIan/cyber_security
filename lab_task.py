import smtplib
from email.message import EmailMessage

real_sender_name = "Zetech University <admin@zetech.ac.ke>"  
fake_email = "admin@zetech.ac.ke"       
my_gmail = "muchiriian2020@gmail.com"
my_app_pass = "bgvk vypi bfju phvo"     
recipient = "fredrick.ochieng@zetech.ac.ke"


msg = EmailMessage()
msg['From'] = f"{real_sender_name} <{fake_email}>"
msg['To'] = recipient
msg['Subject'] = "INTRODUCING THE ZETECH-AGRITECH AND INNOVATION HUB"


email_content = """
<!DOCTYPE html>
<html>
<head>
    <style>
        body {
            font-family: Arial, sans-serif;
            line-height: 1.6;
        }
        .footer {
            margin-top: 20px;
            font-size: 14px;
            color: #555;
        }
        .banner {
            margin-top: 20px;
        }
    </style>
</head>
<body>
<font face="verdana, sans-serif">
    <p>Greetings from Zetech University!</p>
    <p>
        The University is pleased to formally introduce the<b> Zetech University AgriTech and Innovation Hub</b>, 
        a newly established initiative designed to advance innovation, research, entrepreneurship, and 
        practical solutions within the agriculture and agri-business ecosystem.
    </p>
    <p>
        The AgriTech and Innovation Hub has been developed to serve as a collaborative platform bringing 
        together <b>students, academic staff, researchers, industry partners, and innovators</b> to co-create 
        solutions that address real-world agricultural challenges. The Hub will support applied research, 
        technology-driven farming solutions, agribusiness incubation, skills development, and community 
        impact aligned with national and regional development priorities.
    </p>
    <p>
        Through this Hub, members of the Zetech University community will have opportunities to:
        <ul>
            <li>Participate in innovation-driven agricultural projects</li>
            <li>Engage in interdisciplinary research and product development</li>
            <li>Access training, mentorship, incubation, and industry linkages</li>
            <li>Contribute to sustainable agriculture, food security, and agribusiness transformation, in line with UN SDG on Zero Hunger</li>
        </ul>
    </p>
    <p>
        Kindly find <b>attached</b> a detailed concept and profile document outlining the vision, objectives, focus areas, 
        and implementation framework of the AgriTech and Innovation Hub.
    </p>
    <p>
        You are encouraged to review the document and explore ways to engage with, contribute to, and benefit from 
        this exciting initiative as we continue to position Zetech University as a leader in innovation, technology, 
        and societal impact.
    </p>
    <p>Further communication will follow regarding participation opportunities, programmes, and activities under the Hub.</p>
    <p>--</p>
    <p style="margin:1px">
    <img style="height:57px" src="https://ci3.googleusercontent.com/meips/ADKq_NbCC1f4RINYgeqw0PTTiN_2Srf4vyr5yBcQjmkjhJjQnJdIbvYC0hHQ6GkCcHDtGZNq2V8A8doIzxLIYmdMcg5At_-oF6kHVGm45BBiZ3_nNRGFZKAFFXwHHJoLle-8lzz1F44B8mYdxmahkUVgwzyw4OSOjeXCzGOd-NogwQCvJgkF705AYS9HwtVEEf7sK1FriF4SXTF29FhWMwmgUpY=s0-d-e1-ft#https://d36urhup7zbd7q.cloudfront.net/5419702880174080/5695960435916800/5c4195d4-6d3b-48cf-92c4-0cc953843ba4/signoff.gif?ck=1723760805.72" alt="Kind regards" height="57" class="CToWUd" data-bit="iit"></p>
    <p><strong>Intercom</strong><br>
    Internal Communication at Zetech University<br>
    Address: 2768-00200 Nairobi, Kenya<br>
    Phone: 0719 034 500 | Mobile: 0719034500<br>
    Email: intercom@zetech.ac.ke<br>
    Website: <a href="https://www.zetech.ac.ke">www.zetech.ac.ke</a>
    </p>
    <div class="banner">
        <img src="https://ci3.googleusercontent.com/meips/ADKq_NaIgbif8E-ogq1dIcyXrixzrKVyxl4T6WRE6lo5cVie4c9P2R2oL-Hk9NXtwgMRlCCdIVNfd3xpwqfq9-dMAznOJjqfK89T1KgWZNRYz3cE-LmNc5GbeScQrTEeGCTDMM7qIkT2s-EgznT80dCV3_yd_4S1l0YNWlo-aHY4=s0-d-e1-ft#https://d36urhup7zbd7q.cloudfront.net/u/RVb43KjONdy/101125c1-6e52-43cd-aa13-7e35b427a1e6__400x200__.gif" style="width:544px;height:272px" width="544" height="272" alt="App Banner Image" class="CToWUd" data-bit="iit">
    </div>
    <p class="footer">
        IMPORTANT: The contents of this email and any attachments are confidential. They are intended for the named recipient(s) only. 
        If you have received this email by mistake, please notify the sender immediately and do not disclose the contents to anyone 
        or make copies thereof.
    </p>
    <p class="footer">
        Green: Please consider your environmental responsibility. Before printing this e-mail message, ask yourself whether you really 
        need a hard copy.
    </p>
</body>
</html>
"""

msg.set_content(email_content, subtype='html')

try:
    with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
        server.login(my_gmail, my_app_pass)
        server.send_message(msg)
    print("Email sent successfully✅")
except Exception as e:
    print(f"❌ Error: {e}")