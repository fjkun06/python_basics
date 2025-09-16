class Employee:
    """Give employee raise."""

    def __init__(self, first, last, annual_salary):
        """Set Default Values"""
        self.first = first
        self.last = last
        self.annual_salary = annual_salary
        self.raised_salary = annual_salary

    def get_full_name(self):
        """Return employye full name"""
        fullname = f"{self.first} {self.last}"
        return fullname.title()

    def get_initial_salary(self):
        """Get Employee initial salary"""
        return self.annual_salary

    def get_raised_salary(self):
        """Get Employee raised salary"""
        return self.raised_salary

    def give_raise(self, amount=0):
        """Give custom or default raise"""
        if amount:
            self.raised_salary += amount
        else:
            self.raised_salary += 5_000
