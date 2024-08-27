# In Python, mixins are a design pattern used to add functionality to classes without using inheritance. Here's how mixins typically work:
#   - Code reuse: Mixins allow you to reuse code across multiple classes without creating a complex inheritance hierarchy.
#   - Multiple inheritance: Python supports multiple inheritance, which makes mixins possible. A class can inherit from both its main parent class and one or more mixin classes.
#   - Modular design: Mixins promote a modular approach to class design, where each mixin provides a specific set of related methods or attributes.
#   - Enhance functionality: Mixins are used to add optional features or behaviors to a class without modifying its core functionality.
#   - Avoid diamond problem: Mixins help avoid the "diamond problem" of multiple inheritance by keeping the inheritance hierarchy simpler.

# Vedio Reference: https://www.youtube.com/watch?v=pCekYAodyLo&list=PLvQDgAXJ4ADMzlySkwIGomEA9j1Vgq5uS&index=11

# 很多 functionality 可以通过 decorator 來实现

class LoggerMixin:
    def log(self, message):
        print(f"Log: {message}")

class DBConnectorMixin:
    def connect_to_db(self):
        print("Connecting to database...")

class UserManager(LoggerMixin, DBConnectorMixin):
    def create_user(self, username):
        self.connect_to_db()
        # Create user logic here
        self.log(f"User {username} created")