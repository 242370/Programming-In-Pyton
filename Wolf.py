class Wolf:
    def __init__(self):
        self.position = (0.0, 0.0)

    def move(self, movement_value, direction):
        self.position = (self.position[0] + movement_value * direction[0],
                         self.position[1] + movement_value * direction[1])
