class Call(object):
    def __init__(self, caller_id, caller_name, caller_phone, call_time, call_reason):
        self.caller_id = caller_id
        self.caller_name = caller_name
        self.caller_phone = caller_phone
        self.call_time = call_time
        self.call_reason = call_reason
    def display(self):
        print "\nCaller ID:", str(self.caller_id)
        print "Caller Name:", str(self.caller_name)
        print "Caller Phone:", str(self.caller_phone)
        print "Call Time:", str(self.call_time)
        print "Call Reason:", str(self.call_reason)
        return self

class CallCenter(object):
    def __init__(self):
        self.calls = []
        self.queue_size = 0
        self.caller_id = 0
    def add_call(self, caller_name, caller_phone, call_time, call_reason):
        self.caller_id += 1
        self.calls.append(Call(self.caller_id, caller_name, caller_phone, call_time, call_reason))
        self.queue_size += 1
        print "\nCALL ADDED"
        return self
    def remove_call(self):
        for x in range(1, self.queue_size):
            self.calls[x-1] = self.calls[x]
        self.calls.pop()
        print "\nCALL REMOVED"
        self.queue_size -= 1
        return self
    def show_caller_info(self):
        print "\nCallers in Queue..."
        for x in range(0, self.queue_size):
            print self.calls[x].display()
            # print "Caller Name:", x.caller_name
            # print "Caller ID:", str(x.caller_id)
        return self

my_call_center = CallCenter()

call1 = my_call_center.add_call("Tim", "222-333-4444", "4:10", "Needs help").show_caller_info()
call2 = my_call_center.add_call("Alex", "666-888-5555", "4:12", "Wants a refund").show_caller_info()
call3 = my_call_center.add_call("Max", "111-111-5555", "4:16", "Needs more help").remove_call().show_caller_info()
call4 = my_call_center.add_call("Jason", "455-666-8888", "4:20", "Return").show_caller_info()