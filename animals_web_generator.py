import json

def load_data(file_path):
  """Loads a JSON file."""
  with open(file_path, "r") as handle:
    return json.load(handle)

def main():
  """Main function to process animal data, generate well-formatted HTML list items,
  and write to the HTML file.
  """
  animals_data = load_data('animals_data.json')

  # 1. Read the content of the template
  with open('animals_template.html', 'r') as template_file:
    html_template = template_file.read()

  # 2. Generate well-formatted HTML string for each animal
  animals_list_items = ''
  for animal in animals_data:
    animal_item = '<li class="cards__item">\n'
    if "name" in animal:
      animal_item += f'  <div class="card__title">{animal["name"]}</div>\n'
      animal_item += '  <p class="card__text">\n'
      if "characteristics" in animal:
        if "diet" in animal["characteristics"]:
          animal_item += f'    <strong>Diet:</strong> {animal["characteristics"]["diet"]}<br/>\n'
        if "locations" in animal and len(animal["locations"]) > 0:
          animal_item += f'    <strong>Location:</strong> {animal["locations"][0]}<br/>\n'
        if "type" in animal["characteristics"]:
          animal_item += f'    <strong>Type:</strong> {animal["characteristics"]["type"]}<br/>\n'
      animal_item += '  </p>\n'
    animal_item += '</li>\n'
    animals_list_items += animal_item

  # 3. Replace __REPLACE_ANIMALS_INFO__ with the generated list items
  final_html = html_template.replace('__REPLACE_ANIMALS_INFO__', animals_list_items)

  # 4. Write the new HTML content to animals.html
  with open('animals.html', 'w') as output_file:
    output_file.write(final_html)

  print("Generated animals.html with improved formatting.")

if __name__ == "__main__":
  main()
