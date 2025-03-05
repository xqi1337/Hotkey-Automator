import argparse
import keyboard
import signal
import sys

current_line = 0

def read_file_line_by_line(file_path):
    with open(file_path, 'r') as file:
        return file.readlines()

def send_variable(variable):
    keyboard.write(variable)

def read_and_send_part(lines, part_index):
    global current_line
    if current_line < len(lines):
        line = lines[current_line].strip()
        split_content = line.split(':')
        if len(split_content) > part_index:
            send_variable(split_content[part_index])
            if part_index == 1:
                current_line += 1
                print("Switch to next line")

def save_current_line():
    with open('current_line.txt', 'w') as file:
        file.write(str(current_line))

def signal_handler(sig, frame):
    save_current_line()
    sys.exit(0)

def main():
    parser = argparse.ArgumentParser(description='Read and send parts of a file.')
    parser.add_argument('--file_path', type=str, required=True, help='Path to the input file')
    args = parser.parse_args()

    lines = read_file_line_by_line(args.file_path)

    keyboard.add_hotkey('ctrl+1', lambda: read_and_send_part(lines, 0))
    keyboard.add_hotkey('ctrl+2', lambda: read_and_send_part(lines, 1))

    signal.signal(signal.SIGINT, signal_handler)

    while True:
        pass

if __name__ == "__main__":
    main()