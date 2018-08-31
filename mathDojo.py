class MathDojo(object):
    def __init__(self):
        self.result = 0
    def add(self, *args):
        for arg in args:
            if type(arg) == int:
                self.result += arg
            if type(arg) == list or type(arg) == tuple:
                for value in arg:
                    self.result += value
        return self

    def subtract(self, *args):
        for arg in args:
            if type(arg) == int:
                self.result -= arg
            if type(arg) == list or type(arg) == tuple:
                for value in arg:
                    self.result -= value
        return self

    def results(self, *args):
        print self.result



md = MathDojo()
md.add([1], 3,4).add([3,5,7,8], [2,4.3,1.25]).subtract(2, [2,3], [1.1,2.3]).results()




