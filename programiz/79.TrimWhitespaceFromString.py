import re
text = "      \nhello world"
print(re.sub(r'^\s+|\s+$','',text))