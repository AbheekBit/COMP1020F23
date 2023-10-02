import string

def main():
    essay = open("essay.txt")
    #print(essay.read())
    user_text = essay.read()
    user_text = user_text.split()
    print(user_text)


if __name__ =="__main__":
    main()