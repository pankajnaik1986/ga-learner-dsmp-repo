# --------------
#Secret message parts in the correct order
message_parts=[secret_msg_3, secret_msg_1, secret_msg_4, secret_msg_2]

secret_msg = ' '.join(message_parts)
print('This is the secret message ',secret_msg)

final_path= user_data_dir + '/secret_msg.txt'

print('Printing final path :',final_path)

def write_file(secret_msg,path):
    file_open = open(path,mode = 'a+')
    file_open.write(secret_msg)
    file_open.close()






#Code starts here



# --------------
#Code starts here
file_path_6 

# print(file_path_6)
message_6 = read_file(file_path_6)
print('Message 6 :',message_6)

def extract_msg(message_f):
    a_list = message_f.split(" ")
    even_word = lambda x : len(x)%2 == 0 # Checking lenght of word 
    b_list = filter(even_word,a_list)
    final_msg = ' '.join(b_list)
    return final_msg

secret_msg_4 = extract_msg(message_6)

print('Secret Message 4 : ',secret_msg_4)







# --------------
##File path for the file 
file_path 

def read_file(path):
    path = open(path,'r')
    sentence = path.read()
    return sentence

sample_message = read_file(file_path)

#Code starts here


# --------------
# File path for message 4  and message 5
file_path_4
file_path_5

print('File Path 4 : ', file_path_4)
print('File Path 5 : ', file_path_5)

#Reading the file and storing into respective variables 
message_4 = read_file(file_path_4)
message_5 = read_file(file_path_5)

# Printing message 4 and message 5
print('Message 4 :',message_4)
print('Message 5 :',message_5)

def compare_msg(message_d,message_e):
    a_list = message_4.split(' ')
    b_list = message_5.split(' ')
    c_list = [i for i in a_list if i not in b_list]
    final_msg = " ".join(c_list)
    return final_msg

secret_msg_3 = compare_msg(message_4,message_5)
print(secret_msg_3)

#Code starts here






# --------------
#Code starts here
import math 

file_path_1
file_path_2

message_1 = read_file(file_path_1)
message_2 = read_file(file_path_2)

print('Message from First File  : ',message_1)
print('Message from Second File : ',message_2)

def fuse_msg(message_a,message_b):
        message_a = int(message_a)
        message_b = int(message_b)
        quotient = math.floor(message_b/message_a)
        return str(quotient)

secret_msg_1 = fuse_msg(message_1,message_2)

print('Message from Secret File :',secret_msg_1)




# --------------
#Code starts here
import math

file_path_3

print('File Path 3 :',file_path_3)

#Reading file 3 and storing value in file message_3
message_3 = read_file(file_path_3)
print('Message from File 3 :',message_3)

#Defining Function 

def substitute_msg(message_c):
    sub =''
    if message_c == 'Red':
        sub = 'Army General'
    elif message_c =='Green':
        sub = 'Data Scientist'
    else:
        sub = 'Marine Biologist'
    return sub

secret_msg_2 =substitute_msg(message_3)

print('Secret Message 2 : ',secret_msg_2)




