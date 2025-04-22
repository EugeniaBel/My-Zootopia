import json

def load_data(file_path):
  """ Loads a JSON file """
  with open(file_path, "r") as handle:
    return json.load(handle)

def main():
  """Main function to process animal data and print information."""
  animals_data = load_data('animals_data.json')

  for animal in animals_data:
    # Check and print the name
    if "name" in animal:
      print(f"Name: {animal['name']}")

    # Check and print the diet
    if "characteristics" in animal and "diet" in animal["characteristics"]:
      print(f"Diet: {animal['characteristics']['diet']}")

    # Check and print the first location
    if "locations" in animal and len(animal["locations"]) > 0:
      print(f"Location: {animal['locations'][0]}")

    # Check and print the type
    if "characteristics" in animal and "type" in animal["characteristics"]:
      print(f"Type: {animal['characteristics']['type']}")

    print() # Add an empty line between each animal's information

if __name__ == "__main__":
  main()
