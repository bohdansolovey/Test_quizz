from collections import Counter

def readArray(x, y):
    print('number of strings:', len(x))
    for el in x:
        print(el)
    print('number of requests:', len(y))
    for request in y:
        print(request)
    counter_x= Counter(x)
    for request in y:
        print(counter_x[request])


def enter_elements():
    x = []
    y = []
    try:
        choice = input('Enter number of strings, or \'path\ :')
        if choice == "path":
            try:
                path = input('Enter path to your file (If you use Windows type / not \\ :')
                data = []
                with open(path, 'r', encoding='UTF-8') as file:
                    for line in file.readlines():
                        data.append(line.strip())
                x_size = int(data[0])
                for index in range(1, x_size+1):
                    x.append(data[index])
                for ind in range(x_size+2,len(data)):
                    y.append(data[ind])
            except:
                print('no such file')
        else:
            choice = int(choice)
            for index in range(choice):
                x.append(input('enter string for x{}:'.format(index)))
            try:
                y_size = int(input('enter number of elements in requests array:'))
                for index in range(y_size):
                    y.append(input('enter request{}:'.format(index)))
            except:
                print("enter integer value!!!")
    except:
        print("Problem with input!")
    return x, y

x,y = enter_elements()
readArray(x,y)