# Define the calculator class to demonstrate class and static methods 
class Calculator:
    # Class attribute shared across all instances and accessible via class methods
    calculation_type = "Arithmetic Operations"
    @staticmethod
    def add(a,b):
        return a + b  # Static methods to add two numbers
    @classmethod
    def multiply(cls, a, b): # Class methods to multiply two numbers
        # Accesses class attribute 'calculation_type' using cls.
        print(f"calculation type: {cls.calculation_type}")
        return a * b
    
    