c = int(input("Temperature In Celcius\n"))

# f= ((9*c + 160)/5)
# print(f"Temperature in Farenheight {f}")

def convert(c):
    f = ((9 * c + 160) / 5)
    print(f)

convert(c)