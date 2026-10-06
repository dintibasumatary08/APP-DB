import re

text = "Contact me at abc@gmail.com or student123@yahoo.com"

emails = re.findall(r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}\b', text)

print("Email addresses:")
for email in emails:
    print(email)