# Factory Pattern Demo (Python)

A concise demonstration of the Factory Design Pattern in Python, showcasing how to decouple object creation from business logic and adhere to SOLID principles. This repo covers three variants:

- **Simple Factory**: Create objects without exposing instantiation logic to the client.  
- **Factory Method**: Let subclasses decide which class to instantiate.  
- **Abstract Factory**: Produce families of related objects without knowing their concrete classes.
---

**What You’ll Learn**

- Encapsulating object‑creation logic in a dedicated Factory.  
- Differences between Simple Factory, Factory Method, and Abstract Factory.  
- Defining abstract base classes with Python’s `abc` module.  
- Dynamically creating objects (`eval()` used for educational purposes).  
- How to extend the pattern for REST APIs or UI layers.
---

**Features**

- **SOLID‑aligned**: Clear separation of concerns and single responsibility.  
- **ABC usage**: Leveraging `abc.ABC` and `@abstractmethod` for interfaces.  
- **Dynamic instantiation**: Educational use of `eval()` to select classes at runtime.  
- **Console demo**: Simple CLI output illustrating behavior of created objects.
---

## Code Overview

### Simple Factory  
- **`Animal` (abstract)** defines `speak()`.  
- **`Dog`** and **`Cat`** implement `speak()`.  
- **`AnimalFactory`** returns an instance based on a string key.

### Factory Method  
- **`Section` (abstract)** with `description()`.  
- Concrete sections (e.g. `PersonalSection`, `AlbumSection`) implement `description()`.  
- **`Profile` (abstract)** builds profiles by composing sections.  
- Concrete profiles (`FacebookProfile`, `TwitterProfile`) specify which sections to include via a factory method.

### Abstract Factory  
- (If implemented) A pair of factories producing related objects (e.g. GUI widgets for different themes).

## Getting Started

1. **Clone the repo**  
   ```bash
   git clone https://github.com/FerrariRafaello/FactoryPattern.git
   cd FactoryPattern
Run the demo

bash
Copy
Edit
python3 FactoryPatternDemo.py
You’ll see console output showing the objects being created and their behaviors.

Why Use the Factory Pattern?
Decouples object creation from usage.

Eases maintenance and extension when adding new types.

Promotes code reuse and enforces consistent interfaces.

Contributing
Feel free to fork this repository and submit pull requests—whether it’s adding an Abstract Factory example, integrating with a web framework, or improving documentation!

Enjoy exploring clean, maintainable OOP in Python!
