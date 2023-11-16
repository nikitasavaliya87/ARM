import math
instruction_set={"1101":"MOV","0100":"ADD","0000":"AND","0010":"SUB"}
register={"0000":"R0","0001":"R1","0010":"R2","0011":"R3","0100":"R4"}
def bin_hex(ini_string):

  
    # Initialising hex string
    #ini_string = str
    
    # Printing initial string
    print ("Initial string", ini_string)
    
    # Code to convert hex to binary
    res = "{0:08b}".format(int(ini_string, 16))
    
    # Print the resultant string
    print ("Resultant string", str(res))
    return res

def get_opcode(res_str):  #fetch the Opcode
    opcode=res_str[7:11]    #opcode at position 21-24 bit in instruction
    i=instruction_set.get(opcode)
    return i

def Destination_reg(res_str):
    rd_opcode=res_str[16:20]
    rd=register.get(rd_opcode)
    #print(rd)
    return rd

def Source_reg(res_str):
    rs_opcode=res_str[13:17]
    rs=register.get(rs_opcode)
    #print(rd)
    return rs

instr="e0802001"
#instr[1]="e2822005"

#for pc in instr:

res=bin_hex(instr)
res_opcode=str(res)
if res_opcode[7]=="0":
    dest_reg=Destination_reg(res)
    sour_reg=Source_reg(res)
    print("register")

    #Register Type Instruction
else:
    print("Immediate")
    #immediate Instruction
op=get_opcode(res_opcode)
# for i in instruction_set.items:
#     if opcode==:
#         print(instruction_set[i])
print("opcode \t\t\t Assembley menemonics")
print("_______________________________________________")
print(instr+"\t\t"+op+" "+dest_reg+","+sour_reg)
#print(op)