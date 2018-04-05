class MathDojo(object):
    def __init__(self):
        self.result = 0
    def add(self, *a):
        for arg in a:
            if isinstance(arg, list) or isinstance(arg, tuple):
                for x in arg:
                    self.result += x
            else:
                self.result += arg
        return self
    def subtract(self, *a):
        for arg in a:
            if isinstance(arg, list) or isinstance(arg, tuple):
                for x in arg:
                    self.result += x
            else:
                self.result -= arg
        return self

md = MathDojo().add([1], 3,4).add((3,5,7,8), [2,4.3,1.25]).subtract(2, (2,3), [1.1,2.3]).result

print md