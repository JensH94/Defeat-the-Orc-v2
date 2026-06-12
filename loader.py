from classes import Entity


def build_classes(classes_data):
    character_classes = []
    for zeile in classes_data:
        character_classes.append(Entity(zeile))
    return character_classes


def build_enemies(enemies_data):
    enemies = []
    for zeile in enemies_data:
        enemies.append(Entity(zeile))
    return enemies
