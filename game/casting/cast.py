from game.casting.actor import Actor
from game.casting.falling_object import Falling_object
from game.shared.point import Point
import random
class Cast:
    """A collection of actors.

    The responsibility of a cast is to keep track of a collection of actors. It has methods for 
    adding, removing and getting them by a group name.

    Attributes:
        _actors (dict): A dictionary of actors { key: group_name, value: a list of actors }
    """

    def __init__(self):
        """Constructs a new Actor."""
        self._actors = {}
        
    def add_actor(self, group, actor):
        """Adds an actor to the given group.
        
        Args:
            group (string): The name of the group.
            actor (Actor): The actor to add.
        """
        if not group in self._actors.keys():
            self._actors[group] = []
            
        if not actor in self._actors[group]:
            self._actors[group].append(actor)

    def get_actors(self, group):
        """Gets the actors in the given group.
        
        Args:
            group (string): The name of the group.

        Returns:
            List: The actors in the group.
        """
        results = []
        if group in self._actors.keys():
            results = self._actors[group].copy()
        return results
    
    def get_all_actors(self):
        """Gets all of the actors in the cast.
        
        Returns:
            List: All of the actors in the cast.
        """
        results = []
        for group in self._actors:
            results.extend(self._actors[group])
        return results

    def get_first_actor(self, group):
        """Gets the first actor in the given group.
        
        Args:
            group (string): The name of the group.
            
        Returns:
            List: The first actor in the group.
        """
        result = None
        if group in self._actors.keys():
            result = self._actors[group][0]
        return result

    def remove_actor(self, group, actor):
        """Removes an actor from the given group.
        
        Args:
            group (string): The name of the group.
            actor (Actor): The actor to remove.
        """
        if group in self._actors:
            self._actors[group].remove(actor)

    def spawn(self, type, velocity, max_x):
        """Spawns a rock or gem somewhere along the top of the screen to start moving down 
        Args:
            type (String): either gem or rock
            max_x (int): the heighest x accepted by the screen
        """
        location = random.randint(0,60)*15
        
        if type == 'rock':
            new_actor = Falling_object(-10)
            new_actor.set_text('o')
            new_actor.set_color(0)
            
        
        if type == 'gem':
            new_actor = Falling_object(1)
            new_actor.set_text('*')
            new_actor.set_color(1)

        new_actor.set_velocity(velocity)
        new_actor.set_position(Point(location,600))
        self.add_actor('falling_objects',new_actor)
        
    
    