f = open("10.txt", "r")

cycle_counter = 0
current_instruction = "noop"
current_instruction_counter = 1

x = 1
crt_output = ""

while True:
    cycle_counter += 1 # We are now *during* the cycle that we just started, the first is cycle 1
    current_instruction_counter -= 1

    if current_instruction_counter == 0:
        match current_instruction[:4]:
            case "noop": pass
            case "addx":
                x += int(current_instruction[5:])
        
        if not (current_instruction := f.readline()[:-1]):
            break
        
        match current_instruction[:4]:
            case "noop": current_instruction_counter = 1
            case "addx": current_instruction_counter = 2

    if abs((cycle_counter - 1) % 40 - x) <= 1:
        crt_output += "#"
    else:
        crt_output += "."
    
for i in range(0, len(crt_output), 40):
    print(crt_output[i:i+40])
