
class Camera:
    def __init__(self, location, width, height):
        """
        This class checks if an object is within the screen
        and determines relative coordinates for drawing.

        Parameters
        ----------
        location
        width
        height
        """
        self.location = location
        self.x = location[0]
        self.y = location[1]
        self.width = width
        self.height = height
        self.player = None

    def check_contains(self, obj):
        """
        Checks if object is on screen.

        Parameters
        ----------
        obj: sprite object

        Returns
        -------
        bool: determines if on screen

        """
        if (obj.x + obj.rect.width/2 <= self.x - self.width/2
                or obj.x - obj.rect.width/2 >= self.x + self.width/2):
            return False
        elif (obj.y + obj.rect.height/2 <= self.y - self.height/2
              or obj.y - obj.rect.height/2 >= self.y + self.height/2):
            return False
        else:
            obj.rect.center = (obj.x + self.width/2 - self.x , self.y - obj.y + self.height/2)
            return True

    def update(self):
        """
        Moves with player.

        """
        self.x, self.y = self.player.x, self.player.y
        self.location = [self.x, self.y]
