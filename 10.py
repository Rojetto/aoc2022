f = open("10.txt", "r")

cycle_counter = 0
current_instruction = "noop"
current_instruction_counter = 1

x = 1
signal_strength_sum = 0

reached_end = False

while not reached_end:
    cycle_counter += 1 # We are now *during* the cycle that we just started, the first is cycle 1
    current_instruction_counter -= 1

    if current_instruction_counter == 0:
        match current_instruction[:4]:
            case "noop": pass
            case "addx":
                x += int(current_instruction[5:])
        
        if not (current_instruction := f.readline()[:-1]):
            reached_end = True
        else:
            match current_instruction[:4]:
                case "noop": current_instruction_counter = 1
                case "addx": current_instruction_counter = 2

    if (cycle_counter - 20) % 40 == 0:
        signal_strength = cycle_counter * x
        signal_strength_sum += signal_strength

print(signal_strength_sum)
