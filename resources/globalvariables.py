# Variables used throughout the Chess Application
# TODO: Remove "number_of_tiles" and Declare before dimensions. This Involves finding all occurrences in PyChess Code.
# TODO: Change integer 8 in dimensions to the var number_of_tiles
dimensions = {
    "geometry": "602x697",
    "width": 600+2,
    "height": 695+2,
    "cell_width": 600/8,
    "cell_height": 600/8,
    "cell_translation": 1,
    "hud_piece_size": int(600 / 16),
    "piece_size": int(600/16),
    "piece_translation": int(600/8)*.5,
    "number_of_tiles": 8,
    'coordinates_size': int(600/40),
    'coordinates_translation': int(600/50),
}

TITLE = "PyChess"
VERSION_NUMBER = "0.3.0"
CREDITS = "Created By: Christopher Thomas"
