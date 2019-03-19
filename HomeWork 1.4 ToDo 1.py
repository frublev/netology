def adv_print(*args, start="Пустая строка \n", max_line=False, in_file=False, separator=' '):
    print(start, end="")
    output_line = []
    last_str = 0
    if separator == '\n':
        end_print = separator
        end_line = ''
    else:
        end_print = ''
        end_line = separator
    for arg in args:
        output_text = str(arg) + end_line
        line = []
        if last_str > 0 and separator != '\n':
            print(output_text[:last_str])
            line.append(output_text[:last_str])
            output_text = output_text[last_str:]
        while len(output_text) > max_line:
            line.append(output_text[:max_line])
            print(output_text[:max_line])
            output_text = output_text[max_line:]
        last_str = max_line - len(output_text)
        if last_str == 0:
            print(output_text, end='\n')
            line.append(output_text + '\n')
            output_text = "\n".join(line)
        else:
            print(output_text, end=end_print)
            line.append(output_text)
            output_text = "\n".join(line) + end_print
        output_line.append(output_text)
    if in_file:
        with open(in_file, "w", encoding="utf-8") as file_for_write:
            file_for_write.write(start+''.join(output_line))


if __name__ == "__main__":
    strk = "OneTwoThreeFourFiveSix"
    adv_print(strk, 12345, 'test', 54321, 'test123', max_line=5, in_file="text2.txt", separator='\n')
