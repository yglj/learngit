def reverse(str):
    return str[::-1]
def cmp(text):
    text = text.lower()
    text = text.replace(" ","")
    text = text.replace(",","")
    print(text)
    return text == reverse(text)

context = "Rise to vote, sir"
#input("Enter:")
if cmp(context):
    print("is huiwen")
else:
    print("is not")