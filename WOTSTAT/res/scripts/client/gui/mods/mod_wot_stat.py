import BigWorld
import ResMgr
from gui.Scaleform.daapi.view.battle.shared.minimap import Minimap

class EnemyHighlighter:
    def __init__(self):
        self.minimap = None
        self.load_minimap()

    def load_minimap(self):
        self.minimap = BigWorld.player().arena.minimap
        if self.minimap is not None:
            self.highlight_enemies()

    def highlight_enemies(self):
        for vehicle_id, vehicle in BigWorld.entities.items():
            if vehicle.isEnemy:
                self.mark_on_minimap(vehicle)

    def mark_on_minimap(self, vehicle):
        self.minimap.addStaticVehicle(vehicle.position, vehicle.team, vehicle.name)

enemy_highlighter = EnemyHighlighter()
