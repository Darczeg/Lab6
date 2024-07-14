import sys

def parseargs():
    if len(sys.argv) != 3:
        print("Usage: program.exe pathFile1.x pathFile2.y")
        sys.exit(1)
    return sys.argv[1], sys.argv[2]

if name == "_main":
    input_file, output_file = parse_args()
    print(f"Input file: {input_file}")
    print(f"Output file: {output_file}")
