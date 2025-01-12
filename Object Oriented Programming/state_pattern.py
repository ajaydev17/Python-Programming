"""
The state pattern allows an object to change its behavior when its internal state changes,
appearing as if it changed its class. This is implemented by defining separate classes for each
state, each with its behavior.
"""

class State:
    def handle(self):
        pass


class StartState(State):
    def handle(self):
        return "Starting..."


class StopState(State):
    def handle(self):
        return "Stopping..."


class Context:
    def __init__(self, state):
        self.state = state

    def request(self):
        return self.state.handle()
    
start = StartState()
stop = StopState()
context = Context(start)
print(context.request()) # Outputs: Starting...
context.state = stop
print(context.request()) # Outputs: Stopping...