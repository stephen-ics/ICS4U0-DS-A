from Classes.Pokemon.pokemon import Pokemon
from Classes.Pokemon.squirtle import Squirtle
import random
import time

def linearSearch(array, target):
    arrayLength = len(array)
    # Going through array sequencially
    for i in range(0, arrayLength):
        if (array[i].getId() == target):
            return i
    return -1

def binarySearch(array, target):
    left = 0
    right = len(array) - 1
    while (left  <= right):
        mid = (right + left) // 2
        if array[mid].getId() == target:
            return mid
        elif array[mid].getId() < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1 

def selectionSort(array):
    arrayLength = len(array)
    for i in range(arrayLength):
        minIndex = i
        for j in range(i + 1, arrayLength):
            # select the minimum element in every iteration
            if array[j].level < array[minIndex].level:
                minIndex = j
        # swapping the elements to sort the array
        (array[i], array[minIndex]) = (array[minIndex], array[i])

arrayValues = [1, 5, 10, 20, 50, 100, 500, 1000, 5000, 10000, 20000, 30000, 50000, 75000, 100000, 125000, 150000]
squirtleList = []
nameList = ["Joe", "Bob", "Ariel", "Barbunda", "Naruto", "Chris", "Jewl", "Joseph", "Aaron", "Pikachu", "Axel", "Turtle", "Squirrtle", "Blob", "Fish", "Deca", "Dan", "Dani", "Semi", "Doggo", "Blast", "Ken", "Denten", "Tenten", "Carlos", "Mustafa", "Mansen", "Hansen", "Ulta", "Tyla", "Tigga", "Tiner", "Dingo"]
for arrayValue in arrayValues:
    linearBeforeSortedRC = []
    linearAfterSortedRC = []
    binaryAfterSortedRC= []
    builtInSortRC = []
    selectionSortRC = []

    linearBeforeSortedWC = []
    linearAfterSortedWC = []
    binaryAfterSortedWC= []
    builtInSortWC = []
    selectionSortWC = []
    with open("output.txt", "a") as file:
        file.write("\n----------------------------------------------")
        file.write("\nFor case with array values: " + str(arrayValue))
        file.write("\n----------------------------------------------")
        file.close
    
    for j in range(25):
        for i in range(arrayValue):
            level = random.randint(0,10000)
            hp = random.randint(0,10000)
            attack = random.randint(0,10000)
            defense = random.randint(0,10000)
            speed = random.randint(0,10000)
            name = random.randint(0,32)
            wearingSunglassesNum = random.randint(0,1)
            wearingSunglasses = False
            if wearingSunglassesNum == 0:
                wearingSunglasses = True
            currentSquirtleObject = Squirtle(nameList[name], level, hp, attack, defense, speed, "Water", i, wearingSunglasses)
            squirtleList.append(currentSquirtleObject)

        # Random Case
        randomIndex = random.randint(0, len(squirtleList)-1)

        target = randomIndex
        start = time.time()
        result = linearSearch(squirtleList, target)
        end = time.time()
        linearTime = end-start
        linearBeforeSortedRC.append(linearTime)

        # Built-in Sort
        start = time.time()
        result = sorted(squirtleList, key=lambda squirtle: squirtle.level)
        end = time.time()
        builtInSortTime = end-start
        builtInSortRC.append(builtInSortTime)

        # Selection sort
        start = time.time()
        selectionSort(squirtleList)
        end = time.time()
        selectionTime = end-start
        selectionSortRC.append(selectionTime)

        # After sorting linear search
        target = randomIndex
        start = time.time()
        result = linearSearch(squirtleList, target)
        end = time.time()
        linearTime = end-start
        linearAfterSortedRC.append(linearTime)

        # After sorting binary search
        target = len(squirtleList)-1
        start = time.time()
        result = binarySearch(squirtleList, target)
        end = time.time()
        binaryTime = end-start
        binaryAfterSortedRC.append(binaryTime)

        # Worst Cases
        squirtleList2 = []
        for i in range(arrayValue):
            level = random.randint(0,10000)
            hp = random.randint(0,10000)
            attack = random.randint(0,10000)
            defense = random.randint(0,10000)
            speed = random.randint(0,10000)
            name = random.randint(0,32)
            wearingSunglassesNum = random.randint(0,1)
            wearingSunglasses = False
            if wearingSunglassesNum == 0:
                wearingSunglasses = True
            currentSquirtleObject = Squirtle(nameList[name], level, hp, attack, defense, speed, "Water", i, wearingSunglasses)
            squirtleList2.append(currentSquirtleObject)

        squirtleList2[len(squirtleList2)-1] = (Squirtle("lastSquirtle", 2, 2, 2, 2, 2, "Water", len(squirtleList2)-1, False))

        # Before sorting linear search
        target = len(squirtleList2)-1
        start = time.time()
        result = linearSearch(squirtleList2, target)
        end = time.time()
        linearTime = end-start
        linearBeforeSortedWC.append(linearTime)

        # Built-in Sort
        start = time.time()
        result = sorted(squirtleList2, key=lambda squirtle: squirtle.level)
        end = time.time()
        builtInSortTime = end-start
        builtInSortWC.append(builtInSortTime)

        # Selection sort
        start = time.time()
        selectionSort(squirtleList2)
        end = time.time()
        selectionTime = end-start
        selectionSortWC.append(selectionTime)   

        # After sorting linear search
        target = len(squirtleList2)-1
        start = time.time()
        result = linearSearch(squirtleList2, target)
        end = time.time()
        linearTime = end-start
        linearAfterSortedWC.append(linearTime)

        # After sorting binary search
        target = len(squirtleList2)-1
        start = time.time()
        result = binarySearch(squirtleList2, target)
        end = time.time()
        binaryTime = end-start
        binaryAfterSortedWC.append(binaryTime)

    with open("output.txt", "a") as file:
        file.write("\nBefore Sorted Linear Search Random Case #1-25")
        for i in range(25):
            file.write("\n" + str(linearBeforeSortedRC[i]))
            file.close
        file.write("\nBuilt in Sort Random Case #1-25")
        for i in range(25):
            file.write("\n" + str(builtInSortRC[i]))
            file.close
        file.write("\nSelection Sort Random Case #1-25")
        for i in range(25):
            file.write("\n" + str(selectionSortRC[i]))
            file.close
        file.write("\nAfter Sorted Linear Search Random Case #1-25")
        for i in range(25):
            file.write("\n" + str(linearAfterSortedRC[i]))
            file.close
        file.write("\nAfter Sorted Binary Search Random Case #1-25")
        for i in range(25):
            file.write("\n" + str(binaryAfterSortedRC[i]))
            file.close
        file.write("\nWorst Case")

        file.write("\nBefore Sorted Linear Search Worst Case #1-25")
        for i in range(25):
            file.write("\n" + str(linearBeforeSortedWC[i]))
            file.close
        file.write("\nBuilt in Sort Worst Case #1-25")
        for i in range(25):
            file.write("\n" + str(builtInSortWC[i]))
            file.close
        file.write("\nSelection Sort Worst Case #1-25")
        for i in range(25):
            file.write("\n" + str(selectionSortWC[i]))
            file.close
        file.write("\nAfter Sorted Linear Search Worst Case #1-25")
        for i in range(25):
            file.write("\n" + str(linearAfterSortedWC[i]))
            file.close
        file.write("\nAfter Sorted Binary Search Worst Case #1-25")
        for i in range(25):
            file.write("\n" + str(binaryAfterSortedWC[i]))
            file.close
        file.write("\n")
        file.close


