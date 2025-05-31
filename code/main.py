from ai_communication import request
def main():
    print("Write your questions\n")
    x=input()
    if isinstance(x,str):
        result=request(x)
        print(result)
    else:
        "FAILURE: You need to write a string"
main()