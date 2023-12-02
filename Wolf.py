class Wolf:
    def __init__(self):
        self.position = (0.0, 0.0)

    def move(self, movement_value, direction):
        if direction == 'Up':
            self.position = (self.position[0], self.position[1] + movement_value)
        elif direction == 'Right':
            self.position = (self.position[0] + movement_value, self.position[1])
        elif direction == 'Down':
            self.position = (self.position[0], self.position[1] - movement_value)
        else:
            self.position = (self.position[0] - movement_value, self.position[1])
