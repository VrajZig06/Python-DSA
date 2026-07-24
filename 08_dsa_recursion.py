# Recursion: Function that calls itself


# Example of Head Recurstion
count = 4
def recursion_name(count):
    if count == 0:
        return 
    
    print("Vraj")

    recursion_name(count - 1)

recursion_name(count)

# Example of Tail Recurstion
tail_count = 4
def tail_recursion_name(tail_count):
    if tail_count == 0:
        return 
    
    tail_recursion_name(tail_count - 1)
    
    print("Vraj")

    

tail_recursion_name(tail_count)