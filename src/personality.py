import random


def turrets_generator():

    def generate_random():
        neuroticism: int = random.randint(0, 100)
        openness: int = random.randint(
            0, 100 - neuroticism)
        conscientiousness: int = random.randint(
            0, 100 - neuroticism - openness)
        extraversion: int = random.randint(
            0, (100 - neuroticism - openness - conscientiousness))
        agreeableness: int = (
            100 - neuroticism - openness - conscientiousness - extraversion)
        turret = {
            "neuroticism": neuroticism,
            "openness": openness,
            "conscientiousness": conscientiousness,
            "extraversion": extraversion,
            "agreeableness": agreeableness
        }
        return turret

    def shoot() -> None:
        print("Shooting")

    def search() -> None:
        print("Searching")

    def talk() -> None:
        print("Talking")

    while True:
        turret = type("Turret", (object,), {
            "personality": generate_random(),
            "shoot": shoot,
            "search": search,
            "talk": talk
        })
        yield turret


if __name__ == "__main__":

    print("\n#---TEST ONE---#")

    turrets = turrets_generator()
    turret = next(turrets)

    for _ in range(2):
        print()

        value_sum: int = 0
        turret.shoot()
        turret.search()
        turret.talk()
        print("\npersonality: \n")

        for trait, value in turret.personality.items():
            print(f"  {trait}: {value}")
            value_sum += value
        print(f"  total = {value_sum}")

    print("\n#---TEST TWO---#")

    for _ in range(2):
        print()

        turret = next(turrets)
        value_sum: int = 0

        turret.shoot()
        turret.search()
        turret.talk()
        print("\npersonality: \n")

        for trait, value in turret.personality.items():
            print(f"  {trait}: {value}")
            value_sum += value
        print(f"  total = {value_sum}")
