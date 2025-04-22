import json

def load_data(file_path):
  """Loads a JSON file."""
  with open(file_path, "r") as handle:
    return json.load(handle)

def main():
  """Main function to process animal data, generate HTML, and write to a file."""
  animals_data = load_data('animals_data.json')

  # 1. Read the content of the template
  with open('animals_template.html', 'r') as template_file:
    html_template = template_file.read()

  # 2. Generate a string with the animals' data
  animals_info_string = ''
  for animal in animals_data:
    if "name" in animal:
      animals_info_string += f"Name: {animal['name']}"
    if "characteristics" in animal and "diet" in animal["characteristics"]:
      animals_info_string += f"Diet: {animal['characteristics']['diet']}"
    if "locations" in animal and len(animal["locations"]) > 0:
      animals_info_string += f"Location: {animal['locations'][0]}"
    if "characteristics" in animal and "type" in animal["characteristics"]:
      animals_info_string += f"Type: {animal['characteristics']['type']}"
    animals_info_string += '\n'  # Add a newline after each animal's info

  # 3. Replace __REPLACE_ANIMALS_INFO__ with the generated string
  final_html = html_template.replace('__REPLACE_ANIMALS_INFO__', animals_info_string)

  # 4. Write the new HTML content to a new file, animals.html
  with open('animals.html', 'w') as output_file:
    output_file.write(final_html)

  print("Generated animals.html")

if __name__ == "__main__":
  main()
