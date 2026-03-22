*This project has been created as part of the 42 curriculum by khhammou*

## Description
For this project the final folder structure should look like this:
repo_root
│
├── ft_sacred_scroll.py
├── ft_import_transmutation.py
├── ft_pathway_debate.py
├── ft_circular_curse.py
│
└── alchemy
    ├── __init__.py
    ├── elements.py
    ├── potions.py
    │
    ├── transmutation
    │   ├── __init__.py
    │   ├── basic.py
    │   └── advanced.py
    │
    └── grimoire
        ├── __init__.py
        ├── spellbook.py
        └── validator.py

elements.py contains 4 functions
create_fire()
create_water()
create_earth()
create_air()
each should return a string
example:
def create_fire()
    return "Fire element created"

alchemy/init.py
This file controls what the package exposes
you must include:
__version__ = "1.0.0"
__author__ = "Master pythonicus"
from .elements import create_fire, create_water
notes:
create_earth and create_air should not be imported here
so:
alchemy.create_fire() works
alchemy.create_earth() doesn't work
but the entire concept is:
alchemy.elements.create_earth() works

ft_sacred_scroll.py
you demonstrate two things
Direct module access

import alchemy.elements

-> alchemy.elements.create_fire()

package level access:

import alchemy

alchemy.create_fire()

then intentionally try:
alchemy.create_earth() and catch the error as an AttributeError: print("AttributeError - not exposed")

part II is demonstrating different ways to import
create alchemy/potions.py
add these functions in it:
healing_potion()
strength_potion()
invisibility_potion()
wisdom_potion()
each function imports needed elements
calls them
builds the string
Example concept:
from .elements import create_fire, create_water

def healing_potion():
    fire = create_fire()
    water = create_water()
    return f"Healing potion brewed with {fire} and {water}"

ft_import_transmutation.py
show 4 import styles:

1_ Full module
import alchemy.elements
alchemy.elements.create_fire()

2_ Specific import

from alchemy.elements import create_water
create_water()

3_ Alias import
from alchemy.potions import healing_potion as heal
heal()

4_ Multiple imports
from alchemy.elements import create_earth, create_fire

part III Absolut vs Relative imports

Absolute import:
Full path from root
Example in basic.py
from alchemy.elements import create_fire

Relative import:
Using dots
Example in advanced.py:
from .basic import lead_to_gold
from ..potions import healing_potion

. means current folder
.. means parent folder

transmutation/init.py
Expose functions:
from .basic import lead_to_gold, stone_to_gem
from .advanced import philosophers_stone, elixir_of_life
so user can call:
alchemy.transmutation.lead_to_gold()

ft_pathway_debate.py:
demonstrate:
from alchemy.transmutation.basic import lead_to_gold
from alchemy.transmutation.advanced import philosophers_stone
then
import alchemy.transmutation
alchemy.transmutation.lead_to_gold()

part IV Circular Imports
Circular dependency
Example of bad code:
spellbook imports validator
validator imports spellbook
python loads modules once, so this causes import loops
The solution is late import:
Example in spellbook.py:
def record_spell(spell_name, ingredients):

    from .validator import validate_ingredients

    result = validate_ingredients(ingredients)

    if "VALID" in result:
        return f"Spell recorded: {spell_name} ({result})"
    else:
        return f"Spell rejected: {spell_name} ({result})"

Because the import happens when function runs, not when module loads.
This breaks the circular dependency.
validator.py
def validate_ingredients(ingredients: str) -> str:
Check if string contains:
fire
water
earth
air
if yes:
VALID
else:
INVALID

ft_circular_curse.py
demonstrate:
validate_ingredients("fire air")
validate_ingredients("dragon scales")
then:
record_spell("Fireball", "fire air")
record_spell("Dark Magic", "shadow")

knowledge to know:
__init__.py turns a directory into a python package and controls what symbols the pacakage exposes

Difference between import module and from module import function
when you use import modules you do module.function()
when you use from module import function you can directly call the function function()

Absolute vs Relative imports:
Absolute from alchemy.elements import create_fire
Relative from .elements import create_fire

what causes circular imports?
Two modules importing each other during initialization.
How to fix?
Common methods:
late import
dependency injection
shared module
You implement late import.
FIXING FLAKE8 Errors:
noqa = "no quality assurance" — it's a comment that tells flake8 "ignore this line".
F401 is the specific error code for "imported but unused".
So # noqa: F401 means "ignore the unused import warning on this line specifically". You could write just # noqa to silence all warnings on a line, but being specific with F401 is better practice — you're only suppressing the one warning you actually intend to ignore.

### Instructions

You run this code by doing python3 file_name.py

## Resources

The internet

## AI Usage

Testing my code with test cases and helping me find syntax errors