"""
The command pattern encapsulates requests as objects, allowing you to parameterize clients
with requests, queue or log requests, and support undoable operations. This is achieved by
creating a command class with an execute method that performs the action.
"""

class Light:
    def turn_on(self):
        return "Light is ON"

    def turn_off(self):
        return "Light is OFF"

class LightOnCommand:
    def __init__(self, light):
        self.light = light

    def execute(self):
        return self.light.turn_on()

class LightOffCommand:
    def __init__(self, light):
        self.light = light

    def execute(self):
        return self.light.turn_off()


light = Light()
on_command = LightOnCommand(light)
off_command = LightOffCommand(light)
print(on_command.execute()) # Outputs: Light is ON
print(off_command.execute()) # Outputs: Light is OFF