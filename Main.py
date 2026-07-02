import re

def check_url(url):
    score = 0

    # Rule 1: Length
    if len(url) > 75:
        score += 1

    # Rule 2: @ symbol
    if "@" in url:
        score += 2

    # Rule 3: IP address
    if re.match(r"(\d{1,3}\.){3}\d{1,3}", url):
        score += 2

    # Rule 4: suspicious words
    suspicious_words = ["login", "verify", "bank", "secure"]
    for word in suspicious_words:
        if word in url.lower():
            score += 1

    # Decision
    if score >= 4:
        return "Phishing ❌"
    elif score >= 2:
        return "Suspicious ⚠️"
    else:
        return "Safe ✅"

# Test
url = input("Enter URL: ")
print(check_url(url))
