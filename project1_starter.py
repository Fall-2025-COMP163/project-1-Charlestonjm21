"""
COMP 163 - Project 1: Character Creator & Saving/Loading
Name: Charlestone Mayenga
Date: 10/22/2025

AI Usage: [Document any AI assistance used]
Example: AI helped with file I/O error handling logic in save_character function
"""
from fileinput import filename
import os  # Needed to check if files exist
8
def calculate_stats(character_class, level):
    """
    Calculates base stats based on class and level
    Returns: tuple of (strength, magic, health)
    
    Design your own formulas! Ideas:
    - Warriors: High strength, low magic, high health
    - Mages: Low strength, high magic, medium health  
    - Rogues: Medium strength, medium magic, low health
    - Clerics: Medium strength, high magic, high health
    """
    # TODO: Implement this function
    # Return a tuple: (strength, magic, health)
    # Check which class was chosen
    if character_class == "Warrior":
        # Warriors are strong fighters
        strength = 10 + (level * 3)  # Base 10, gain 3 per level
        magic = 3 + (level * 1)      # Base 3, gain 1 per level (weak at magic)
        health = 100 + (level * 10)  # Base 100, gain 10 per level (very tough)
    
    elif character_class == "Mage":
        # Mages use magic
        strength = 5 + (level * 1)   # Base 5, gain 1 per level (physically weak)
        magic = 15 + (level * 4)     # Base 15, gain 4 per level (strong magic)
        health = 80 + (level * 5)    # Base 80, gain 5 per level (medium health)
    
    elif character_class == "Rogue":
        # Rogues are balanced
        strength = 8 + (level * 2)   # Base 8, gain 2 per level
        magic = 8 + (level * 2)      # Base 8, gain 2 per level
        health = 70 + (level * 6)    # Base 70, gain 6 per level
    
    elif character_class == "Cleric":
        # Clerics are healers with good magic
        strength = 7 + (level * 2)   # Base 7, gain 2 per level
        magic = 12 + (level * 3)     # Base 12, gain 3 per level
        health = 90 + (level * 8)    # Base 90, gain 8 per level
    else:
        # Default stats for unknown/invalid classes
        strength = 10
        magic = 10
        health = 100
    # Return all three stats as a tuple (a group of values)
    return (strength, magic, health)
    pass

def create_character(name, character_class):
    """
    Creates a new character dictionary with calculated stats
    Returns: dictionary with keys: name, class, level, strength, magic, health, gold
    
    Example:
    char = create_character("Aria", "Mage")
    # Should return: {"name": "Aria", "class": "Mage", "level": 1, "strength": 5, "magic": 15, "health": 80, "gold": 100}
    """
    # TODO: Implement this function
    # Remember to use calculate_stats() function for stat calculation
    # All new characters start at level 1
    level = 1
     # Use calculate_stats to get the stats for this class and level
    strength, magic, health = calculate_stats(character_class, level)
    
    # Create a dictionary to store all character info
    character = {
        "name": name,              # The name we were given
        "class": character_class,  # The class we were given
        "level": level,            # Always 1 for new characters
        "strength": strength,      # From calculate_stats
        "magic": magic,            # From calculate_stats
        "health": health,          # From calculate_stats
        "gold": 100                # Everyone starts with 100 gold
    }
    
    # Send back the complete character
    return character
    pass

def save_character(character, filename):
    """
    Saves character to text file in specific format
    Returns: True if successful, False if error occurred
    
    Required file format:
    Character Name: [name]
    Class: [class]
    Level: [level]
    Strength: [strength]
    Magic: [magic]
    Health: [health]
    Gold: [gold]
    """
    # TODO: Implement this function
    # Remember to handle file errors gracefully
     # Get the directory path from the filename
    directory = os.path.dirname(filename)
    
    # If there's a directory path, check if it exists
    if directory and not os.path.exists(directory):
        return False
    
    # Try to open and write the file
    file = open(filename, "w")
    file.write(f"Character Name: {character['name']}\n")
    file.write(f"Class: {character['class']}\n")
    file.write(f"Level: {character['level']}\n")
    file.write(f"Strength: {character['strength']}\n")
    file.write(f"Magic: {character['magic']}\n")
    file.write(f"Health: {character['health']}\n")
    file.write(f"Gold: {character['gold']}\n")
    file.close()
    return True
    pass

