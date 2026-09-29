import json


def load_data(file_path):
  """ Loads a JSON file """
  with open(file_path, "r") as handle:
    return json.load(handle)


def read_html():
    with open('animals_template.html', "r") as handle:
        return handle.read()


def write_html(string):
    with open('animals_template.html', "w") as handle:
        handle.write(string)


def generate_output(animals_data):
    """ Generates a string from data"""
    output = ''
    for animal in animals_data:
        for key in ['Name', 'Diet', 'Location', 'Type']:
            match key:
                case "Name":
                    output += f"{key}: {animal['name']}\n"
                case "Diet":
                    output += f"{key}: {animal['characteristics']['diet']}\n"
                case "Location":
                    output += f"{key}: {animal['locations'][0]}\n"
                case "Type":
                    if 'type' in animal['characteristics']:
                        output += f"{key}: {animal['characteristics']['type']}\n"
        output += f"\n"

    return output


def main():
    animals_data = load_data('animals_data.json')
    output = generate_output(animals_data)

    html = read_html()
    html = html.replace('__REPLACE_ANIMALS_INFO__', output)

    write_html(html)


if __name__ == '__main__':
    main()