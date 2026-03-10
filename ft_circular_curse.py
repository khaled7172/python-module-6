from alchemy import grimoire


def main() -> None:
    print("=== Circular Curse Breaking ===")
    print()
    print("Testing ingredient validation:")
    ingredients = "fire air"
    ingredients_2 = "dragon scales"
    print('validate_ingredients("fire air"): ',
          grimoire.validate_ingredients(ingredients))
    print('validate_ingredients("dragon scales"): ',
          grimoire.validate_ingredients(ingredients_2))
    print()
    print("Testing spell recording with validation:")
    spell_name = "Fireball"
    invalid_spell = "Dark Magic"
    ingredients_3 = "shadow"
    print('record_spell("Fireball", "fire air"): ',
          grimoire.record_spell(spell_name, ingredients))
    print(
        'record_spell("Dark Magic", "shadow"): ',
        grimoire.record_spell(
            invalid_spell,
            ingredients_3))
    print()
    print("Testing late import technique")
    light_spell = "Lightning"
    ingredients_light = "air"
    print(
        'record_spell("Lightning", "air"): ',
        grimoire.spellbook.record_spell(
            light_spell,
            ingredients_light))
    print()
    print("Circular dependency curse avoided using late imports!")
    print("All spells processed safely!")


if __name__ == "__main__":
    main()
