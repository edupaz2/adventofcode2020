def check_program(instructions):
    acc = 0
    instruction_idx = 0
    visited = []
    while instruction_idx not in visited and instruction_idx < len(instructions):
        instruction = instructions[instruction_idx].strip()
        visited.append(instruction_idx)
        if instruction[:3] == "acc":
            acc += int(instruction[4:])
            instruction_idx += 1
        elif instruction[:3] == "jmp":
            instruction_idx += int(instruction[4:])
        else:
            instruction_idx += 1
    return acc, instruction_idx == len(instructions)

def execute1():
    f = open("inputfile.8.txt", "r")
    return check_program(f.readlines())

def execute2():
    f = open("inputfile.8.txt", "r")
    instructions = f.readlines()
    for i in range(len(instructions)):
        if instructions[i][:3] == "nop":
            instructions[i] = "jmp" + instructions[i][3:]
            acc, finished = check_program(instructions)
            if not finished:
                instructions[i] = "nop" + instructions[i][3:]
            else:
                return acc
        elif instructions[i][:3] == "jmp":
            instructions[i] = "nop" + instructions[i][3:]
            acc, finished = check_program(instructions)
            if not finished:
                instructions[i] = "jmp" + instructions[i][3:]
            else:
                return acc

if __name__ == "__main__":
    print(execute2())
