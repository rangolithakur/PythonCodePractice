class GetAttrTest(object):
    """ class to verify getattr functinality
    without getattr method defined
    """
    def __init__(self):
        self.x = 'x'
        self.y = 'y'


class GetAttrWithDef(object):
    """ class to verify getattr functinality
    with getattr method defined inside class
    """
    def __init__(self):
        self.x = 'x'
        self.y = 'y'

    def __getattr__(self, item):
        print('getattr called')
        self.__dict__[item] = 0
        return 0

class GetAttributeTest(object):
    def __init__(self):
        self.x = 'x'
        self.y = 'y'

    def __getattribute__(self,item):
        print('getattribute called')
        if item.startswith('cur'):
            raise AttributeError
        return object.__getattribute__(self,item)
        
    
if __name__ == "__main__":
    
##        obj = GetAttrTest()
##        print('obj.x-{}'.format(obj.x))
##        print('obj.y-{}'.format(obj.y))
##        #print('obj.z-{}'.format(obj.z)) #Atrribte error
##        print(dir(obj))

        obj = GetAttrWithDef()
        print('obj.x-{}'.format(obj.x))
        print('obj.y-{}'.format(obj.y))
        print('obj.z-{}'.format(obj.z)) #getaatr method is called
        print(dir(obj))

        obj = GetAttributeTest()
        print('obj.x-{}'.format(obj.x))
        print('obj.y-{}'.format(obj.y))
        #print('obj.z-{}'.format(obj.z)) #getaatr method is called
        #print(dir(obj))
            
