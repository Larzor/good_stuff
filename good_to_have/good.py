def getInputBetween(startval:int, endval:int)->int:
    while True:
        try:
            val=int(input("Matain: "))
            if val >= startval and val <= endval:
                return val
        except:
            print("Ange ett tal tack!")


if __name__ == "__main__":
    x = getInputBetween(100, 200)
    print(x)

# python -m venv env