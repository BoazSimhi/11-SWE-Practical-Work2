alpha_part = ["a", "b", "c", "d", "e"]    #[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
item = "d" #alpha_part[6]

#print(alpha_part.index(item)) # But why do all this code when this one line pretty much works the whole thing?

lower_bound = 0
upper_bound = len(alpha_part) - 1
found = False

while True:
    if found == False and lower_bound <= upper_bound:
        midpoint = (lower_bound + upper_bound) // 2
        if alpha_part[midpoint] == item:
            found = True
        try:
            if alpha_part[midpoint] <= alpha_part.index(item):#item:
                lower_bound = midpoint + 1
        except:
            if item in alpha_part:
                if alpha_part.index(midpoint) <= alpha_part.index(item):
                    lower_bound = midpoint + 1
                elif alpha_part.index(midpoint) >= alpha_part.index(item):
                    upper_bound = midpoint - 1
            else:
                print("Item not found.")
                break
        else:
            upper_bound = midpoint - 1
    else:
        if found:
            print("Item found at", midpoint)
        else:
            print("Item not found.")
        break
