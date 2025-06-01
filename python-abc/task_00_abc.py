#!/usr/bin/env python3
"""
Defines an abstract class Animal with an abstract method sound,
and two subclasses Dog and Cat that implement sound.
"""

from abc import ABC, abstractmethod


class Animal(ABC):
    """Abstract base class representing an animal."""

    @abstractmethod
    def sound(self):
        """Abstract method to return the sound of the animal."""
        pass


class Dog(Animal):
    """Concrete class representing a Dog."""

    def sound(self):
        return "Bark"


class Cat(Animal):
    """Concrete class representing a Cat."""

    def sound(self):
        return "Meow"

