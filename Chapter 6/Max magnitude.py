def max_magnitude(magnitudes):
    maximum = 0
    for x in magnitudes:
        if abs(maximum) <= abs(x):
            maximum = x
    return maximum

if __name__=="__main__":
    Magnitudes = []
    i=1
    print("To determine which of your three magnitudes is the largest, "
          "you will be asked to input all three into a list")
    while len(Magnitudes)<=2:
        response = int(input(f"Input magnitude #{i}:\n"))
        Magnitudes.append(response)
        i+=1
    print("You finished! your inputs are")
    print(Magnitudes)
    print(f"Your maximum magnitude is:",max_magnitude(Magnitudes))