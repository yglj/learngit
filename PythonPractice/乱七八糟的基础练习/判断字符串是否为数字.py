import unicodedata
def is_number():
    s = input()
    try:
        if( unicodedata.numeric(s) or float(s) ):
            return True
    except (ValueError,TypeError):
        print("不是数字")

    return False
#is_number()
if ( True or 3/0):
    print("逻辑短路")
try:
    if (3/0 or True):
        print(0)
except :
    print("zero error")