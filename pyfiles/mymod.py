if __name__ != '__main__':
    name = input("enter file name: ")

    def countLines(name):
        """
        counts the number of lines in a file
        """
        f = open(name).readlines
        return print("There are {} no of lines".format(len(f())))

    def countChars(name):
        f = ''.join(open(name).read())
        return print('There are ', len(f.split()), ' no of characters')

    def test(namee):
        countLines(namee.seek(0)), countChars(namee.seek(0))
