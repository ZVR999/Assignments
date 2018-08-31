import datetime
from operator import attrgetter
# Create a call blueprint

# Completed all including hacker level
# OOOOOOOOOOOOOOOOOOOHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHH LOL
class Call(object):
    def __init__(self,call_id,name,phone_number,called_at,reason):
        self.call_id = call_id
        self.name = name
        self.phone_number = phone_number
        self.called_at = called_at
        self.reason = reason
    # Display all information within a call
    def display(self):
        print "Call id: "+str(self.call_id)
        print "Caller's Name: "+str(self.name)
        print "Caller's Phone Number: "+str(self.phone_number)
        print "Time of call: "+str(self.called_at)
        print "Reason for call: "+str(self.reason)
    
# Create a call center blueprint
class CallCenter(object):
    def __init__(self):
        self.calls = []
        self.queue_size = 0
    # Add a call to the call list of the call center
    def add(self,call):
        call_list = self.calls
        call_list.append(call)
        return self
    # Remove a call from the call list of the call center
    def removeCall(self):
        call_list = self.calls
        if call_list != []:
            call_list.remove(call_list[0])
        return self
    # Remove a specific call from the call list of the call center according to their phone number 
    def removeSpecifc(self,phone_number):
        call_list = self.calls
        for call in call_list:
            if call.phone_number == phone_number:
                call_list.remove(call)
        return self
    # Display all name's and phone number's of caller waiting in call queue
    def info(self):
        call_list = self.calls
        length_of_queue = self.queue_size
        length_of_queue = len(call_list)
        
        for call in call_list:
            print "Caller's name: "+str(call.name)
            print "Caller's phone number: "+str(call.phone_number)
        print length_of_queue
    # Sort calls by time in ascending order. 
    def reSort(self):
        call_list = self.calls
        
        call_list.sort(key = attrgetter('called_at'))
        for call in call_list:
            print "Caller's name: "+str(call.name)
            print "Caller's phone number: "+str(call.phone_number)
            
# Random times that would be initally set by .now() but this is for testing
now = datetime.datetime(2000,1,10)
now1 = datetime.datetime(2000,2,11)
now2 = datetime.datetime(2000,3,12)
now3 = datetime.datetime(2000,4,13)
now4 = datetime.datetime(2000,5,14)
call_center = CallCenter()
call1 = Call(1,'John','789-555-4809',now,'Bored')
call2 = Call(2,'Marcus','789-555-4309',now1,'Bored')
call3 = Call(3,'Julie','789-555-4609',now2,'Bored')
call4 = Call(4,'Valis','789-555-4509',now3,'Bored')
call5 = Call(5,'Marie','789-555-4209',now4,'Hungry')
# call1.display()
# call_center.add(call1).add(call2).info()
# call_center.removeSpecifc('789-555-4809').info()

# call_center.add(call3).add(call1).add(call5).add(call2).info()
call_center.add(call4).add(call3).add(call1).add(call5).add(call2).reSort()
