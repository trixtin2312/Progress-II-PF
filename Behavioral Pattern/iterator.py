def count_on(count):
    # Our list
    number_of_words = ["A", "В", "C", "D", "E", "L"]
    iterator = zip(range(count), number_of_words)
    for position, alphabets in iterator:
        yield alphabets


for num in count_on(5):
    print("{}".format(num))