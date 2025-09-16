class AnonymousSurvey:
    """Collect anonymous answers to a survey question."""

    def __init__(self, question):
        """Store a question, and prepare to store responses."""
        self.question = question
        self.responses = []

    def show_question(self):
        """Show the survey question."""
        print(self.question)

    def store_response(self, response):
        """Store a single response to the survey."""
        self.responses.append(response)
    
    def show_results(self):
      """"""
      print('Survey results:')
      for res in self.responses:
        print(f"- {res}")
        
