with open("./Practiceset/twinkel.txt", "r") as text:
        data = text.read()  # Convert to lowercase for case-insensitive check
        if "twinkle" in data:  # Ensure correct spelling
            print("It has 'twinkle'")
        else:
            print("It does not have 'twinkle'")