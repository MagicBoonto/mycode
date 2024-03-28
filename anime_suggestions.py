def suggest_anime(genre):
    anime_database = {
        "action": ["Attack on Titan", "My Hero Academia", "One Punch Man", "Naruto", "Dragon Ball Z", "Bleach", "Demon Slayer", "Black Clover", "Hunter x Hunter", "Tokyo Ghoul", "Mob Psycho 100", "Fairy Tail", "JoJo's Bizarre Adventure"],
        "comedy": ["Konosuba", "Nichijou", "Gintama", "One Piece", "The Disastrous Life of Saiki K", "Daily Lives of High School Boys", "Grand Blue", "Kaguya-sama: Love is War", "Miss Kobayashi's Dragon Maid", "Osomatsu-san", "Haven't You Heard? I'm Sakamoto", "Ouran High School Host Club"],
        "fantasy": ["Fullmetal Alchemist: Brotherhood", "Sword Art Online", "Re:Zero", "Overlord", "The Rising of the Shield Hero", "Log Horizon", "No Game No Life", "Magi: The Labyrinth of Magic", "Fate/Zero", "Made in Abyss", "The Seven Deadly Sins", "That Time I Got Reincarnated as a Slime"],
        "slice of life": ["Your Lie in April", "Toradora!", "Clannad", "Anohana: The Flower We Saw That Day", "March Comes in Like a Lion", "K-On!", "Barakamon", "Silver Spoon", "Natsume's Book of Friends", "A Place Further than the Universe", "Sakurasou no Pet na Kanojo", "Shirobako"],
        "isekai": ["Sword Art Online", "Re:Zero", "Overlord", "No Game No Life", "That Time I Got Reincarnated as a Slime", "Log Horizon", "The Rising of the Shield Hero", "Konosuba", "In Another World with My Smartphone", "The Saga of Tanya the Evil"]
        }

    if genre.lower() in anime_database:
        return anime_database[genre.lower()]
    else:
        return None

def main():
    print("ようこそ!")
    while True:
        try:
            user_genre = input("? (action, comedy, fantasy, slice of life, isekai): ")
            recommended_anime = suggest_anime(user_genre)
            if recommended_anime:
                print("My suggestions are:")
                for anime in recommended_anime:
                    print("-", anime)
            else:
                print("Sorry, we havent got any suggestions for that yet...")
        except KeyboardInterrupt:
            print("\Sayonara!")
            break
        except Exception as e:
            print("Error:", e)
            continue

if __name__ == "__main__":
    main()

