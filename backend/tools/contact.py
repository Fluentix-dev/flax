from typing import List 
from enum import Enum, auto
import asyncio
import aiosmtplib
from email.message import EmailMessage
import dotenv
import os
import webbrowser


dotenv.load_dotenv("../../.env")
SENDER_EMAIL = str(os.getenv("SENDER_EMAIL"))
SENDER_PASSWORD = str(os.getenv("EMAIL_PASSWORD"))


class ContactChannel(Enum):
    """
    Shows the ways to contact a person
    """
    Email = auto()
    PhoneNumber = auto()
    Link = auto()

    def __str__(self):
        return f"<contactChannel>{self.name}</>"


class ContactInfo:
    """
    The data to contact that person.
    """
    def __init__(self, contactChannel: ContactChannel, reciever: str, header: str, content: str):
        self.reciever = reciever
        self.header = header
        self.content = content
        self.contactChannel = contactChannel
    

    def __str__(self):
        return f"<ContactInfo>{self.contactChannel}<reciever>{self.reciever}</><header>{self.header}</><content>{self.content}</>"


class Contact:
    @staticmethod
    def Contact(contactInfo: ContactInfo):
        """
        Contacts the person with given contact info.
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
        mes["From"] = SENDER_EMAIL
        mes["Subject"] = header
        mes.set_content(msg)

        try:
            async with aiosmtplib.SMTP(hostname="smtp.gmail.com", port=587, use_tls=False) as server:
                await server.login(SENDER_EMAIL, SENDER_PASSWORD)
                await server.send_message(mes)
                print(f"Email sent to {email}")
        except Exception as e:
            print(f"Error: {e}")

    @staticmethod
    async def ContactEmailHTML(email: str, header: str, html: str, fallbackText: str):
        mes = EmailMessage()
        mes["To"] = email
        mes["From"] = SENDER_EMAIL 
        mes["Subject"] = header
        mes.set_content(fallbackText)
        mes.add_alternative(html, subtype='html')

        try:
            async with aiosmtplib.SMTP(hostname="smtp.gmail.com", port=587, use_tls=False) as server:
                await server.login(SENDER_EMAIL, SENDER_PASSWORD)
                await server.send_message(mes)
                print(f"HTML Email sent to {email}")
        except Exception as e:
            print(f"Error: {e}")

    
    @staticmethod
    async def ContactPhone(phoneNumber: str, msg: str):
        """
        Call phone and hack to someone
        """
        print("Contacting to phone isn't implemented yet!")


    @staticmethod
    async def OpenLink(link: str):
        """
        welcome.py memorial

        The one incident where computers in my school's computer lab got fucked up
        """
        webbrowser.open_new(link) # welcome.py memorial...


    def __str__(self):
        return f"<function>Contact</>"


if __name__ == '__main__':
    an = ContactInfo(ContactChannel.Email, "iaminfinityiqcoding@gmail.com", "Test msg from app", "testing12345")
    Contact.Contact(an)