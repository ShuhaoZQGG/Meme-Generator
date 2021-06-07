class QuoteModel:
    def __init__(self,body = 'This is a quote body', author='Author'):
        self.body = body
        self.author = author

    def __str__(self):
        f"{self.body}--{self.author}"
    
    def __repr__(self):
        """Repr returns the sting when object is called."""
        if self.body.startswith("\"") and self.body.endswith("\""):
            return f'{self.body} - {self.author}'
        else:
            return f'"{self.body}" - {self.author}'