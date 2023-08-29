#!/usr/bin/env python3

class Dog:
    def __init__(self, name, breed="Mutt"):
        self.name = name
        self.breed = breed

if __name__ == "__main__":
    fido = Dog("Fido")
    print(f"Fido's name: {fido.name}, breed: {fido.breed}")

    snoopy = Dog("Snoopy", "Beagle")
    print(f"Snoopy's name: {snoopy.name}, breed: {snoopy.breed}")
