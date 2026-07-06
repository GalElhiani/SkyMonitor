#this module is an implementation of a tracking cloud services costs through machine state changes
#Author: Gal ELhiani
#Tester: Meytar

from datetime import datetime

class Machine:
    '''a base representation of a tracked infrastructure machine'''
    tracking_table = []
    def __init__(self, type, name):
        '''initializes a machine instance and registers it to the tracking table'''
        self.type = type
        self.name = name
        self.is_running = False
        self.start_time = None
        self.stop_time = None

        Machine.tracking_table.append(self)
    
    def __repr__(self):
         return f"Machine: {self.name}, {self.type}"


    def start_machine(self, current_time=None):
            '''starts the machine and records the start timestamp'''
            if not self.is_running:
                self.is_running = True
                self.start_time = current_time if current_time else datetime.now()
                return self.start_time
            raise RuntimeError("the machine is already on!")
        
    def stop_machine(self, current_time=None):
            '''stops the machine and records the stop timestamp'''
            if self.is_running:
                self.is_running = False
                self.stop_time = current_time if current_time else datetime.now()
                return self.stop_time
            raise RuntimeError("the machine is already off!")
    
    def get_time(self, current_time=None):
        '''calculates the total runtime in minutes'''
        if self.start_time is None:
            return 0

        if self.is_running:
             end = current_time if current_time else datetime.now()
             total_duration = end - self.start_time
        else:
             total_duration = self.stop_time - self.start_time

        return total_duration.total_seconds() / 60        

    def get_price(self, current_time=None):
        '''calculates the accumulated cost for this machine'''
        return (self.get_time(current_time)) * self.cpm

    @classmethod
    def get_total_price(cls, current_time=None):
        '''calculates the combined cost of all tracked machines'''
        total = 0
        for machine in cls.tracking_table:
            total+= machine.get_price(current_time)
        return total


class MachineType1(Machine):
    '''initializes a type 1 machine with a cost of 2 per minute'''
    def __init__(self, type, name):
        super().__init__(type, name)
        self.cpm = 2

class MachineType2(Machine):
    '''initializes a type 2 machine with a cost of 5 per minute'''
    def __init__(self, type, name):
        super().__init__(type, name)
        self.cpm = 5



