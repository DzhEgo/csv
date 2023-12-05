import json

def load_json(file_path):
    with open(file_path, 'r') as json_file:
        return json.load(json_file)

def save_json(data, file_path):
    with open(file_path, 'w') as json_file:
        json.dump(data, json_file, indent=4)

superhero_squad = load_json('files/SuperHero.json')

new_members = [
    {"name": "Captain America", "age": 100, "secretIdentity": "Steve Rogers", "powers": ["Superhuman strength", "Shield throwing"]},
    {"name": "Spider-Man", "age": 23, "secretIdentity": "Peter Parker", "powers": ["Wall-crawling", "Web-slinging", "Spidey sense"]}
]

superhero_squad['members'].extend(new_members)
superhero_squad['members'].sort(key=lambda x: len(x['powers']), reverse=True)

save_json(superhero_squad, 'files/superhero_squad_updated.json')

second_squad = {
    "squadName": "Fantastic Four",
    "homeTown": "New York City",
    "formed": 1961,
    "secretBase": "Baxter Building",
    "active": True,
    "members": [
        {"name": "Mr. Fantastic", "age": 40, "secretIdentity": "Reed Richards", "powers": ["Elasticity", "Genius-level intellect"]},
        {"name": "Invisible Woman", "age": 35, "secretIdentity": "Sue Storm", "powers": ["Invisibility", "Force field generation"]},
        {"name": "Human Torch", "age": 28, "secretIdentity": "Johnny Storm", "powers": ["Pyrokinesis", "Flight"]},
        {"name": "The Thing", "age": 45, "secretIdentity": "Ben Grimm", "powers": ["Superhuman strength", "Rock-like skin"]}
    ]
}

save_json(second_squad, 'files/fantastic_four.json')

superhero_squad = load_json('files/superhero_squad_updated.json')
fantastic_four = load_json('files/fantastic_four.json')

def calculate_stats(team):
    members = team["members"]
    total_age = sum(member["age"] for member in members)
    total_powers = sum(len(member["powers"]) for member in members)
    return total_age / len(members), total_powers

superhero_squad_avg_age, superhero_squad_total_powers = calculate_stats(superhero_squad)
fantastic_four_avg_age, fantastic_four_total_powers = calculate_stats(fantastic_four)

print("Super Hero Squad:")
print("Средний возраст:", superhero_squad_avg_age)
print("Общее количество способностей:", superhero_squad_total_powers)
print("\nFantastic Four:")
print("Средний возраст:", fantastic_four_avg_age)
print("Общее количество способностей:", fantastic_four_total_powers)