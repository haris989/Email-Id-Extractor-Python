#I have created this file - Programmer_Sidharth
import re

def extract_email(text):
    emails = re.finditer(r"\w+@\w+\.\w+", text)
    return [email.group() for email in emails]
    
if __name__ == "__main__":
    for email in extract_email("Hi there! this is programmer_sidharth. My email is programmersidharth@gmail.com "):
        print(email)
