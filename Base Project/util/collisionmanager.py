
class CollisionManager:

    def __init__(self):
        self.entities = []

    def move(self, entity, dx, dy):
        pass

    def checkCollisionWithEntites(self, entity):
        pass

    def addEntity(self, entity):
        self.entities.append(entity)

    def removeEntity(self, entity):
        self.entities.remove(entity)
