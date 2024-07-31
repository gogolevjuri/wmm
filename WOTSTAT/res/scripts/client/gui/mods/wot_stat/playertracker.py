import BigWorld
import datetime
class PlayerTracker:
    def __init__(self):
        self.log_file = open('player_log.txt', 'a')
        self.write_header()

    def write_header(self):
        self.log_file.write("Time, Position, Map, Vehicle\n")

    def log_player_data(self):
        player = BigWorld.player()
        if player and player.isAlive():
            time_now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            position = player.position
            map_name = player.arena.arenaType.geometryName
            vehicle = player.vehicleTypeDescriptor.name
            log_entry = f"{time_now}, {position}, {map_name}, {vehicle}\n"
            self.log_file.write(log_entry)

    def close_log_file(self):
        self.log_file.close()
