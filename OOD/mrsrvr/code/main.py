from mission import Mission
if __name__ == "__main__":
    # read from input.txt
    try:
        with open("input.txt", "r", encoding="utf-8") as f: # with automatically closes file after
            content = f.read()
    except FileNotFoundError:
        print("File input.txt not found")
        exit(1)

    scenarios = content.strip().split("\n\n")
    mission = Mission()
    for scen in scenarios:
        mission.parse(scen)

