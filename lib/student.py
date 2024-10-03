#!/usr/bin/env python

from user import User

class Student(User):
    def __init__(self, first_name, last_name):
        super().__init__(first_name, last_name)  # Initialize the User class
        self.knowledge = []  # Initialize an empty knowledge list

    def learn(self, knowledge_str):
        self.knowledge.append(knowledge_str)  # Add knowledge to the list