# Two-Pass Assembler: Pass-I
# Input: Assembly program as list of lines
# Output: Symbol table, Literal table, Intermediate code

# Sample Assembly Program
asm_code = [
    "START 200",
    "MOVER AREG, ='5'",
    "MOVEM AREG, X",
    "L1 MOVER BREG, ='2'",
    "ORIGIN L1+3",
    "LTORG",
    "NEXT ADD AREG, ='1'",
    "SUB BREG, ='2'",
    "BC LT, BACK",
    "LTORG",
    "BACK EQU L1",
    "ORIGIN NEXT+5",
    "MULT CREG, ='4'",
    "STOP",
    "X DS 1",
    "END"
]

# Initialize tables
SYMTAB = {}
LITTAB = {}
POOLTAB = [0]
intermediate_code = []

LC = 0  # Location Counter
pool_index = 0

# Predefined Opcode table
OPTAB = {
    'STOP': '00', 'ADD': '01', 'SUB': '02', 'MULT': '03', 'MOVER': '04',
    'MOVEM': '05', 'BC': '06', 'ORIGIN': '', 'EQU': '', 'LTORG': '', 'DS': '', 'DC': ''
}

# Function to handle literals
def process_literals():
    global LC, pool_index
    for lit, addr in LITTAB.items():
        if addr == -1:
            LITTAB[lit] = LC
            intermediate_code.append(f"{LC}\t(AD,=){lit}")
            LC += 1
    POOLTAB.append(len(LITTAB))

# Pass-I
for line in asm_code:
    tokens = line.split()
    if not tokens:
        continue
    
    if tokens[0] == 'START':
        LC = int(tokens[1])
        intermediate_code.append(f"{LC}\t(AD,START)\t{tokens[1]}")
    
    elif tokens[0] in OPTAB:
        opcode = tokens[0]
        operands = ''.join(tokens[1:]).split(',')
        # Check for literals
        for op in operands:
            if op.startswith('='):
                if op not in LITTAB:
                    LITTAB[op] = -1
        intermediate_code.append(f"{LC}\t(IS,{OPTAB.get(opcode,'')})\t{','.join(operands)}")
        LC += 1
    
    elif tokens[0] == 'ORIGIN':
        label_expr = tokens[1]
        # Simple handling: assume label + number
        if '+' in label_expr:
            label, num = label_expr.split('+')
            LC = SYMTAB[label] + int(num)
        elif '-' in label_expr:
            label, num = label_expr.split('-')
            LC = SYMTAB[label] - int(num)
        else:
            LC = SYMTAB[label_expr]
        intermediate_code.append(f"{LC}\t(AD,ORIGIN)\t{tokens[1]}")
    
    elif tokens[0] == 'LTORG':
        process_literals()
        intermediate_code.append(f"{LC}\t(AD,LTORG)")
    
    elif tokens[0] == 'EQU':
        SYMTAB[tokens[0]] = SYMTAB[tokens[1]]
    
    elif tokens[0] not in OPTAB:
        # Label definition
        label = tokens[0]
        if label not in SYMTAB:
            SYMTAB[label] = LC
        opcode = tokens[1]
        operands = ''.join(tokens[2:]).split(',')
        for op in operands:
            if op.startswith('='):
                if op not in LITTAB:
                    LITTAB[op] = -1
        intermediate_code.append(f"{LC}\t(IS,{OPTAB.get(opcode,'')})\t{','.join(operands)}")
        LC += 1
    
    # DS and DC
    if 'DS' in tokens:
        SYMTAB[tokens[0]] = LC
        LC += int(tokens[-1])
        intermediate_code.append(f"{LC}\t(DL,DS)\t{tokens[-1]}")

    if 'DC' in tokens:
        SYMTAB[tokens[0]] = LC
        LC += 1
        intermediate_code.append(f"{LC}\t(DL,DC)\t{tokens[-1]}")

# Process remaining literals at the end
process_literals()

# Display Symbol Table
print("\nSymbol Table (SYMTAB):")
for sym, addr in SYMTAB.items():
    print(f"{sym}\t{addr}")

# Display Literal Table
print("\nLiteral Table (LITTAB):")
for lit, addr in LITTAB.items():
    print(f"{lit}\t{addr}")

# Display Intermediate Code
print("\nIntermediate Code:")
for ic in intermediate_code:
    print(ic)
