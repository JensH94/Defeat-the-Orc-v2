forest = {
    "room_1": {
        "description": "A dense forest, light shines through the treetops",
        "exit": {
            "back": "exit_environment",
            "left": "room_2",
            "middle": "room_3",
            "right": "room_4",
        },
    },
    "room_2": {
        "description": "A small clearing with an abandoned campfire",
        "exit": {"back": "room_1", "middle": "room_5"},
    },
    "room_5": {
        "description": "At the foot of the clearing is an abandoned and broken tent",
        "exit": {"back": "room_2"},
    },
    "room_3": {
        "description": "Clear, rippling water flows through the river that opens up before you",
        "exit": {"back": "room_1", "left": "room_6", "right": "room_7"},
    },
    "room_6": {
        "description": "The terrain slopes down and in front of you is an old riverbed",
        "exit": {"back": "room_3"},
    },
    "room_7": {
        "description": "Upstream you'll find an abandoned hut with an old cooking area in front of the door",
        "exit": {"back": "room_3"},
    },
    "room_4": {
        "description": "The clearing closes abruptly. The light becomes dimmer",
        "exit": {
            "back": "room_1",
            "right": "room_8",
            "middle": "room_9",
        },
    },
    "room_8": {
        "description": "A small opening in the thicket brings you to a small field",
        "exit": {"back": "room_4"},
    },
    "room_9": {
        "description": "A small opening in the thicket leads you to the foot of a rocky cliff",
        "exit": {"back": "room_4"},
    },
}
