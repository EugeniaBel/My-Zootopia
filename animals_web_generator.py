import json

def load_data(file_path):
  """Loads a JSON file. """
  with open(file_path, "r") as handle:
    return json.load(handle)

def serialize_animal(animal_obj):
  """Serializes a single animal object into an HTML list item."""
  animal_item = '<li class="cards__item">\n'
  if "name" in animal_obj:
    animal_item += f'  <div class="card__title">{animal_obj["name"]}</div>\n'
    animal_item += '  <p class="card__text">\n'
    if "characteristics" in animal_obj:
      if "diet" in animal_obj["characteristics"]:
        animal_item += f'    <strong>Diet:</strong> {animal_obj["characteristics"]["diet"]}<br/>\n'
      if "locations" in animal_obj and len(animal_obj["locations"]) > 0:
        animal_item += f'    <strong>Location:</strong> {animal_obj["locations"][0]}<br/>\n'
      if "type" in animal_obj["characteristics"]:
        animal_item += f'    <strong>Type:</strong> {animal_obj["characteristics"]["type"]}<br/>\n'
    animal_item += '  </p>\n'
  animal_item += '</li>\n'
  return animal_item

def main():
  """Main function to process animal data, serialize each animal,
  and write the HTML to a file.
  """
  animals_data = load_data('animals_data.json')

  # 1. Read the content of the template
  with open('animals_template.html', 'r') as template_file:
    html_template = template_file.read()

  # 2. Serialize each animal object
  animals_list_items = ''
  for animal in animals_data:
    animals_list_items += serialize_animal(animal)

  # 3. Replace __REPLACE_ANIMALS_INFO__ with the generated list items
  final_html = html_template.replace('__REPLACE_ANIMALS_INFO__', animals_list_items)

  # 4. Write the new HTML content to animals.html
  with open('animals.html', 'w') as output_file:
    output_file.write(final_html)

  print("Generated animals.html with organized code.")

if __name__ == "__main__":
  main()