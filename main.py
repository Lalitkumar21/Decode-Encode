from encoding import encode
from decoding import decode

print("Encode(1) or decode(2)")
choice=int(input(""))
if choice==1:
    encode()
elif choice==2:
    decode()
else:
    print("incorrect input")
