# Insecure Custom Hash Function
def custom_hash(s):
    h = 0
    for char in s:
        h = (h * 31 + ord(char)) & 0xFFFFFFFF
    return h

# Find string collision matching hash: 305419896
target_hash = 305419896
