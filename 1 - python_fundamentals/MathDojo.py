class MathDojo(object):
    def __init__(self):
        self.result = 0
    def add(self, *num):
        for i in num:
            if type(i) == list or type(i) == tuple:
                for k in i:
                    self.result += k
            else:
                self.result += i
        return self
    def subtract(self, *num):
        for i in num:
            if type(i) == list or type(i) == tuple:
                for k in i:
                    self.result -= k
            else:
                self.result -= i
        return self
print MathDojo().add(2).add(2, 5).subtract(3, 2).result
print MathDojo().add([1],3,4).add([3, 5, 7, 8], [2, 4.3, 1.25]).subtract(2, [2,3], [1.1, 2.3]).result
i = 5
print MathDojo().add(i).add(2,3).add((1,2)).result
