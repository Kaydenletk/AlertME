import smtplib
from email.message import EmailMessage
from PIL import Image
import imghdr

username = "kaydenleprojects@gmail.com"
password = "jfkojvzjloolnzfm"
sender = "kaydenleprojects@gmail.com"
receiver = "kaydenleprojects@gmail.com"

def get_image_type(file_path):
    with Image.open(file_path) as img:
        return img.format.lower()

def send_email(image_path):
    print("send_email function started")
    email_message = EmailMessage()
    email_message["Subject"] = "Someone on the camera!"
    email_message.set_content("Hey, check the camera")

    with open(image_path, "rb") as file:
        content = file.read()
        filename = file.name
        im_type = imghdr.what(None, content)

    email_message.add_attachment(content, maintype="image", subtype=im_type, filename=filename)

    gmail = smtplib.SMTP("smtp.gmail.com", 587)
    gmail.ehlo()
    gmail.starttls()
    gmail.login(sender, password)
    gmail.sendmail(sender, receiver, email_message.as_string())
    gmail.quit()
    print("send_email function ended")

if __name__ == "__main__":
    send_email("image/19.png")
