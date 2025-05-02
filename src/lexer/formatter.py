class Formatter:
    @staticmethod
    def format_scanner_output(tokens, errors):
        output = []

        for token in tokens:
            output.append(
                f"Line {token.line}: Token Text: {token.text:<15} Token Type: {token.type_}"
            )

        if errors:
            output.append("\nLexical Errors:")
            output.extend(errors)

        output.append(f"\nTotal number of errors: {len(errors)}")

        return '\n'.join(output)

    @staticmethod
    def write_to_file(output, filepath):
        with open(filepath, 'w') as f:
            f.write(output)