import re
#search -first occurrence
# text ="I have 31 students and 2 TM'S"
# match = re.search(r"\d+", text)
# print(match.group())
# print(match.start())
# print(match.end())

#FINDALL list of all occurrences
# match = re.findall(r"\d+", text)
# print(match)

#FINDITRE
# match = re.finditer(r"\d+",text)
# for x in match:
#     print(f"{x.group()}, {x.start()},{x.end()}")


#^(caret) matches all charcters from the start
#text1 = "acb accb ab"
# # pattern ="a..b"
# pattern = "^ac"


#$ dollar sign(brings the specified type)
# pattern = "b$"

#* all characters before until specfied letter is found
#pattern = "b*"
#matches = re.findall(pattern, text1)
#print(matches)



#CHARACTERCLASSES

# text ="apple banna cat dog"
# pattern = r"[abc]"
# matches = re.findall(pattern, text)
# print(matches)

#digits

# text= "we are 2 students and 2 TMS"
# pattern = r"\d"
# matches = re.findall(pattern, text)
# print(matches)

#character[A-Z] case sensistive aspect
# text = "We ARe LaTE For CLASS"
# pattern = r"[A-Z]"

# matches = re.findall(pattern, text)
# print(matches)

#digits
# text = "we are 2 students and 23 TM'S"
# pattern = r"[0-9]"
# matches = re.findall(pattern,text)
# print(matches)


#\s counts the white spaces
# text = "We are in class.\nAre you there?"
# print(text)
# pattern = r"\s"
# matches = re.findall(pattern, text)
# print(matches)

#?
# text = "I have 31 students and 2 TM's"

# pattern = r"\d?"

# matches = re.findall(pattern, text)
# print(matches)


#{n} occurrences
# pattern = r"a{2}"
# text = "aa ba bac dca"
# pattern = r"a{2,3}"
# matches = re.findall(pattern, text)
# print(matches)


text = "Contact us at 123-456-3210"
pattern = r"\d{3}-\d{3}-\d{4}"
matches = re.findall(pattern,text)
print(matches)


#EMAIL


text = "Send an email to support@example.com or sales@company.net for inquiries."

# Regular expression for email extraction
email_pattern = r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}"

emails = re.findall(email_pattern, text)
print("Extracted Emails:", emails)

#DATES
text = "The event is on 12/08/2023 and another one on 07-15-2024."

# Regular expression for date extraction
date_pattern = r"\b\d{2}/\d{2}/\d{4}\b|\b\d{2}-\d{2}-\d{4}\b"

dates = re.findall(date_pattern, text)
print("Extracted Dates:", dates)

#PATTERN
def is_valid_password(password):
    pattern = r"^(?=.*[A-Z])(?=.*[a-z])(?=.*\d)(?=.*[@$!%*?&])[A-Za-z\d@$!%*?&]{8,}$"
    
    if re.match(pattern, password):
        return "✅ Password is strong."
    else:
        return "❌ Password does not meet security requirements."

# Test Cases
passwords = ["Weakpass", "Strong1@", "NoNumber@", "GoodPass1!"]
for pwd in passwords:
    print(f"Password: {pwd} -> {is_valid_password(pwd)}")
