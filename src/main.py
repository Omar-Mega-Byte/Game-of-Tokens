from src.lexer.lexer import Lexer
from src.lexer.file_handler import FileHandler
from src.lexer.formatter import Formatter
from pathlib import Path
import sys


def scan_file(input_file_path: Path, output_file_path: Path) -> None:
    try:
        lexer = Lexer()
        file_handler = FileHandler()

        tokens, errors = file_handler.process_file(input_file_path, lexer)

        scanner_output = Formatter.format_scanner_output(tokens, errors)

        output_file_path.parent.mkdir(parents=True, exist_ok=True)

        with output_file_path.open('w', encoding='utf-8') as f:
            f.write(scanner_output)

        print(f"\nScanner completed successfully")
        print(f"Input:  {input_file_path}")
        print(f"Output: {output_file_path}")
        print(f"\n{len(tokens)} tokens found")
        print(f"{len(errors)} errors detected\n")

        print("Sample output:")
        print('\n'.join(scanner_output.split('\n')[:10]))
        if len(scanner_output.split('\n')) > 10:
            print("... (truncated)")

    except FileNotFoundError:
        print(f"Error: Input file not found at {input_file_path}", file=sys.stderr)
        sys.exit(1)
    except Exception as e:
        print(f"Scanner error: {str(e)}", file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    BASE_DIR = Path(__file__).parent.parent
    INPUT_PATH = BASE_DIR / "data" / "input" / "sample_input.txt"
    OUTPUT_PATH = BASE_DIR / "data" / "output" / "results.txt"

    scan_file(INPUT_PATH, OUTPUT_PATH)
