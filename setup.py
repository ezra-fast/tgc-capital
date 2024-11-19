#!/usr/bin/python3

import os

pages = [
"focus.md",
"partners.md",
"success.md",
"the-process.md",
"getting-started.md",
"special-accounts.md",
"contact.md",
]

def populate():
    for page in pages:
        os.system(f'cp index.md {page}')
        print(f"[+] Creating {page}")

def reset():
    for page in pages:
        os.system(f'rm {page}')
        print(f"[+] Removing {page}")

def change():
    for page in pages:
        os.system(f"vim {page}")

# populate()
# reset()
change()
