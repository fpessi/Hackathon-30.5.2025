from ai_communication import request
def main():
    print("Write your questions. Stop by writing exit")
    x=input() #user writes their input for the ai
    while x.lower()!="exit":
        if isinstance(x,str):
            result=request(x) #the users text is sent to the ai to process
            if result==None:
                print("FAILURE: try again")
            else:
                edited_result=result["choices"][0]["text"]
                print(edited_result)
            x=input()
        else:
            print("FAILURE: You need to write a string") #if the user somehow gives other value that string
            x = input()
    print("Exiting software")


main()