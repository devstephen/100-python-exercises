with open('urls.txt', "r") as file:
    lines = file.readlines()
    print(lines)

with open("corrected_urls.txt", "w") as file:
    for line in lines:
        line_add_slash = line[:6] + "/" + line[6:]
        file.write(line_add_slash)
        