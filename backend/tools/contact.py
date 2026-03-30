from typing import List 
from enum import Enum, auto
import asyncio
import aiosmtplib
from email.message import EmailMessage
import dotenv
import os
import webbrowser


dotenv.load_dotenv("../../.env")
sender_email = str(os.getenv("SENDER_EMAIL"))
password = str(os.getenv("EMAIL_PASSWORD"))

print(sender_email)
print(password)


class ContactChannel(Enum):
    """
    Shows the ways to contact a person
    """
    Email = auto()
    PhoneNumber = auto()
    Link = auto()


class ContactInfo:
    """
    The data to contact that person.
    """
    def __init__(self, contactChannel: ContactChannel, reciever: str, header: str, content: str):
        self.reciever = reciever
        self.header = header
        self.content = content
        self.contactChannel = contactChannel


class Contact:
    @staticmethod
    def Contact(contactInfo: ContactInfo):
        """
        Contacts the person with given contact info.
        What do we use for UI?
        """

        match contactInfo.contactChannel:
            case ContactChannel.Email:
                asyncio.run(Contact.ContactEmail(contactInfo.reciever, contactInfo.header, contactInfo.content))
            case ContactChannel.PhoneNumber:
                asyncio.run(Contact.ContactPhone(contactInfo.reciever, contactInfo.content))

    @staticmethod
    async def ContactEmail(email: str, header: str, msg: str):
        mes = EmailMessage()
        mes["To"] = email
        mes["From"] = sender_email
        mes["Subject"] = header
        mes.set_content(msg)

        try:
            async with aiosmtplib.SMTP(hostname="smtp.gmail.com", port=587, use_tls=False) as server:
                await server.login(sender_email, password)
                await server.send_message(mes)
                print(f"Email sent to {email}")
        except Exception as e:
            print(f"Error: {e}")

    @staticmethod
    async def ContactEmailHTML(email: str, header: str, html: str, fallbackText: str):
        mes = EmailMessage()
        mes["To"] = email
        mes["From"] = sender_email 
        mes["Subject"] = header
        mes.set_content(fallbackText)
        mes.add_alternative(html, subtype='html')

        try:
            async with aiosmtplib.SMTP(hostname="smtp.gmail.com", port=587, use_tls=False) as server:
                await server.login(sender_email, password)
                await server.send_message(mes)
                print(f"HTML Email sent to {email}")
        except Exception as e:
            print(f"Error: {e}")

    
    @staticmethod
    async def ContactPhone(phoneNumber: str, msg: str):
        pass


    @staticmethod
    async def OpenLink(link: str):
        webbrowser.open_new(link)



# Testing code
mr_tuyen = ContactInfo(ContactChannel.Email, "iaminfinityiqcoding@gmail.com", "ABC", "ABC")
Contact.Contact(mr_tuyen)