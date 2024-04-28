import regex as re

colour = {
    "black":"\033[0;30m",
    "red":"\033[0;31m",
    "green":"\033[0;32m",
    "yellow":"\033[0;33m",
    "blue":"\033[0;34m",
    "purple":"\033[0;35m",
    "cyan":"\033[0;36m",
    "white":"\033[0;37m",
}

def error(text):
    '''
    Prints error message in red text to the terminal
    '''
    print(colour["red"]+f"ERROR: {text}"+colour["white"])

def notify(text):
    '''
    Prints green text to the terminal
    '''
    print(colour["green"]+f"SUCCESS: {text}"+colour["white"])

def menu(class_obj):
    '''
    Calls a function based on the user's selection from available methods in the class object
    '''
    selection = input(getMethods(class_obj))
    func = {}
    for method in getMethods(class_obj):
        func[method] = getattr(class_obj, method)

    func[selection]()

def getMethods(class_obj):
    methods = []

    # Lambda function that check whether or not a method is callable
    is_method = lambda obj, func: callable(getattr(obj, func))
    # Lambda function that checks if a method is not double underscored
    is_pure = lambda func: re.fullmatch(r"^[^_].+[^_]$", func)

    for func in dir(class_obj):
        if is_method(class_obj, func) and is_pure(func):
            methods.append(func)

    # Methods are returned as strings
    return methods

def main():
    pass

if __name__ == "__main__":
    main()