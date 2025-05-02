import os

class FileHandler:
    def __init__(self):
        self.current_file = None
        self.included_files = []

    def process_file(self, filename, lexer):
        if not os.path.exists(filename):
            return [], [f"Error: File {filename} not found"]
        with open(filename, 'r') as f:
            source = f.read()
        tokens, errors = lexer.tokenize(source)
        include_tokens = [t for t in tokens if t.type_ == 'Inclusion']
        for token in include_tokens:
            if token.text == 'Using':
                idx = tokens.index(token)
                if idx + 2 < len(tokens) and tokens[idx + 1].text == '(' and tokens[idx + 2].type_ == 'IDENTIFIER':
                    include_file = tokens[idx + 2].text
                    if include_file not in self.included_files:
                        self.included_files.append(include_file)
                        inc_tokens, inc_errors = self.process_file(include_file, lexer)
                        tokens.extend(inc_tokens)
                        errors.extend(inc_errors)
        return tokens, errors