import json

def load_data(file_path):
  """ Loads a JSON file """
  with open(file_path, "r") as handle:
    return json.load(handle)

animals_data = load_data('animals_data.json')

print(animals_data)




for animal in animals_data:
    for key in ['Name', 'Diet', 'Location', 'Type']:

        match key:
            case "Name":
                print(f"{key}: ", end="")
                print(f"{animal['name']}")
            case "Diet":
                print(f"{key}: ", end="")
                print(f"{animal['characteristics']['diet']}")
            case "Location":
                print(f"{key}: ", end="")
                print(f"{animal['locations'][0]}")
            case "Type":
                if 'type' in animal['characteristics']:
                    print(f"{key}: ", end="")
                    print(f"{animal['characteristics']['type']}")
    print()