class QuoteModel:
    def __init__(self,body = 'This is a quote body', author='Author'):
        self.body = body
        self.author = author

    def __str__(self):
        f"{self.boy}--{self.author}"
    
    def __repr__(self):
        f"QuoteModel(quote={self.body!r}--author={self.author!r})"
