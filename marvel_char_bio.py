marvelchars = {
    "Starlord": {
        "real name": "Peter Quill",
        "powers": "Dance moves",
        "archenemy": "Thanos"
    },

    "Mystique": {
        "real name": "Raven Darkholme",
        "powers": "Shape shifter",
        "archenemy": "Professor X"
    },

    "Hulk": {
        "real name": "Bruce Banner",
        "powers": "Super strength",
        "archenemy": "Adrenaline"
    },

    "Iron Man": {
        "real name": "Tony Stark",
        "powers": "Powered armor suit",
        "archenemy": "Mandarin"
    },

    "Spider-Man": {
        "real name": "Peter Parker",
        "powers": "Wall-crawling, super strength, spider sense",
        "archenemy": "Green Goblin"
    },

    "Thor": {
        "real name": "Thor Odinson",
        "powers": "Godly strength, lightning manipulation",
        "archenemy": "Loki"
    },

    "Captain America": {
        "real name": "Steve Rogers",
        "powers": "Peak human strength and agility, Vibranium shield",
        "archenemy": "Red Skull"
    },

    "Black Widow": {
        "real name": "Natasha Romanoff",
        "powers": "Master martial artist, espionage expert",
        "archenemy": "Taskmaster"
    },

    "Doctor Strange": {
        "real name": "Stephen Strange",
        "powers": "Mystic arts, time manipulation",
        "archenemy": "Dormammu"
    },

    "Black Panther": {
        "real name": "T'Challa",
        "powers": "Enhanced strength, agility, Vibranium suit",
        "archenemy": "Killmonger"
    },

    # Additional Characters
    "Wolverine": {
        "real name": "Logan",
        "powers": "Regeneration, retractable claws",
        "archenemy": "Sabretooth"
    },

    "Deadpool": {
        "real name": "Wade Wilson",
        "powers": "Regeneration, expert marksman, breaking the fourth wall",
        "archenemy": "Ajax"
    },

    "Storm": {
        "real name": "Ororo Munroe",
        "powers": "Weather manipulation",
        "archenemy": "Shadow King"
    },

    "Magneto": {
        "real name": "Erik Lehnsherr",
        "powers": "Magnetism manipulation",
        "archenemy": "Xavier"
    },

    "Hawkeye": {
        "real name": "Clint Barton",
        "powers": "Expert archer, marksman",
        "archenemy": "Bullseye"
    },

    "Groot": {
        "real name": "Groot",
        "powers": "Tree-like appearance, regeneration",
        "archenemy": "Ronan the Accuser"
    },

    "Rocket Raccoon": {
        "real name": "Rocket Raccoon",
        "powers": "Expert marksman, engineering skills",
        "archenemy": "The Collector"
    },

    "Black Bolt": {
        "real name": "Blackagar Boltagon",
        "powers": "Vocal power, flight",
        "archenemy": "Maximus the Mad"
    },

    "Scarlet Witch": {
        "real name": "Wanda Maximoff",
        "powers": "Reality manipulation, chaos magic",
        "archenemy": "Chthon"
    },

    "Vision": {
        "real name": "Vision",
        "powers": "Density manipulation, energy blasts",
        "archenemy": "Ultron"
    }
}

char_name = input('Which character do you want to know about? (Starlord, Mystique, Hulk, Iron Man, Spider-Man, Thor, Captain America, Black Widow, Doctor Strange, Black Panther, Wolverine, Deadpool, Storm, Magneto, Hawkeye, Groot, Rocket Raccoon, Black Bolt, Scarlet Witch, Vision) ')
char_stat = input('What statistic do you want to know about? (real name, powers, archenemy) ')

value = marvelchars.get(char_name.title(), {}).get(char_stat.lower(), "Invalid input or information not available.")

print(f"{char_name}'s {char_stat} is: {value}")

