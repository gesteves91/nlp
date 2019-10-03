import re

def match_num(string):
    text = re.compile(r"^5")
    if text.match(string):
        return True
    else:
        return False
        
print(match_num('5-2345861'))
print(match_num('6-2345861'))