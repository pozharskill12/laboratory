def change(list):
    list[0], list[-1] = list[-1], list[0]
    print(list)

newList = [1, 2, 3, 4, 5]
listpin = ["a", "b", "c"]
change(listpin)