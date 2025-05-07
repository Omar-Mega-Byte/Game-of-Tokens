from src.lexer.lexer import Lexer
from src.lexer.file_handler import FileHandler
from src.lexer.formatter import Formatter
from src.parser.parser_main import Parser
import json 
from pathlib import Path
import sys


BASE_DIR = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(BASE_DIR))


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


def run_parser(scanner_output_file_path: Path, parser_results_file_path: Path) -> None:
    """Runs the parser on the output of the scanner."""
    try:
        print(f"\nStarting Parser...")
        print(f"Parser Input: {scanner_output_file_path}")
        
        parser_instance = Parser(str(scanner_output_file_path)) 
        matched_rules, num_errors, ast = parser_instance.parse()
        
        print("Parser finished.")

        parser_results_file_path.parent.mkdir(parents=True, exist_ok=True)
        with parser_results_file_path.open("w", encoding="utf-8") as f:
            f.write("--- Parser Output ---\n")
            f.write("Matched Rules:\n")
            for rule in matched_rules:
                f.write(f"- {rule}\n")
            f.write(f"\nNumber of Syntax Errors: {num_errors}\n")
            if ast:
                f.write("\nAST Representation (simulated):\n")
                f.write(json.dumps(ast, indent=2) + "\n")
        
        print(f"Parser results saved to {parser_results_file_path}")
        print(f"Matched Rules processed by Parser: {len(matched_rules)}")
        print(f"Number of Syntax Errors from Parser: {num_errors}")

    except Exception as e:
        print(f"Parser error: {str(e)}", file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    BASE_DIR = Path(__file__).parent.parent
    INPUT_PATH = BASE_DIR / "data" / "input" / "sample_input.txt"
    OUTPUT_PATH = BASE_DIR / "data" / "output" / "results.txt"
    PARSER_OUTPUT_PATH = BASE_DIR / "data" / "output" / "parser_final_results.txt"

    scan_file(INPUT_PATH, PARSER_OUTPUT_PATH)
    run_parser(OUTPUT_PATH, PARSER_OUTPUT_PATH)