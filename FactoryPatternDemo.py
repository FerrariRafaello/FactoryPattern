from abc import ABC, abstractmethod
from flask import Flask, request, jsonify, Response
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# ===== Simple Factory Pattern =====

class FactoryError(Exception):
    pass

class Animal(ABC):
    @abstractmethod
    def speak(self):
        pass

class Dog(Animal):
    def speak(self):
        return "woof"
    
class Cat(Animal):
    def speak(self):
        return "meow"

class AnimalFactory:
    @staticmethod
    def create(animal_type: str):
        animals = {
            "dog": Dog,
            "cat": Cat
        }
        cls = animals.get(animal_type.lower())
        if cls:
            return cls()
        else:
            raise FactoryError(f"Unknown animal type: {animal_type}")

# ===== Factory Method Pattern =====

class Section(ABC):
    @abstractmethod
    def description(self):
        pass

class PersonalSection(Section):
    def description(self):
        return "Personal Section"
    
class AlbumSection(Section):
    def description(self):
        return "Photo Album Section"

class PatentSection(Section):
    def description(self):
        return "Patent Section"

class PublicationSection(Section):
    def description(self):
        return "Publication Section"

class Profile(ABC):
    def __init__(self):
        self.sections = []
        self.create_profile()
    
    @abstractmethod
    def create_profile(self):
        pass

    def get_sections(self):
        return [section.description() for section in self.sections]

    def add_section(self, section: Section):
        self.sections.append(section)
    
class FacebookProfile(Profile):
    def create_profile(self):
        self.add_section(PersonalSection())
        self.add_section(PatentSection())
        self.add_section(PublicationSection())

class TwitterProfile(Profile):
    def create_profile(self):
        self.add_section(AlbumSection())
        self.add_section(PersonalSection())
    
class ProfileFactory:
    @staticmethod
    def create(profile_type: str):
        profiles = {
            "facebook": FacebookProfile,
            "twitter": TwitterProfile
        }

        cls = profiles.get(profile_type.lower())
        if cls:
            return cls()
        else:
            raise FactoryError(f"Unknown profile type: {profile_type}")
        
# ===== Flask REST API =====

app = Flask(__name__)

HTML_PAGE = """
<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8" />
<meta name="viewport" content="width=device-width, initial-scale=1" />
<title>Factory Pattern Demo</title>
<style>
  body { font-family: Arial, sans-serif; max-width: 600px; margin: 30px auto; padding: 0 15px; }
  input, button, select { width: 100%; padding: 8px; margin: 6px 0 12px; box-sizing: border-box; }
  button { cursor: pointer; }
  pre { background: #f5f5f5; padding: 12px; border-radius: 5px; white-space: pre-wrap; }
</style>
</head>
<body>

<h1>Factory Pattern Demo</h1>

<section>
  <h2>Simple Factory - Create Animal</h2>
  <select id="animalType">
    <option value="">-- Select an animal --</option>
    <option value="dog">Dog</option>
    <option value="cat">Cat</option>
  </select>
  <button onclick="createAnimal()">Create Animal</button>
</section>

<section>
  <h2>Factory Method - Create Profile</h2>
  <select id="profileType">
    <option value="">-- Select a profile --</option>
    <option value="facebook">Facebook</option>
    <option value="twitter">Twitter</option>
  </select>
  <button onclick="createProfile()">Create Profile</button>
</section>

<h2>Result</h2>
<pre id="result">No actions performed yet.</pre>

<script>
  const apiBase = '';

  async function createAnimal() {
    const type = document.getElementById('animalType').value;
    if (!type) {
      alert('Please select an animal type.');
      return;
    }
    const response = await fetch(apiBase + '/animal', {
      method: 'POST',
      headers: {'Content-Type': 'application/json'},
      body: JSON.stringify({type})
    });
    const data = await response.json();
    document.getElementById('result').textContent = JSON.stringify(data, null, 2);
  }

  async function createProfile() {
    const type = document.getElementById('profileType').value;
    if (!type) {
      alert('Please select a profile type.');
      return;
    }
    const response = await fetch(apiBase + '/profile', {
      method: 'POST',
      headers: {'Content-Type': 'application/json'},
      body: JSON.stringify({type})
    });
    const data = await response.json();
    document.getElementById('result').textContent = JSON.stringify(data, null, 2);
  }
</script>

</body>
</html>
"""
@app.route('/')
def index():
    return Response(HTML_PAGE, mimetype="text/html")

@app.route("/animal", methods=["POST"])
def animal_route():
    data = request.get_json(force=True)
    animal_type = data.get("type")
    try:
        animal = AnimalFactory.create(animal_type)
        return jsonify({"type": animal_type, "sound": animal.speak()})
    except ValueError as e:
        logger.error(e)
        return jsonify({"errr": str(e)}), 400
    
@app.route("/profile", methods = ["POST"])
def profile_route():
    data = request.get_json(force=True)
    profile_type = data.get("type")
    try:
        profile = ProfileFactory.create(profile_type)
        return jsonify({"type": profile_type, "sections": profile.get_sections()})
    except ValueError as e:
        logger.error(e)
        return jsonify({"error": str(e)}, 400)

if __name__ == "__main__":
    app.run(debug=True)