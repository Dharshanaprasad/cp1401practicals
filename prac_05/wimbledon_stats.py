FILENAME = "wimbledon.csv"

def main():
    champions = process_wimbledon_file(FILENAME)
    display_champion_stats(champions)
    display_countries(champions)

def process_wimbledon_file(filename):
    champions = {}
    with open(filename, "r", encoding="utf-8-sig") as file:
        file.readline()  # Skip the header
        for line in file:
            parts = line.strip().split(',')
            champion = parts[2]
            country = parts[1]
            champions[champion] = champions.get(champion, 0) + 1
    return champions

def display_champion_stats(champions):
    print("Wimbledon Champions:")
    for champion, wins in champions.items():
        print(f"{champion} {wins}")

def display_countries(champions):
    countries = sorted(set(champions))
    print("\nThese countries have won Wimbledon:")
    print(", ".join(countries))

if __name__ == "__main__":
    main()
