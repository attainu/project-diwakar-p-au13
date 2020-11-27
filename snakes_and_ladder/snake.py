class Snake:
    def __init__(self, start=None, end=None):
        self.start = start
        self.end = end
        self.message = f"Encountered SNAKE. Going back to {self.end}"

    def get_start(self):
        return self.start

    def get_end(self):
        return self.end

    def set_start(self, start):
        self.start = start

    def set_end(self, end):
        self.end = end
