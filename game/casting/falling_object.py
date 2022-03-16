from game.casting.actor import Actor

class Falling_object(Actor):
    """Stores a point value that it will add when a player collides with it"""
    def __init__(self,point_value):
        super().__init__()
        self.points = point_value