def vogal(x):
    x = x.lower()
    if x in ("a", "e",  "i", "o", "u"):
        return True
    else:
        return False
    
print(vogal("a"))
print(vogal("b"))
print(vogal("E"))