import os

file_path = os.path.abspath(__file__)
directory = os.path.dirname(file_path)

fruits = [
    "apple",
    "orange",
    "banana",
    "watermelon",
    "cherry",
    "blackberry",
    "peach",
    "pear",
]


def writeToFile(fruits, directory):
    try:

        with open(directory + "//fruits.txt", "w") as file:
            for item in fruits:
                file.write(f"{item}\n")

    except Exception as e:
        print(f"Error : {e}")


writeToFile(fruits, directory)


def readToFile(directory):
    try:
        with open(directory + "//fruits.txt", "r", encoding="utf-8") as file:
            for item in file:
                print(item.strip())
    except Exception as e:
        print(f"Error : {e}")


readToFile(directory)