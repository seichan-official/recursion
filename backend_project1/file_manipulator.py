import sys

def reverse_file(inputpath,outputpath):
    with open(inputpath,'r' , encoding='UTF-8') as infile:
        content = infile.read
    with open(outputpath,'w',encoding="UTF-8") as outfile:
        outfile.write(content[::-1])
        
def copy_file(inputpath,outputpath):
    with open(inputpath,'r' ,encoding='UTF-8') as infile:
        content = infile.read
    with open(outputpath,'w', encoding='UTF-8') as outfile:
        outfile.write(content)
        
def duplicate_contents(inputpath, n):
    with open(inputpath, 'r', encoding='utf-8') as file:
        content = file.read()
    with open(inputpath, 'w', encoding='utf-8') as file:
        file.write(content * n)

def replace_string(inputpath, needle, newstring):
    with open(inputpath, 'r', encoding='utf-8') as file:
        content = file.read()
    content = content.replace(needle, newstring)
    with open(inputpath, 'w', encoding='utf-8') as file:
        file.write(content)
        
def main():
    if len(sys.argv) < 3:
        print("Usage: <command> <inputpath> [additional arguments]")
        return

    command = sys.argv[1]
    inputpath = sys.argv[2]

    if command == "reverse":
        if len(sys.argv) != 4:
            print("Usage: reverse <inputpath> <outputpath>")
            return
        outputpath = sys.argv[3]
        reverse_file(inputpath, outputpath)
    elif command == "copy":
        if len(sys.argv) != 4:
            print("Usage: copy <inputpath> <outputpath>")
            return
        outputpath = sys.argv[3]
        copy_file(inputpath, outputpath)
    elif command == "duplicate-contents":
        if len(sys.argv) != 4:
            print("Usage: duplicate-contents <inputpath> <n>")
            return
        n = int(sys.argv[3])
        duplicate_contents(inputpath, n)
    elif command == "replace-string":
        if len(sys.argv) != 5:
            print("Usage: replace-string <inputpath> <needle> <newstring>")
            return
        needle = sys.argv[3]
        newstring = sys.argv[4]
        replace_string(inputpath, needle, newstring)
    else:
        print("Unknown command")

if __name__ == "__main__":
    main()
