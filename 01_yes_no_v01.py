# checks that response is either first letter of word, or full word 
# ie: YES, ye and y will return true
def YesNo(response):
    if "yes"[0:len(response)] == response.lower():
        return True
    elif "nope"[0:len(response)] == response.lower():
        return False
    else:
        return YesNo(input("that is not a response "))
        

# Ask if you have used the app before and checks using YesNo
answer = YesNo(input("Have you used this app before? "))

if answer:
    print("Yes")
else:
    print("No")
