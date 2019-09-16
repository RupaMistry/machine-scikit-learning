class ModelException(Exception):
    def initStart(self, message, *args):
        Exception.initStart(self, *args)
        self.message = message

    def get_message(self):
        return self.message
