import json


def load_data(file_path):
  """ Loads a JSON file """
  with open(file_path, "r") as handle:
    return json.load(handle)


def read_html():
    """ Reads HTML file """
    with open('animals_template.html', "r", encoding='utf-8') as handle:
        return handle.read()


def write_html(string):
    """ Writes HTML file """
    with open('animals.html', "w", encoding='utf-8') as handle:
        handle.write(string)


def serialize_animal(animal):
    """ Generate one list card from animal data """
    output = '\t\t\t<li class="cards__item">\n'
    output += f'\t\t\t\t<div class ="card__title">{animal["name"]}</div>\n'
    output += '\t\t\t\t<p class="card__text">\n'
    output += f'\t\t\t\t\t<strong>Diet</strong>: {animal["characteristics"]["diet"]}</br>\n'
    output += f'\t\t\t\t\t<strong>Location</strong>: {animal["locations"][0]}</br>\n'
    if 'type' in animal["characteristics"]:
        output += f'\t\t\t\t\t<strong>Type</strong>: {animal["characteristics"]["type"]}</br>\n'
    output += '\t\t\t\t</p>\n'
    output += '\t\t\t</li>'

    return output


def generate_output(animals_data):
    """ Generates a string from data"""
    output = ''
    for animal in animals_data:
        output += serialize_animal(animal)

    return output


def main():
    animals_data = load_data('animals_data.json')
    output = generate_output(animals_data)
    html = read_html()
    html = html.replace('            __REPLACE_ANIMALS_INFO__', output)
    write_html(html)


if __name__ == '__main__':
    main()