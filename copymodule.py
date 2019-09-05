def shallowCopy(*args):
    inputList = args
    print(type(inputList))
    inputList.append(4)
    return inputList

def deepCopy(*args):
    inputList = []
    inputList = args
    inputList.append(4)
    return inputList

