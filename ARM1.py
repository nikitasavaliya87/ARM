#instr=[, "","","","","","e1430005"] 
instruction=[0] * 7
instruction[0]= "e3a00001"
instruction[1]= "e3a01002"
instruction[2]= "e0802001"
instruction[3]= "e2822005"
instruction[4]= "e0815002"
instruction[5]= "e0415002"
instruction[6]="e1430005"


Registers=[0]*16
immediate_flag=0
cf=0
zf=0
#print(Registers)

def Register_display():
    print("Registers:")
    print("R0="+ str(Registers[0]) +"\t\t\t"+"R1="+str(Registers[1])+"\t\t\t"+ "R2="+str(Registers[2])+"\t\t\t"+"R3="+str(Registers[3]) +"\t\t\t")
    print("R4="+'{0:#0{1}x}'.format(Registers[4],10)+"\t\t\t"+ "R5="+'{0:#0{1}x}'.format(Registers[5],10)+"\t\t\t"+"R6="+'{0:#0{1}x}'.format(Registers[6],10) +"\t\t\t"+"R7="+'{0:#0{1}x}'.format(Registers[7],10) +"\t\t\t")
    print("R8="+'{0:#0{1}x}'.format(Registers[8],10)+"\t\t\t"+ "R9="+'{0:#0{1}x}'.format(Registers[9],10)+"\t\t\t"+"R10="+'{0:#0{1}x}'.format(Registers[10],10) +"\t\t\t"+"R11="+'{0:#0{1}x}'.format(Registers[11],10) +"\t\t\t")
    print("R12="+'{0:#0{1}x}'.format(Registers[12],10)+"\t\t\t"+ "R13="+'{0:#0{1}x}'.format(Registers[13],10)+"\t\t\t"+"R14="+'{0:#0{1}x}'.format(Registers[14],10) +"\t\t\t"+"R15="+'{0:#0{1}x}'.format(Registers[15],10) +"\t\t\t")    
    print("Carry Flag: "+str(cf))
    print("Zero Flag: "+str(zf)) 
    
    # print("OF: "+str(OF))
    # print("---------------------------------------------------------------------------------------------------------------")


                   
program_Counter=0
for i in instruction:       
    binary = "{0:08b}".format(int(i, 16)) 
    #print(res)                                       
    binary_format=str(binary)                                     # convert this binary to string
    #print(binary_format)
    opcode=binary_format[7:11]                               # fetch the opcode using get_opcode function
    #print(opcode)
    destination=int(i[4]) 
    print(destination)
    Registers[15]=program_Counter
    if binary_format[6]=="1":
        immediate_flag=1
        value=int(i[7])
        #print (value)
    else:
        immediate_flag=0
        Rm=int(i[7])
        #print(reg_n)
    if opcode=="1101":
        #Rm=int(i[7])
        Registers[destination]=value
           #print(Registers[destination])
        print("menemonics: "+ i+"\tMOV R"+str(destination)+" ,#"+str(value))
        #display()       
        
                  
       # print("Mov instruction")
    elif opcode=="0100":
        #print("Add instruction")
        Rn=int(i[3])
        if immediate_flag==1:
           
            Registers[destination]=Registers[Rn]+value
            print("menemonics: "+ i+"\tADD R"+str(destination)+", R"+str(Rn)+" ,#"+str(value))
        else:
            Registers[destination]=Registers[Rn]+Registers[Rm]
            print("menemonics: "+ i+"\tADD R"+str(destination) +", R"+str(Rn)+ " ,R"+str(Rm))

        
        

    elif opcode=="0010":
        print("Sub instruction")
        Rn=int(i[3])
        if immediate_flag==1:
            if Registers[Rn]<value:
                Registers[destination]=value-Registers[Rn]
                cf=1
            else:
                Registers[destination]=Registers[Rn]-value
                cf=0
            print("menemonics: "+ i+"\tSUB R"+str(destination)+", R"+str(Rn)+" ,#"+str(value))
        else:
            if Registers[Rn]<Registers[Rm]:
                Registers[destination]=Registers[Rm]-Registers[Rn]
                cf=1
            else:
                Registers[destination]=Registers[Rn]-Registers[Rm]
                cf=0
            print("menemonics: "+ i+"\tSUB R"+str(destination) +", R"+str(Rn)+ " ,R"+str(Rm))
    elif opcode=="1010":
        print("CMP instruction")
        Rn=int(i[3])
        if immediate_flag==1:
            if Registers[Rn]<value:
                cf=1
            elif Registers[Rn]>value:
                cf=0
            else:
                zf=1
            print("menemonics: "+ i+"\tCMP R"+str(Rn)+" ,#"+str(value))
        else:
            if Registers[Rn]<Registers[Rm]:
                cf=1
            elif Registers[Rn]>value:
                cf=0
            else:
                zf=1
            print("menemonics: "+ i+"\tCMP R"+str(Rn)+ " ,R"+str(Rm))

    program_Counter=program_Counter+4
    Register_display()