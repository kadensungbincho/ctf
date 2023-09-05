from pwn import *
import sys

GET_SHELL = 0x8048669
PRINTF_GOT = 0x804a010

payload = b""
payload = ""

sys.stdout.buffer.write(payload)
