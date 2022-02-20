# checks that response is either first letter of word, or full word 
# ie: YES, ye and y will return true
def Number(response,low,high):
    if int(response) >= low and int(response) <= high:
        return int(response)
    elif int(response) < low:
        return int(low)
    elif int(response) > high:
        return int(high)


# Ask if you have used the app before and checks using YesNo
def question():
    try:
        answer = Number(int(input("Pick a number from 1 to 10: ")),1,10)
        return answer
    except:
        print("Oops, something went wrong.")
        return question()
while True:
    print(question())