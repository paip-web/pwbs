from pwbs.api.plugin import Plugin

class ExamplePlugin(Plugin):
    """Plugin Base Class"""
    def __init__(self):
        self.test = 21
    def init(self):
        """
        Plugin Initialization Method
        """
        self.test = 22
        print('Example Plugin Initialized')
