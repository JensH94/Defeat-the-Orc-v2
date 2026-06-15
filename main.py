from database import disconnect, verbinden
from loader import load_all

connection = verbinden()

every_data = load_all(connection)

disconnect(connection)

print(every_data)
