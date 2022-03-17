from game.shared.point import Point

class Director:
    """A person who directs the game. 
    
    The responsibility of a Director is to control the sequence of play.

    Attributes:
        _keyboard_service (KeyboardService): For getting directional input.
        _video_service (VideoService): For providing video output.
    """

    def __init__(self, keyboard_service, video_service):
        """Constructs a new Director using the specified keyboard and video services.
        
        Args:
            keyboard_service (KeyboardService): An instance of KeyboardService.
            video_service (VideoService): An instance of VideoService.
        """
        self._keyboard_service = keyboard_service
        self._video_service = video_service
        
    def start_game(self, cast):
        """Starts the game using the given cast. Runs the main game loop.

        Args:
            cast (Cast): The cast of actors.
        """
        self._score = 0
        self._ticks = 0
        self._difficulty = 12
        self._video_service.open_window()
        while self._video_service.is_window_open():
            self._get_inputs(cast)
            self._do_updates(cast)
            self._do_outputs(cast)
        self._video_service.close_window()
        

    def _get_inputs(self, cast):
        """Gets directional input from the keyboard and applies it to the prospector.
        
        Args:
            cast (Cast): The cast of actors.
        """
        prospector = cast.get_first_actor("prospectors")
        velocity = self._keyboard_service.get_direction()
        prospector.set_velocity(velocity)        

    def _do_updates(self, cast):
        """Updates the prospector's position, spawns new objects and resolves any collisions with falling objects.
        
        Args:
            cast (Cast): The cast of actors.
        """
        self._ticks += 1
        if self._score <= 0:
            self._score=0
        banner = cast.get_first_actor("banners")
        prospector = cast.get_first_actor("prospectors")
        falling_objects = cast.get_actors("falling_objects")

        banner.set_text(f"Score: {self._score}")
        max_x = self._video_service.get_width()
        max_y = self._video_service.get_height()
        prospector.move_next(max_x, max_y)
        self._difficulty = 150 * (1/(self._score+11))
        
        if self._ticks % int(self._difficulty) == 0:

            cast.spawn('rock',Point(0,5),max_x)
            cast.spawn('gem',Point(0,5),max_x)

        for falling_object in falling_objects:
            falling_object.move_next(max_x, max_y)

            position = falling_object.get_position()
            if prospector.get_position().equals(position):
                self._score += falling_object.points
                cast.remove_actor('falling_objects',falling_object)
            if position.get_y() <= 0:
                cast.remove_actor('falling_objects',falling_object)
                

        
    def _do_outputs(self, cast):
        """Draws the actors on the screen.
        
        Args:
            cast (Cast): The cast of actors.
        """
        self._video_service.clear_buffer()
        actors = cast.get_all_actors()
        self._video_service.draw_actors(actors)
        self._video_service.flush_buffer()

    