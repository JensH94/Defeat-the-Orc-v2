forest = {
    "room_1": {
        "name": "Forest Edge",
        "description": "A dense forest, light shines through the treetops",
        "details": "The forest entrance spans an uneven, stony surface dotted with flowers and surrounded by grass.You see a path to the left, a small, worn trail to the right, and the forest opening up before you.",
        "exit": {
            "back": "exit_environment",
            "left": "room_2",
            "middle": "room_3",
            "right": "room_4",
        },
    },
    "room_2": {
        "name": "Abandoned Campfire",
        "description": "A small clearing with an abandoned campfire",
        "details": "A small abandoned campfire right next to a big tree. An open space around the tree and campfire that seemed small at first but is in fact quite big.",
        "exit": {"back": "room_1", "middle": "room_5"},
    },
    "room_5": {
        "name": "Broken Tent",
        "description": "At the foot of the clearing is an abandoned and broken tent",
        "details": "Looks like the tent has seen better days. The tent is surrounded by earth and mud.",
        "exit": {"back": "room_2"},
    },
    "room_3": {
        "name": "Riverside",
        "description": "Clear, rippling water flows through the river that opens up before you",
        "details": "A small trail leads to the river, you can clearly see tracks of many animals.",
        "exit": {"back": "room_1", "left": "room_6", "right": "room_7"},
    },
    "room_6": {
        "name": "Riverbed",
        "description": "The terrain slopes down and in front of you is an old riverbed",
        "details": "Befor you is an old dried-up riverbed. You can see a lot of rocks and mud in there.",
        "exit": {"back": "room_3"},
    },
    "room_7": {
        "name": "Abandoned Hut",
        "description": "Upstream you'll find an abandoned hut with an old cooking area in front of the door",
        "details": "The cooking area does not look to bad you could probably light it and coock something up. The old hut has a busted front door and looks really worn down , it has been ages since someone was living here.",
        "exit": {"back": "room_3"},
    },
    "room_4": {
        "name": "Thicket",
        "description": "The clearing closes abruptly. The light becomes dimmer",
        "details": "Trees and bushes are overgrown and it is hard to move here.",
        "exit": {
            "back": "room_1",
            "right": "room_8",
            "middle": "room_9",
        },
    },
    "room_8": {
        "name": "Field",
        "description": "A small opening in the thicket brings you to a small field",
        "details": "A run down small field with a lot of animal trackes. Pretty sure if you plant something here it will get eaten.",
        "exit": {"back": "room_4"},
    },
    "room_9": {
        "name": "Cliff",
        "description": "A small opening in the thicket leads you to the foot of a rocky cliff",
        "details": "You are at the bottom and befor you is a big rocky cliff. You see no end to the cliff on either side",
        "exit": {"back": "room_4"},
    },
}
