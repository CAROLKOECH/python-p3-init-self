#!/usr/bin/env python3

class Person:
    def __init__(self, name):
        self.name = name

if __name__ == "__main__":
    person = Person("Alice")
    print(f"Person's name: {person.name}")
