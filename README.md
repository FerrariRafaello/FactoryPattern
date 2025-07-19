# Factory Pattern Example in Python

This project demonstrates the Factory Design Pattern in Python with an emphasis on clean Object-Oriented Programming (OOP) principles. It showcases:
- Simple Factory: Creating objects without exposing the instantiation logic to the client.
- Factory Method: Letting subclasses decide which class to instantiate.
- Abstract Factory: Creating related objects without specifying their concrete classes.
---

**Features**
- Clear separation of concerns following SOLID principles.
- Usage of Python’s abc module for abstract base classes.
- Demonstrates dynamic object creation using eval() for educational purposes.
- Simple console output illustrating object behaviors.
- Ready to be extended for integration with REST APIs or UI layers.
---

**Code Overview**
- Simple Factory
- Animal (abstract class): defines interface speak.
- Concrete classes Dog and Cat implement speak.
- Factory class produces instances based on input strings.
---

**Factory Method**
- Section (abstract class) defines interface description.
- Concrete classes implement specific sections (PersonalSection, AlbumSection, etc.).
- Profile (abstract class) builds profiles by composing sections.
- Concrete profiles (Facebook, Twitter) specify which sections to include.
---

**How to Run**
Simply run the main Python script:
-> python3 FactoryPatternDemo.py

You will see output illustrating the created objects and their behavior.

**Why Use the Factory Pattern?**
- Decouples object creation from usage.
- Makes code easier to maintain and extend.
- Enables code reuse and enforces consistent interfaces.
---

Contributions
Feel free to fork this repository and contribute enhancements or fixes.

Enjoy clean and maintainable code!
