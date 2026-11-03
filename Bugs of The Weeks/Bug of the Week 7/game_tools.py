# game_tools.py
def make_label(player, points):
    return f"{player.title()} has {points} points"

def add_bonus(points, bonus=5):
    return points + bonus