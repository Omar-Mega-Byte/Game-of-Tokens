class ErrorReporter:
    def __init__(self):
        self.errors = []

    def report_error(self, message, line_number=None, position=None):
        """Records a syntax error."""
        error_detail = f"Error: {message}"
        if line_number is not None:
            error_detail += f" at line {line_number}"
        if position is not None:
            error_detail += f", position {position}"
        self.errors.append(error_detail)
        print(error_detail) 

    def get_errors(self):
        """Returns all recorded errors."""
        return self.errors

    def get_error_count(self):
        """Returns the total number of errors."""
        return len(self.errors)

if __name__ == '__main__':
    reporter = ErrorReporter()
    reporter.report_error("Unexpected token ';'")
    reporter.report_error("Missing identifier", line_number=5, position=10)
    
    print("\n--- Error Reporter Test Output ---")
    print(f"Total errors: {reporter.get_error_count()}")
    for err in reporter.get_errors():
        print(err)

