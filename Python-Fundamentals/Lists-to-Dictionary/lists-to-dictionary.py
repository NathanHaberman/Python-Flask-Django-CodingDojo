name = ["Anna", "Eli", "Pariece", "Brendan", "Amy", "Shane", "Oscar"]
favorite_animal = ["horse", "cat", "spider", "giraffe", "ticks", "dolphins", "llamas", "bears"]

def make_dict(arr1, arr2):
    new_dict = {}
    longer = arr1
    shorter = arr2
    if len(arr2) > len(arr1):
        longer = arr2
        shorter = arr1
    for i in range(len(shorter)):
        new_dict[longer[i]] = shorter[i]
    print new_dict

make_dict(name, favorite_animal)