class Call(object):
    def __init__(self, uniqueId, name, number, time, reason):
        self.id = uniqueId
        self.name = name
        self.number = number
        self.time = time
        self.reason = reason
    def display(self):
        print "Unique ID: %d\nName: %s\nNumber: %d\nTime: %d\nReason: %s" % (self.id, self.name, self.number, self.time, self.reason)
        return self

class CallCenter(Call):
    def __init__(self, calls):
        self.calls = calls
        self.queue = len(self.calls)
    def add(self, call):
        self.calls.append(call)
        return self
    def remove(self):
        self.calls.pop(0)
        return self
    def info(self):
        for i in self.calls:
            i.display()
        print "Queue: " + str(self.queue)


call = Call(123, 'Ethan', 415, 10, 'yes')
calls = CallCenter([call])
calls.info()
