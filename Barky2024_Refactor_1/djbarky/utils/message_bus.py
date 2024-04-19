# message_bus.py

class MessageBus:
    def __init__(self):
        self.handlers = {}

    def register_handler(self, command_name, handler):
        if command_name not in self.handlers:
            self.handlers[command_name] = []
        self.handlers[command_name].append(handler)

    def dispatch_command(self, command_name, *args, **kwargs):
        if command_name in self.handlers:
            for handler in self.handlers[command_name]:
                handler(*args, **kwargs)

# Create a global instance of the message bus
message_bus = MessageBus()
