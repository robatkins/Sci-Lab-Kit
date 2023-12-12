import argparse

# Tool to extract texts from binary (non-text) files. Search any binary file, such as an executable, for text strings of printable characters. This tools is similar to the Linux strings command. The tool supports both ASCII and Unicode formats. 

def extract_text_from_binary(file_path, unicode_mode=False):
    try:
        with open(file_path, 'rb') as file:
            binary_data = file.read()

            if unicode_mode:
                text = binary_data.decode('utf-16le', errors='ignore')
            else:
                text = ''.join(chr(byte) if 32 <= byte < 127 or byte in [9, 10, 13] else ' ' for byte in binary_data)

            print(text)

    except FileNotFoundError:
        print(f"Error: File '{file_path}' not found.")
    except Exception as e:
        print(f"Error: {e}")

def main():
    parser = argparse.ArgumentParser(description="Extract text from binary files.")
    parser.add_argument("file_path", help="Path to the binary file")
    parser.add_argument("-u", "--unicode", action="store_true", help="Enable Unicode mode (UTF-16LE)")

    args = parser.parse_args()

    file_path = args.file_path
    unicode_mode = args.unicode

    extract_text_from_binary(file_path, unicode_mode)

if __name__ == "__main__":
    main()
