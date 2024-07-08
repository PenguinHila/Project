from utils import SCORES_FILE_NAME
import os


def add_score(game_difficulty):
    if not os.path.exists(SCORES_FILE_NAME):
        with open(SCORES_FILE_NAME, 'w') as file:
            file.write('0')
    else:
        with open(SCORES_FILE_NAME, 'r') as file:
            content = file.read().strip()

        with open(SCORES_FILE_NAME, 'w') as file:
            score = (game_difficulty * 3) + 5 + int(content)
            file.write(str(score))

