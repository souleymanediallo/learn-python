class Agent:
    """Docstring décrivant le concept de agent."""
    def __init__(self, position, **properties):
        self.position = position
        self.neuroticism = properties["neuroticism"]
        self.language = properties["language"]


