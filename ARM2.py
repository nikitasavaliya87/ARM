memory=["e3a00001", "e3a01002","e0802001","e2822005","e0815002","e0415002","e1430005","e3450006"]   # create memory array for hexadecimal opcode
registers=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0] #intialize 15 registers with value 0
carry_flag=0 # intialize carry flag is 0
zero_flag=0  # intialize zero flag is 0
pc=0           #intialize program couter is 0

def hextobinary(inst):          # function for converting hexa to binary format
    
    n = int(inst, 16)
    bStr = ''           # intialize bstr as null
    while n > 0:        # check value of n is greater than 0
        bStr = str(n % 2) + bStr        # perform modulo by 2 and concate with bstr for binary string
        n = n >> 1   # Bits are shifted to right by number 1
    result = bStr  # store the value into the bstr
    return result       # return result by function called

def show():         # function for showing the value of 15 registers
    
    print("R0:"+str(registers[0]))
    print("R1:"+str(registers[1]))
    print("R2:"+str(registers[2]))
    print("R3:"+str(registers[3]))
    print("R4:"+str(registers[4]))
    print("R5:"+str(registers[5]))
    print("R6:"+str(registers[6]))
    print("R7:"+str(registers[7]))
    print("R8:"+str(registers[8]))
    print("R9:"+str(registers[9]))
    print("R10:"+str(registers[10]))
    print("R11:"+str(registers[11]))
    print("R12:"+str(registers[12]))
    print("R13:"+str(registers[13]))
    print("R14:"+str(registers[14]))
    print("R15:"+str(registers[15]))
    

def immediate_decoding(inst):   # immediate_decoding function for decoding immediate type instruction
    opcode=inst[7:11]              # fetch the opcode from insr at position 21-24
    Reg_Dest=int(inst[16:20],2)   # convert destination register which store at position 15 to 12 bit into integer format
    immediate_value=int(inst[28:32],2)    # convert immediate value which store at position 0 to 4 bit into integer format
    Reg_N=int(inst[12:16],2)   # convert register N value which store at position 19 to 16 bit into integer format
    carry_flag=0        # define carry flag is 0
    zero_flag=0         # define zero flag is 0


    if opcode=="1101":      # check the opcode= 1101 then it is MOV instruction
        instrution_name="MOV"       # store the "MOV" string into the instrution_name
        registers[Reg_Dest]=immediate_value     #store the immediate value into the appropriate destination registers.
        print("\n"+instrution_name+ " R"+str(Reg_Dest)+" ,#"+str(immediate_value))   # print assembly menemonics
        #print("Carry Flag="+str(carry_flag)+"\t Zero Flag="+str(zero_flag))
       
    elif opcode=="0100":    # check the opcode= 0100 then it is ADD instruction
        instrution_name="ADD"  # store the "ADD" string into the instrution_name
        registers[Reg_Dest]=registers[Reg_N]+immediate_value  #add the immediate value with register N and store into the appropriate destination registers.
        print(str(inst)+"\t\t\t"+ instrution_name+ " R"+str(Reg_Dest)+", R"+str(Reg_N) +" ,#"+str(immediate_value))    # print assembly menemonics
        #print("Carry Flag="+str(carry_flag)+"\t Zero Flag="+str(zero_flag))


    elif opcode=="0010":     # check the opcode= 0010 then it is SUB instruction
        instrution_name="SUB"   # store the "SUB" string into the instrution_name
        if registers[Reg_N]<immediate_value:  # check the immediate value is higher than register N
            registers[Reg_Dest]=immediate_value-registers[Reg_N] #subtraction the immediate value with register N and store into the appropriate destination registers.
            carry_flag=1        # set carryflag as 1
            
        else:   # otherwise 
            registers[Reg_Dest]=registers[Reg_N]-immediate_value   #subtraction the register Nwith immediate value  and store into the appropriate destination registers.
            if registers[Reg_Dest]==0: #check the appropriate destination register value if it is 0 then
                zero_flag=1    # set the zero flag as 1
            carry_flag=0      #set the carry flag is 0
        print(str(inst)+"\t\t\t"+ instrution_name+ " R"+str(Reg_Dest)+", R"+str(Reg_N) +" ,#"+str(immediate_value))  # print assembly menemonics
        #print("Carry Flag="+str(carry_flag)+"\t Zero Flag="+str(zero_flag))


    elif opcode =="1010":  # check the opcode= 1010 then it is CMP instruction
        instrution_name="CMP"       # store the "CMP" string into the instrution_name
        if registers[Reg_N]<immediate_value:  # check the immediate value is higher than register N
            temp=immediate_value-registers[Reg_N] #subtraction the immediate value with register N and store into the temporary temp registers.
            carry_flag=1      # set carryflag as 1
        else:               # otherwise
            temp=registers[Reg_N]-immediate_value #subtraction the register N with immediate value  and store into the temporary temp registers.
            if temp==0:  #check the temp variable is 0
              
                zero_flag=1     # set the zero flag as 1
            carry_flag=0   #set the carry flag is 0
        print(str(inst)+"\t\t\t"+ instrution_name+ " R"+str(Reg_N)+" ,#"+str(immediate_value))   # print assembly menemonics
        #print("Carry Flag="+str(carry_flag)+"\t Zero Flag="+str(zero_flag))

    show()   # call the show function to show the status of each registers
    print("Carry Flag="+str(carry_flag)+"\t Zero Flag="+str(zero_flag)) #print the appropriate flags value

