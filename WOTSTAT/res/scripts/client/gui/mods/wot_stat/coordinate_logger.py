import BigWorld
import Math
import time
import ResMgr
import os

class CoordinatesLogger:
    def __init__(self):
        self.log_file = os.path.join(ResMgr.userPrefsDirectory(), "coordinates_log.txt")
        self.last_log_time = time.time()
        self.log_interval = 1  # Логировать каждые 1 сек

    def log_coordinates(self):
        current_time = time.time()
        if current_time - self.last_log_time >= self.log_interval:
            self.last_log_time = current_time
            visible_entities = self.get_visible_entities()
            with open(self.log_file, 'a') as f:
                for entity in visible_entities:
                    position = entity.position
                    f.write(f"{entity.name}: {position.x}, {position.y}, {position.z}\n")

    def get_visible_entities(self):
        visible_entities = []
        for entity in BigWorld.entities.values():
            if hasattr(entity, 'isAlive') and entity.isAlive() and hasattr(entity, 'position'):
                visible_entities.append(entity)
        return visible_entities

logger = CoordinatesLogger()

def tick():
    logger.log_coordinates()
    BigWorld.callback(1, tick)

tick()
