class Battery:
  """Battery class."""

  def __init__(self, battery_size=40):
      """Initialize the battery's attributes."""
      self.battery = battery_size
      
  def describe_battery(self):
    """Print a statement describing abttery size"""
    print(f"This car has a {self.battery}-kWh battery.")
