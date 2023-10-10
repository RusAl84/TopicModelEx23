

def load_data(filename = "data.txt"):    
    with open(filename, encoding="utf8") as file:
        text = file.read()
    lines = []    
    for line in text.split('\n'):
        line_list = []
        if len(line)>5:
            for word in line.split(' '):
                if len(word)>5:
                    line_list.append(word)
            lines.append(line_list)
    return lines
    
if __name__ == "__main__":
    lines = load_data()
    print(lines)