from math import ceil
class Message():
    
    @classmethod
    def worst_responseTime(cls,bit_time,target,obj_list):
        blocking_time = target.get_transmission_time()
        for i in range(0,len(obj_list)):
            if obj_list[i].get_priority() > target.get_priority() and blocking_time < obj_list[i].get_transmission_time():
                blocking_time = obj_list[i].get_transmission_time()

        Q = blocking_time
    
        while 1:
            RHS = blocking_time
            for i in range(0,len(obj_list)):
                if obj_list[i].get_priority()<target.get_priority():
                    RHS += ceil((Q + bit_time)/obj_list[i].get_period())*obj_list[i].get_transmission_time()
            
            if RHS + target.get_transmission_time() > target.get_period():
                break
            elif Q == RHS:
                return Q+target.get_transmission_time()
            else:
                Q = RHS
        return 'Constrain violation'



    def __init__(self, args):
        self.__priority = int(args[0])
        self.__transmission_time = float(args[1])
        self.__period = int(args[2])
    
    def __str__(self):
        return 'Priority= {0}\nTransmission Time= {1}\nPeriod= {2}'.format(self.__priority,self.__transmission_time,self.__period)

    def get_priority(self):
        return self.__priority
    
    def get_transmission_time(self):
        return self.__transmission_time
    
    def get_period(self):
        return self.__period

    def set_priority(self,n_priority):
        self.__priority = n_priority

    
if __name__ == '__main__':

    data_list = []
    with open("input.dat") as file_obj:
        for string in file_obj:
            data_list.append(string.strip())

    number_of_message = int(data_list[0])
    bit_transmission = float(data_list[1])

    message_list =[Message(data_list[i].split()) for i in range(2,len(data_list))]
    output_list=[]
    for i in range(0,number_of_message):
        output_list.append(Message.worst_responseTime(bit_transmission,message_list[i],message_list))
        print(output_list[i])
    


