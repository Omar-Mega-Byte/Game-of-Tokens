import re
from src.keywords import get_keyword_map


class Token:
    def __init__(self, line, text, type_):
        self.line = line
        self.text = text
        self.type_ = type_

    def __str__(self):
        return f"Line : {self.line} Token Text: {self.text} Token Type: {self.type_}"


class Lexer:
    def __init__(self):
        self.keywords = get_keyword_map()
        self.tokens = []
        self.errors = []
        self.line_number = 0
        self.token_patterns = self._build_token_patterns()

    def _build_token_patterns(self):
        return [
            (r'/\#[\s\S]*?\#/', None),
            (r'/-.*', None),

            (
                r'\b(' + '|'.join(re.escape(kw) for kw in self.keywords.keys()) + r')\b',
                'KEYWORD'
            ),

            (r'"[^"]*"', 'Quotation Mark'),
            (r"'[^']'", 'Quotation Mark'),
            (r'\d+', 'Constant'),
            (r'\b(true|false)\b', 'Boolean'),

            (r'&&|\|\|', 'Logic operators'),
            (r'[+\-*/]', 'Arithmetic Operation'),
            (r'==|!=|<=|>=|<|>', 'Logic operators relational'),
            (r'=', 'Assignment operation'),
            (r'\.', 'Access Operator'),

            (r';', 'Statement_Terminator'),
            (r',', 'Comma'),
            (r'[{}()[\]]', 'Braces'),

            (r'\b[a-zA-Z_][a-zA-Z0-9_]*\b', 'Identifier'),

            (r'\s+', None)
        ]

    def tokenize(self, source_code):
        self.tokens = []
        self.errors = []
        self.line_number = 0

        source_code = self._strip_multiline_comments(source_code)

        for line in source_code.split('\n'):
            self.line_number += 1
            self._tokenize_line(line.strip())

        return self.tokens, self.errors

    def _strip_multiline_comments(self, source_code):
        pattern = re.compile(r'/\#[\s\S]*?\#/')  # ملهوش لازمة
        return pattern.sub('', source_code)

    def _tokenize_line(self, line):
        pos = 0
        while pos < len(line):
            match = None
            for pattern, token_type in self.token_patterns:
                regex = re.compile(pattern)  # ملهوش لازمة
                match = regex.match(line, pos)
                if match:
                    text = match.group(0)
                    if token_type:
                        if token_type == 'KEYWORD':
                            actual_type = self.keywords.get(text, 'Identifier')
                        else:
                            actual_type = token_type
                        self.tokens.append(Token(self.line_number, text, actual_type))
                    pos = match.end()
                    break

            if not match:
                if line[pos] not in ' \t':
                    self.errors.append(
                        f"Line {self.line_number}: Error - Invalid token '{line[pos]}'"
                    )
                pos += 1
