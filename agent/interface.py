class PortableAgent:
    def __init__(self, name):
        self.name = name

    def run(self, question):
        raise NotImplementedError(
            "Each runtime must implement the run method."
        )