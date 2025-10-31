[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-22041afd0340ce965d47ae6ef1cefeee28c7c493a6346c4f15d667ab976d596c.svg)](https://classroom.github.com/a/JTXl4WMa)
[![Open in Visual Studio Code](https://classroom.github.com/assets/open-in-vscode-2e0aaae1b6195c2367325f4f02e2d04e9abb55f0b24a779b69b11b9e10269abc.svg)](https://classroom.github.com/online_ide?assignment_repo_id=21178041&assignment_repo_type=AssignmentRepo)
# COMP 163 - Project 1: Character Creator & Chronicles
# 🎯 Project Overview

Build a text-based RPG character creation and story progression system that demonstrates mastery of functions and file I/O operations.

# Required Functions 
Complete these functions in project1_starter.py:

create_character(name, character_class) - Create new character

calculate_stats(character_class, level) - Calculate character stats

save_character(character, filename) - Save character to file

load_character(filename) - Load character from file

display_character(character) - Display character info

level_up(character) - Increase character level

# 🎭 Character Classes
Implement these character classes with unique stat distributions:


Warrior: High strength, low magic, high health

Mage: Low strength, high magic, medium health

Rogue: Medium strength, medium magic, low health

Cleric: Medium strength, high magic, high health

# 📁 Required File Format
Your save_character() function must create files in this exact format:

Character Name: [name]

Class: [class]

Level: [level]

Strength: [strength]

Magic: [magic]

Health: [health]

Gold: [gold]


# Run specific test file
python -m pytest tests/test_character_creation.py -v

# Test your main program
python project1_starter.py

GitHub Testing:

After pushing your code, check the Actions tab to see automated test results:

✅ Green checkmarks = tests passed
❌ Red X's = tests failed (click to see details)

# ⚠️ Important Notes
Protected Files

DO NOT MODIFY files in the tests/ directory

DO NOT MODIFY files in the .github/ directory

Modifying protected files will result in automatic academic integrity violation

# AI Usage Policy

✅ Allowed: AI assistance for implementation, debugging, learning

📝 Required: Document AI usage in code comments

🎯 Must be able to explain: Every line of code during interview

# 📝 Submission Checklist

 All required functions implemented
 
 Code passes all automated tests
 
 README updated with your documentation
 
 Interview scheduled and completed
 
 AI usage documented in code comments

# 🏆 Grading

Implementation (70%): Function correctness, file operations, error handling

Interview (30%): Code explanation and live coding challenge

# COMP 163 - Project 1: Character Creator & Chronicles

**Name:** Charlestone Mayenga  
**Date:** 10/28/2025 
**Course:** COMP 163 - Introduction to Programming

---

## 🎮 Game Concept

**World Setting:**  
This RPG character system is set in the ancient realm of **Aethermoor**, a land once united under a golden age of magic and valor. After the fall of the Crystal Throne, darkness spreads across the kingdoms, and heroes from four legendary orders must rise to restore balance. Warriors defend with steel and honor, Mages channel arcane powers from forgotten tomes, Rogues strike from the shadows with cunning precision, and Clerics heal the wounded with divine light.

**Game Theme:**  
Medieval fantasy with class-based progression and equipment systems. Players create unique characters, save their progress, and watch their heroes grow stronger through leveling up.

---

## ⚔️ Character Classes

### Warrior
- **Role:** Tank/Frontline Fighter
- **Strengths:** Exceptional physical strength, very high health pool
- **Weaknesses:** Limited magical abilities
- **Starting Equipment:** Iron Sword, Wooden Shield
- **Best for:** Players who prefer direct melee combat and high survivability

### Mage
- **Role:** Ranged Magic Damage Dealer
- **Strengths:** Powerful spellcasting, highest magic growth
- **Weaknesses:** Low physical strength, medium health (glass cannon)
- **Starting Equipment:** Wooden Staff, Spell Book
- **Best for:** Players who want devastating magical attacks from a distance

### Rogue
- **Role:** Balanced/Versatile Fighter
- **Strengths:** Well-rounded stats, adaptable playstyle
- **Weaknesses:** Lower health pool compared to other classes
- **Starting Equipment:** Dagger, Lockpicks
- **Best for:** Players who want flexibility in combat and exploration

### Cleric
- **Role:** Support/Healer
- **Strengths:** Strong healing magic, high survivability
- **Weaknesses:** Medium physical combat ability
- **Starting Equipment:** Mace, Holy Symbol
- **Best for:** Players who want to support allies and sustain through battles

---

## 📊 Design Choices

### Stat Formula Design

I designed the stat formulas to create distinct gameplay identities for each class:

#### **Warrior**
```python
strength = 10 + (level * 3)  # Gains +3 strength per level
magic = 3 + (level * 1)      # Minimal magic growth (+1 per level)
health = 100 + (level * 10)  # Massive health gain (+10 per level)
```
**Design Reasoning:** Warriors are the ultimate tanks. They start with solid base strength (10) and gain the most health per level (10 HP), making them incredibly durable on the frontlines. Their magic is intentionally weak to balance their overwhelming physical presence.

#### **Mage**
```python
strength = 5 + (level * 1)   # Minimal strength growth
magic = 15 + (level * 4)     # Massive magic growth (+4 per level)
health = 80 + (level * 5)    # Moderate health gain
```
**Design Reasoning:** Mages are classic glass cannons. They start with the highest base magic (15) and gain the most magic per level (4), making them devastating spellcasters. However, their low strength and moderate health mean they must stay out of melee range to survive.

#### **Rogue**
```python
strength = 8 + (level * 2)   # Balanced strength growth
magic = 8 + (level * 2)      # Balanced magic growth
health = 70 + (level * 6)    # Lower health growth
```
**Design Reasoning:** Rogues are the jack-of-all-trades. Their perfectly balanced stat distribution (both start at 8, both gain +2 per level) makes them versatile. The trade-off is lower health, encouraging strategic hit-and-run tactics rather than sustained combat.

#### **Cleric**
```python
strength = 7 + (level * 2)   # Moderate combat ability
magic = 12 + (level * 3)     # Strong magic for healing/support
health = 90 + (level * 8)    # Very high survivability
```
**Design Reasoning:** Clerics need to stay alive to support their team. They have the second-highest health growth (8 per level) and strong magic (12 base, +3 per level) for healing spells. Their moderate strength allows for some self-defense but keeps them primarily support-focused.

### Starting Gold
All characters begin with **100 gold** to purchase basic supplies and equipment for their journey. This provides a foundation for future item systems.

## 🌟 Bonus Creative Features

### Starting Equipment Based on Class ✨

I implemented a **equipment system** where each character receives unique starting gear matched to their role:

|Character| Equipment                  | Purpose                              |
|---------|----------------------------|--------------------------------------|
| Warrior | Iron Sword, Wooden Shield  | Offense and defense for melee combat |
| Mage    | Wooden Staff, Spell Book   | Magical focus and spell knowledge    |
| Rogue   | Dagger, Lockpicks          | Stealth weapons and utility tools    |
| Cleric  | Mace, Holy Symbol          | Divine implements for healing/combat |

#### Implementation Details:
- Equipment is assigned in `create_character()` based on character class
- Equipment is saved to text files (line 8 of save format)
- Equipment is loaded from text files with **backwards compatibility**
- If loading an old save file without equipment, defaults to "Basic Gear"
- Equipment persists through level ups (doesn't change)
- Invalid/unknown classes receive "Basic Gear"

#### Why This Feature?
This bonus feature adds **immersion and identity** to each character type. When players create a Warrior, they immediately feel like a Warrior with appropriate gear. It also sets the foundation for future equipment upgrade systems.

---

## 🤖 AI Usage Documentation

I used AI assistance (Claude) for the following parts of this project:

### Where AI Helped:

1. **File I/O Operations** (`save_character` and `load_character`)
   - AI explained how to open, write, read, and close files
   - AI helped me understand the difference between `"w"` (write) and `"r"` (read) modes
   - AI showed how to use `os.path.exists()` to check if files exist
   - AI explained `os.path.dirname()` for validating directory paths

2. **Error Handling**
   - AI explained how to check file existence before opening
   - AI helped implement directory validation in `save_character`

3. **Dictionary Operations**
   - AI clarified how to access dictionary values using keys (`character['name']`)
   - AI explained why `level_up()` modifies dictionaries in place (no return needed)

4. **Understanding `calculate_stats` Error**
   - AI helped me debug the `UnboundLocalError` 
   - AI explained I needed an `else` clause for invalid character classes

5. **Testing and Debugging**
   - AI helped me understand pytest output and error messages
   - AI explained what each test was checking for
   - AI showed me how to run specific test files

### What I Understand and Can Explain:

✅ **Every line of my code** - I can walk through each function step by step  
✅ **How dictionaries work** - Key-value pairs and how to access/modify them  
✅ **How file I/O works** - Opening files, reading/writing data, closing files  
✅ **String manipulation** - Using `split()`, `strip()`, and f-strings  
✅ **Conditional logic** - How `if/elif/else` branches work  
✅ **Function design** - Parameters, return values, and how functions call each other  
✅ **Data flow** - How `create_character` calls `calculate_stats`, how `level_up` uses `calculate_stats`  
✅ **The equipment bonus feature** - Why and how it was added without breaking existing code  

---

## 🚀 How to Run

### Prerequisites
- Python 3.7 or higher
- pytest (for running tests)
- Git (for version control)

### Initial Setup

1. **Clone the repository** (if you haven't already):
```bash
   git clone [your-repo-url]
   cd project-1-Charlestonjm21
```

2. **Create a virtual environment**:
```bash
   python -m venv venv
```

3. **Activate the virtual environment**:
```bash
   # Mac/Linux
   source venv/bin/activate
```

4. **Install dependencies**:
```bash
   pip install pytest
```

### Running the Main Program
```bash
python project1_starter.py
```

This will run a comprehensive test suite demonstrating:
- Creating characters of all four classes
- Saving characters with equipment to files
- Loading characters from files
- Leveling up characters
- Verifying equipment persists through saves/loads


### Manual Testing Examples

You can test individual functions in a Python interactive shell:
```python
# Start Python shell
python

# Import your functions
from project1_starter import *

# Create a character
hero = create_character("TestHero", "Warrior")
print(hero)

# Display it
display_character(hero)

# Save it
save_character(hero, "test_hero.txt")

# Load it back
loaded = load_character("test_hero.txt")
display_character(loaded)

# Level up
level_up(hero)
display_character(hero)


### Bonus Features
- [x] **Starting Equipment Based on Character** - Unique gear for each character with persistence

---

## 🎓 Learning Outcomes

Through this project, I learned:

1. **Function Design** - How to break complex problems into smaller, reusable functions
2. **File I/O** - Reading from and writing to text files, handling file errors gracefully
3. **Data Structures** - Using dictionaries to organize related data, tuples for returning multiple values
4. **String Manipulation** - Parsing formatted text, splitting strings, removing whitespace
5. **Conditional Logic** - Using if/elif/else to handle different cases and validate input
6. **Error Handling** - Checking conditions before operations to prevent crashes
7. **Version Control** - Using Git and GitHub for code management and collaboration
8. **Testing** - Understanding automated tests and debugging based on test failures
9. **Documentation** - Writing clear docstrings, comments, and README files
10. **Code Organization** - Structuring a project with logical function ordering

### Challenges Faced:

**Challenge 1: UnboundLocalError in `calculate_stats`**  
*Problem:* Initially forgot the `else` clause, causing errors when invalid classes were passed.  
*Solution:* Added an `else` block with default stats to handle unknown classes gracefully.

**Challenge 2: File Directory Validation**  
*Problem:* `save_character` crashed when given invalid directory paths.  
*Solution:* Used `os.path.dirname()` and `os.path.exists()` to validate directories before opening files.

**Challenge 3: Backwards Compatibility**  
*Problem:* Adding equipment would break loading old save files without the equipment line.  
*Solution:* Checked `len(lines)` before accessing equipment line and provided default value if missing.

---

## 📝 Testing Results

### Local Tests
All pytest tests pass:
```
tests/test_character_creation.py ✅ 7 passed
tests/test_file_operations.py ✅ All passed
tests/test_level_system.py ✅ All passed
tests/test_comprehensive.py ✅ All passed
```

### GitHub Actions
Automated tests run on push and show ✅ green checkmarks in the Actions tab.

---
