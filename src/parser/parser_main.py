class Parser:
    def __init__(self, input_file_path):
        self.input_file_path = input_file_path
        self.tokens = []
        self.matched_rules = []
        self.num_errors = 0
        self.ast = None 

    def _read_input_file(self):
        """Reads tokens from the specified input file."""
        try:
            with open(self.input_file_path, "r", encoding="utf-8") as f:
                self.tokens = [line.strip() for line in f if line.strip()] 
            if not self.tokens:
                print(f"Warning: Input file {self.input_file_path} is empty or contains no processable lines.")
        except FileNotFoundError:
            print(f"Error: Input file {self.input_file_path} not found.")
            self.tokens = [] 
            self.num_errors += 1

    def _validate_grammar_rules(self):
        """Simulates grammar rule validation."""
        if not self.tokens:
            return

        for i in range(0, len(self.tokens), 2):
            if i + 1 < len(self.tokens):
                rule = f"Rule: {self.tokens[i]} -> {self.tokens[i+1]}"
                self.matched_rules.append(rule)
                if (i // 2) % 5 == 0 and i > 0:
                    self.num_errors += 1
                    print(f"Syntax Error (simulated) near: {self.tokens[i]}")
            else:
                self.num_errors += 1
                print(f"Syntax Error (simulated): Unmatched token {self.tokens[i]}")
        
        if not self.matched_rules and self.tokens:
            self.num_errors +=1 
            print("Syntax Error (simulated): No rules could be matched from the input tokens.")


    def _build_parse_tree(self):
        """Simulates AST/Parse Tree generation."""
        if self.matched_rules and self.num_errors == 0:
            self.ast = {"type": "Program", "body": self.matched_rules}
        else:
            self.ast = None

    def _report_syntax_errors(self):
        """Simulates reporting syntax errors."""
        if self.num_errors > 0:
            print(f"Total syntax errors found: {self.num_errors}")
        else:
            print("No syntax errors found.")

    def parse(self):
        """Main parsing method."""
        self._read_input_file()
        if not self.tokens and self.input_file_path != "data/output/results.txt":
            return self.matched_rules, self.num_errors, self.ast
            
        self._validate_grammar_rules()
        self._build_parse_tree() 
        self._report_syntax_errors() 

        return self.matched_rules, self.num_errors, self.ast

if __name__ == '__main__':
    parser = Parser("../../data/output/results.txt") 
    matched_rules, num_errors, ast = parser.parse()
    
    print("\n--- Parser Test Output ---")
    print("Matched Rules:")
    for r in matched_rules:
        print(f"- {r}")
    print(f"\nNumber of Syntax Errors: {num_errors}")
    if ast:
        print("\nAST (simulated):")
        import json
        print(json.dumps(ast, indent=2))

