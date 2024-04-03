def convert(msg):
    msg1 = msg.replace(":)","🙂")
    msg2 = msg1.replace(":(","🙁")
    return msg2

def main():
    msg = input("enter un msg : ")
    result = convert(msg)
    print(result)


main()

