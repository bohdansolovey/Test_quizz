
def getKey(item):
    return item[3]





def output(list_of_tuples):
    list_of_tuples = sorted(list_of_tuples, key = getKey)
    for elements in list_of_tuples:
        name, surname, gender, age = elements
        if gender in ['M', 'm', 'man', 'male', 'Man', 'Male']:
            print('Господин %s %s'%(name,surname))
        else:
            print('Госпожа %s %s'%(name,surname))


def enter_decorator(fn):
    def wrapped():
        try:
            choice = input('Enter number of peoples, or \'path\ :')
            if choice == "path":
                try:
                    path = input('Enter path to your file (If you use Windows type / not \\ :')
                    with open(path, 'r', encoding='UTF-8') as file:
                        data = []
                        for line in file.readlines():
                            name, surname, gender, age = line.split()
                            fn(name, surname, gender, age, data)
                    output(data)
                except:
                    print('no such file')
            else:
                data = []
                choice = int(choice)
                for i in range(0, choice):
                    name, surname,  gender, age = input('Enter Name, Surname,  Gender( M / F ), Age(number): ').split()
                    fn(name, surname, gender, age, data)
                output(data)
        except:
            print("except")

        print("<\_____/>")
    return wrapped


@enter_decorator
def taking_params(name, surname, gender, age, data):
    if gender not in ['M', 'm', 'man', 'male', 'Man', 'Male', 'F', 'f', 'female', 'Female']:
        print('retype:')
        name, surname, gender, age = input('Enter Name, Surname,  Gender( M / F ), Age(number): ').split()
    data.append((name, surname, gender, age))

taking_params()

