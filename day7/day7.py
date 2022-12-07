from pathlib import Path
dirs = {}
currentSize = 0
with open('input.txt') as f:
    # p = Path('/')
    line = f.readline() # ignote first line casue its just a cd /
    line = f.readline()
    while line:
        if line.startswith('$ cd'):
            # p = p / line[4:].strip()
            line = f.readline()

        elif line.startswith('$ ls'):
            line = f.readline()
            while line:
                if line.startswith('$'):
                    break
                else:
                    if line.startswith('dir'):
                        dirs[line[4:]]
                    else:
                        currentSize += int(line.split(' ')[0])
                
                line = f.readline()

        
