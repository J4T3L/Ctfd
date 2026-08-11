# Insecure Custom Hash Function
def custom_hash(s):
    h = 0
    for char in s:
        h = (h * 31 + ord(char)) & 0xFFFFFFFF
    return h

# Target Hash for CTF{cush0m_h4sh_c0ll1s10n_2026}: 305419896
# Find a collision string!
