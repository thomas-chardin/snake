#  Fonction permetant de lire un json
# fonction permettant d'écrire la date heure et score dans le json
import json
import time

def add_score_to_json(score):
    scores = open_json()
    
    current_time = time.strftime('%Y-%m-%d %H:%M:%S')
    scores.append({"timestamp": current_time, "score": score})

    with open('scores.json', 'w') as file:
        json.dump(scores, file)

def open_json():
    try:
        with open('scores.json', 'r') as file:
            scores = json.load(file)
    except FileNotFoundError:
        scores = []
    return scores
