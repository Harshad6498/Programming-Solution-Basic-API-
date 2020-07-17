num = input("Enter the Number: ")
#val = num.startswith("9" or "8" or "7")
if (num.startswith("9" or "8" or "7")) and (len(num)==10) and (num.isdigit()):
    print("VALID")
else:
    print("NOT VALID")