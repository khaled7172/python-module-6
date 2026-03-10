import alchemy.elements
# """This is direct module import"""
import alchemy
# """This is a package level import"""


def main() -> None:
    print()
    print("=== Sacred Scroll Mastery ===")
    print()
    print("Testing direct module access")
    print("alchemy.elements.create_fire(): ", end="")
    print(alchemy.elements.create_fire())
    print("alchemy.elements.create_water(): ", end="")
    print(alchemy.elements.create_water())
    print("alchemy.elements.create_earth(): ", end="")
    print(alchemy.elements.create_earth())
    print("alchemy.elements.create_air(): ", end="")
    print(alchemy.elements.create_air())
    print()

    print("Testing package-level access (controlled by __init__.py):")
    print("alchemy.create_fire(): ", end="")
    print(alchemy.create_fire())
    print("alchemy.create_water(): ", end="")
    print(alchemy.create_water())
    try:
        print("alchemy.create_earth(): ", end="")
        print(alchemy.create_earth())
    except AttributeError:
        print("AttributeError - not exposed")
    try:
        print("alchemy.create_air(): ", end="")
        print(alchemy.create_air())
    except AttributeError:
        print("AttributeError - not exposed")
    print()
    print("Package metadata:")
    print("Version:", alchemy.__version__)
    print("Author:", alchemy.__author__)


if __name__ == "__main__":
    main()
