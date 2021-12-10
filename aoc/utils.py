def read(puzzel):
    with open(puzzel) as file:
        lines = file.readlines()
        lines = [line.rstrip() for line in lines]
    return lines
