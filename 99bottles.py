bottles = input("How many bottles of beer will we start with? ")
total = int(bottles)
def song(bottles=99):
    num = int(bottles)
    delim = "------------------------------------------------------------"
    if num > 2:
        print(num, "bottles of beer on the wall!")
        print(num, "bottles of beer!")
        print("Take one down")
        print("And pass it around")
        print((num - 1), "more bottles of beer on the wall!")
        print(delim)
    elif num == 2:
        print(num, "bottles of beer on the wall!")
        print(num, "bottles of beer!")
        print("Take one down")
        print("And pass it around")
        print((num - 1), "more bottle of beer on the wall!")
        print(delim)
    elif num == 1:
        print(num, "bottle of beer on the wall!")
        print(num, "bottle of beer!")
        print("Take one down")
        print("And pass it around")
        print("No more bottles of beer on the wall!")
        print(delim)


while total > 0:
    song(total)
    total -= 1
if total == 0:
    print("Crisis! No beer.")
