class vehicle:
  def __init__(self, bodystyle):
    self.bodystyle = bodystyle

class car(vehicle):
  def __init__(self, enginetype):
    super().__init__("car")
    self.wheels = 4
    self.doors = 4
    self.enginetype = enginetype

class motorcycle(vehicle): # motorcycle should inherit from vehicle
  def __init__(self, enginetype, hassidecar):
    super().__init__("motorcycle")
    if (hassidecar):
      self.wheels = 3
    else:
      self.wheels = 2

    self.doors = 0
    self.enginetype = enginetype

class scooter(vehicle):
  def __init__(self, hasaseat): # Added space between def and __init__
    super().__init__("scooter")
    self.wheels = 2
    self.doors = 0
    if (hasaseat):
      self.enginetype = "gas"
    else:
      self.enginetype = "electric"


car1 = car('gas')
car2 = car("electric")
mc1 = motorcycle("gas", False)
mc2 = motorcycle("electric", True)
Escooter = scooter(False) # Provided both arguments
Moped = scooter(True)

print(mc1.wheels)
print(car2.enginetype)
print(mc1.doors)
print(mc2.wheels)
print(Moped.enginetype) # Corrected from Escooter.engine to Escooter.enginetype