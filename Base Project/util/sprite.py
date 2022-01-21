from util.imageloader import *

class Sprite:

    def __init__(self, path_to_image, x, y, width=0, height=0):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        if path_to_image != None:
            self.image = ImageLoader().loadImage(path_to_image)

        if width == 0:
            self.width = self.image.get_width()
        if height == 0:
            self.height = self.image.get_height()

        self.half_width = int(float(self.width) / 2.0)
        self.half_height = int(float(self.height) / 2.0)

        self.collision_manager = None

    def update(self, keys_pressed):
        pass

    def draw(self, window):
        window.blit(self.image, (self.x, self.y, self.width, self.height))

    def move(self, dx, dy):
        if self.collision_manager is None:
            self.x += dx
            self.y += dy
        else:
            self.collision_manager.move(self, dx, dy)

    def moveTo(self, x, y):
        if self.collision_manager is None:
            self.x = x
            self.y = y
        else:
            self.collision_manager.moveTo(self, x, y)

    def changeSize(self, width, height):
        self.width = width
        self.height = height
        self.half_width = int(float(self.width) / 2.0)
        self.half_height = int(float(self.height) / 2.0)

    def collidesWithPoint(self, point):
        px, py = point
        if px <= self.x + self.width and px >= self.x:
            if py <= self.y + self.height and py >= self.y:
                return True
        return False

    def collidesWithRect(self, rect):
        rx, ry, rwidth, rheight = rect
        if self.x < rx + rwidth and self.x + self.width > rx:
            if self.y < ry + rheight and self.y + self.height > ry:
                return True
        return False

    def addCollisionManager(self, collision_manager):
        self.collision_manager = collision_manager

    def removeCollisionManager(self):
        self.collision_manager = None

    def getPosition(self):
        return (self.x, self.y, self.width, self.height)

    def getTopLeft(self):
        return (self.x, self.y)

    def getTopRight(self):
        return (self.x + self.width, self.y)

    def getBottomLeft(self):
        return (self.x, self.y + self.height)

    def getBottomRight(self):
        return (self.x + self.width, self.y + self.height)

    def getTopMiddle(self):
        return (self.x + self.half_width, self.y)

    def getRightMiddle(self):
        return (self.x + self.width, self.y + self.half_height)

    def getLeftMiddle(self):
        return (self.x, self.y + self.half_height)

    def getBottomMiddle(self):
        return (self.x + self.half_width, self.y + self.height)