def load_character(filename):
    """
    Loads character from text file
    Returns: character dictionary if successful, None if file not found
    """
    # TODO: Implement this function
    # Remember to handle file not found errors
    if not os.path.exists(filename):
        return None
    
    file = open(filename, "r")
    lines = file.readlines()
    file.close()
        
        # Create empty dictionary to store character data
    character = {}
        
        # Process each line
        # lines[0] = "Character Name: Aria\n"
        # We need to extract "Aria"
        
        # Line 0: Character Name: Aria
    character["name"] = lines[0].split(": ")[1].strip()
        
        # Line 1: Class: Mage
    character["class"] = lines[1].split(": ")[1].strip()
        
        # Line 2: Level: 1
    character["level"] = int(lines[2].split(": ")[1].strip())
        
        # Line 3: Strength: 6
    character["strength"] = int(lines[3].split(": ")[1].strip())
        
        # Line 4: Magic: 19
    character["magic"] = int(lines[4].split(": ")[1].strip())
        
        # Line 5: Health: 85
    character["health"] = int(lines[5].split(": ")[1].strip())
        
        # Line 6: Gold: 100
    character["gold"] = int(lines[6].split(": ")[1].strip())
        
    return character
        
    pass

def display_character(character):
    """
    Prints formatted character sheet
    Returns: None (prints to console)
    
    Example output:
    === CHARACTER SHEET ===
    Name: Aria
    Class: Mage
    Level: 1
    Strength: 5
    Magic: 15
    Health: 80
    Gold: 100
    """
    # TODO: Implement this function
    # Print the header
    print("=== CHARACTER SHEET ===")
    
    # Print each piece of character info
    # character["name"] gets the value stored under the "name" key
    print(f"Name: {character['name']}")
    print(f"Class: {character['class']}")
    print(f"Level: {character['level']}")
    print(f"Strength: {character['strength']}")
    print(f"Magic: {character['magic']}")
    print(f"Health: {character['health']}")
    print(f"Gold: {character['gold']}")
    pass

def level_up(character):
    """
    Increases character level and recalculates stats
    Modifies the character dictionary directly
    Returns: None
    """
    # TODO: Implement this function
    # Remember to recalculate stats for the new level

    # Increase the level by 1
    character["level"] = character["level"] + 1
    # Or shorthand: character["level"] += 1
    
    # Get the new stats for this level
    # Remember: calculate_stats returns (strength, magic, health)
    new_strength, new_magic, new_health = calculate_stats(
        character["class"], 
        character["level"]
    )
    
    # Update the character's stats
    character["strength"] = new_strength
    character["magic"] = new_magic
    character["health"] = new_health
    
    # Note: We don't change name, class, or gold
    # Note: We don't return anything - we modified the dictionary directly

    pass

# Main program area (optional - for testing your functions)
if __name__ == "__main__":
    print("=== CHARACTER CREATOR ===")
    print("Test your functions here!")
    
      # Test 1: Create a character
    print("--- TEST 1: Create Character ---")
    hero = create_character("Aria", "Mage")
    display_character(hero)
    
    # Test 2: Save character
    print("\n--- TEST 2: Save Character ---")
    success = save_character(hero, "aria.txt")
    if success:
        print("✓ Character saved successfully!")
    else:
        print("✗ Failed to save character")
    
    # Test 3: Load character
    print("\n--- TEST 3: Load Character ---")
    loaded = load_character("aria.txt")
    if loaded:
        print("✓ Character loaded successfully!")
        display_character(loaded)
    else:
        print("✗ Failed to load character")
    
    # Test 4: Level up
    print("\n--- TEST 4: Level Up ---")
    print("Before level up:")
    display_character(hero)
    
    level_up(hero)
    
    print("\nAfter level up:")
    display_character(hero)
    
    print("\n=== ALL TESTS COMPLETE ===")
    
    # Example usage:
    # char = create_character("TestHero", "Warrior")
    # display_character(char)
    # save_character(char, "my_character.txt")
    # loaded = load_character("my_character.txt")
    
    # Create a new character
    hero = create_character("Gandalf", "Mage")
    print("Starting character:")
    display_character(hero)
    
    # Level up once
    print("\n--- Leveling up to 2 ---")
    level_up(hero)
    display_character(hero)
    
    # Level up again
    print("\n--- Leveling up to 3 ---")
    level_up(hero)
    display_character(hero)
    
    # Level up multiple times
    print("\n--- Leveling up to 10 ---")
    for i in range(7):  # Level up 7 more times (3 → 10)
        level_up(hero)
    display_character(hero)
    
    # Save the leveled character
    save_character(hero, "gandalf_level10.txt")
    print("\nSaved level 10 character to file!")
