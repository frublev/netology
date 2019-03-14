def adv_print(str, start="\n", max_line = False, in_file = False):
    print(start, end="")
    if len(str) > max_line > 0:
        line = []
        while len(str) > max_line:
            line.append(str[:max_line])
            print(str[:max_line])
            str = str[max_line:]
        line.append(str)
        print(str)
        str = "\n".join(line)
    else:
        print(str)
    if in_file != False:
        with open(in_file, "w", encoding="utf-8") as file_for_write:
            file_for_write.write(start+str)


if __name__ == "__main__":
    str = "OneTwoThreeFourFiveS"
    adv_print(str, max_line = 3, in_file = "text1.txt")