def register_decoding(inst):   # register_decoding function for decoding register type instruction
    opcode=inst[7:11]            # fetch the opcode from insr at position 21-24
    Reg_Dest=int(inst[16:20],2)  # convert destination register which store at position 15 to 12 bit into integer format
    Reg_M=int(inst[28:32],2)    # convert register M value which store at position 0 to 04 bit into integer format
    Reg_N=int(inst[12:16],2)    # convert register N value which store at position 19 to 16 bit into integer format
    carry_flag=0                # define carry flag is 0
    zero_flag=0                 # define zero flag is 0
        
    if opcode=="0100":    # check the opcode= 0100 then it is ADD instruction
        instrution_name="ADD"   # store the "ADD" string into the instrution_name
        registers[Reg_Dest]=registers[Reg_N]+registers[Reg_M]   #add the appropraite register M with register N and store into the appropriate destination registers.
        print(str(inst)+"\t\t\t"+ instrution_name+ " R"+str(Reg_Dest)+", R"+str(Reg_N) +" ,R"+str(Reg_M))  # print assembly menemonics
        #print("Carry Flag="+str(carry_flag)+"\t Zero Flag="+str(zero_flag))


    elif opcode=="0010":
        instrution_name="SUB"
        if registers[Reg_N]<registers[Reg_M]:
            registers[Reg_Dest]=registers[Reg_M]-registers[Reg_N]
            carry_flag=1
        else:
            registers[Reg_Dest]=registers[Reg_N]-registers[Reg_M]
            if registers[Reg_Dest]==0:
                zero_flag=1
        print(str(inst)+"\t\t\t"+ instrution_name+ " R"+str(Reg_Dest)+", R"+str(Reg_N) +" ,R"+str(Reg_M))
        #print("Carry Flag="+str(carry_flag)+"\t Zero Flag="+str(zero_flag))
    else:
        instrution_name="CMP"
        if registers[Reg_N]<registers[Reg_M]:
            temp=registers[Reg_M]-registers[Reg_N]
            carry_flag=1
        else:
            temp=registers[Reg_N]-registers[Reg_M]
            if temp==0:
                carry_flag=0
                zero_flag=1

        print(str(hex(int(inst)))+"\t\t\t"+ instrution_name+ " R"+str(Reg_N)+" ,#"+str(Reg_M))
        #print("Carry Flag="+str(carry_flag)+"\t Zero Flag="+str(zero_flag))

    show()
    print("Carry Flag="+str(carry_flag)+"\t Zero Flag="+str(zero_flag))


for i in memory:        # fetch one by one instruction in memory array

    instruction=hextobinary(i)      # convert hexadecimal number to binary format and store in instruction variable
    if instruction[4]=="0":         #check bit 27 is 0
         if instruction[5]=="0":    # check bit 26 is 0
             if instruction[6]=="1":  # check bit 25 is one for immediate value
                 #print("immediate Addressing")
                 immediate_decoding(instruction)    #call the immediate_decoding function
             else:                  # otherwise call register_decoding function
                 #print("Register")
                 register_decoding(instruction) 
    registers[15]=pc    # store thae value of pc into the register 15
    pc=pc+4             # increment pc by value 4


 
