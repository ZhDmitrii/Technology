import itertools
import json


def create_deck():
    """Создаёт колоду карт."""
    suits = ["Пики", "Трефы", "Бубны", "Червы"]
    ranks = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"]

    return [(suit, rank) for suit in suits for rank in ranks]


def save_to_json(combinations, filename):
    """Сохраняет результат в JSON файле."""
    with open(filename, "w", encoding="utf-8") as file:
        json.dump(combinations, file, ensure_ascii=False, indent=4)


def generate_combinations(num_card):
    """Генерирует комбинации и преобразует комбинации в удобочитаемый вид."""
    deck = create_deck()

    combinations = list(itertools.combinations(deck, num_card))

    readable_combinations = []
    for combo in combinations:
        readable_combo = " : ".join(f"{card[0]} {card[1]}" for card in combo)
        readable_combinations.append(readable_combo)

    return readable_combinations


if __name__ == "__main__":

    num_cards = int(input("\nВведите количество карт в комбинации (от 1 до 52): "))
    print("-" * 52)

    if num_cards < 1 or num_cards > 52:
        print("Ошибка: введённое число должно быть от 1 до 52.")
    else:
        combination = generate_combinations(num_cards)

        print(f"Вывод первых комбинаций:")
        for comb in combination[:10]:
            print(comb)
        print("-" * 52)

        save_to_json(combination, "combos.json")

        print(f"Сохранено {len(combination)} комбинаций в файл combos.json.")
        print("-" * 52)
