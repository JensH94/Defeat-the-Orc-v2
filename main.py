from database import get_data, disconnect, verbinden
from loader import build_classes, build_enemies

connection = verbinden()

classes_data = get_data(connection, "classes")
enemies_data = get_data(connection, "enemies")

disconnect(connection)

character_classes = build_classes(classes_data)
enemies = build_enemies(enemies_data)

print(character_classes)
print(enemies)
