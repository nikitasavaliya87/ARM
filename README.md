# ARM
# ARM Software made in Python Language in 4 different way

# ARM Software Emulation

This project emulates ARM software instructions using Python. It converts given ARM instructions to their corresponding assembly mnemonics.

## Description

The Python script `ARM_Ass.py` takes a hexadecimal ARM instruction as input, decodes it, and converts it into its assembly language representation. It categorizes the instructions into Register Type and Immediate Type, fetching the opcode and corresponding registers involved in the instruction.

## Features

- Converts ARM instructions to assembly mnemonics
- Decode only one byte instruction and two byte instruction
- Decodes Register Type and Immediate Type instructions
- Generates the assembly language representation of the input ARM instruction

## Usage

1. Ensure Python is installed on your system.
2. Clone this repository.
3. Open `ARM_Ass.py`.
4. Run the script using `python ARM_Ass.py`.
5`. View the output displaying the assembly mnemonic of the input instruction.

## ARM Instruction Conversion

![image](https://github.com/nikitasavaliya87/ARM/assets/144912665/9c850bcc-000d-44a3-b269-91dd2192307e)

![image](https://github.com/nikitasavaliya87/ARM/assets/144912665/0bca2103-b86c-40b2-a794-48e15d43f846)


## Example

For the input instruction `e0802001`, the output will be `MOV R2,R1` as per the ARM assembly language.

## Known Limitations

- Limited to a subset of ARM instructions
- Three- Byte instruction is not working
- May not handle all edge cases of ARM instructions


## Contact Information

For queries or suggestions, contact nikita.savaliya16@gmail.com

