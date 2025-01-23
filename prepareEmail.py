import os
import smtplib, ssl
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart
from dotenv import load_dotenv, dotenv_values
import time


def sendEmail(movies, story):
    load_dotenv()
    
    try:
            port = 465  # For SSL
            smtp_server = "smtp.gmail.com"
            sender_email = os.getenv("SENDER_EMAIL") # Enter your address
            receiver_emails = [os.getenv("RECEIVER_EMAIL1"), os.getenv("RECEIVER_EMAIL2")]  # Enter receiver address   
            password = os.getenv("GMAIL_KEY")
     

            html = f'''
            <html>
            <body>
            <div>
            {story[2]}
            <div>

            <div><img src="cid:image{0}" alt="Img_s{0}" width="180" height="260"></div>

            <div>
            <h2>
            En preparacion para filmar, con unos retoques, puede que no me reconozcan
            <h2>
            </div>
            
            <div><img src="cid:image{1}" alt="Img_s{1}" width="180" height="260"></div>
            
            </body>
            </html>

            '''           

            for receiver_email in receiver_emails:

                print(f'preparing email for {receiver_email}')
                message = MIMEMultipart("alternative")
                message["Subject"] = "Clover Recomendations"                
                message["From"] = sender_email
                message["To"] = receiver_email
                part2 = MIMEText(html, "html")
                message.attach(part2)

                try:
                    images = []
                    picturefile = movies[1].replace('/media/','/mnt/nas_mount/',1)
                    print(picturefile)
                    images.append((picturefile,f"""<image{0}>""",movies[2]))
                    images.append(('/home/tambor/recomendations/clover/photoBomb (1).jpg',f"""<image{1}>""",'Captured'))

                    for img_path, cid, plot in images:
                        try:
                            with open(img_path, 'rb') as img_file:
                                img = MIMEImage(img_file.read(),_subtype="jpg")
                                img.add_header('Content-ID', cid)
                                message.attach(img)
                                print(img_path)
                        except Exception as e:
                            print(f'{e} ')

                    context = ssl.create_default_context()
                    with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
                        server.login(sender_email, password)
                        server.sendmail(sender_email, receiver_email, message.as_string())

                except Exception as e:
                            print(f'{e} ')
    except Exception as e:
        print(f'{e} ')

            
