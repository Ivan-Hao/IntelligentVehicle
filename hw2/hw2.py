from hw1 import Message
from random import random, shuffle
from math import exp
from time import time

def cost_function(time_list):
    if 'Constrain violation' in time_list:
        return 're-do'
    else:
        return sum(time_list)

if __name__ == '__main__':

    data_list = []
    with open("input.dat") as file_obj:
        for string in file_obj:
            data_list.append(string.strip())

    number_of_message = int(data_list[0])
    bit_transmission = float(data_list[1])

    message_list =[Message(data_list[i].split()) for i in range(2,len(data_list))]
    
    initial_list=[]
    for i in range(0,number_of_message):
        initial_list.append(Message.worst_responseTime(bit_transmission,message_list[i],message_list))
    

    initial_priority = [data_list[n].split()[0] for n in range(2,len(data_list))] #s
    
    state_priority = initial_priority.copy() #s* = s
    state_cost = cost_function(initial_list) #cost(s)
    

    initial_time = time() 
    T = 1000 #T

    while 1:

        output_list=[]
        new_priority = initial_priority.copy()
        shuffle(new_priority) #pick a random neighbor s' of s
        
        for i in range(number_of_message):
            message_list[i].set_priority(new_priority[i])

        for i in range(number_of_message):
            output_list.append(Message.worst_responseTime(bit_transmission,message_list[i],message_list))
        new_cost = cost_function(output_list) #cost(s')
        
    
        if new_cost == 're-do':
            pass
        else:
            de_cost = new_cost - state_cost #delta C = cost(s') - cost(s)
            
            if new_cost < state_cost:
                state_cost = new_cost
                state_priority = new_priority.copy() #s* = s'

            if de_cost <= 0:
                initial_priority = new_priority.copy() #s = s'
            elif de_cost > 0:
                if random() < exp(-de_cost/T):
                    
                    initial_priority = new_priority.copy() #s = s' with probability e–ΔC/T
                


        end_time = time() 
        if (end_time-initial_time) > 300:
            break

        T = 0.9*T #T = rT (where r < 1)
    
    for i in range(len(state_priority)):
        print(state_priority[i])
    print(state_cost)
        
