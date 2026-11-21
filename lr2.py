s = "Abraсadabra"

print("The third symbol of string: ", s[2])
print("The second to last symbol of strnig: ", s[-2])
print("The first five symbols if string: ", s[: 6])
print("The string without two last symbols: ", s[: -2])
print("The symbols of string with even index: ", s[::2])
print("The symbols of string with non-even index: ", s[1::2])
print("The reversed string: ", s[::-1])
print("The reversed string with non-even index: ", s[::-1][::2])
print(len(s))