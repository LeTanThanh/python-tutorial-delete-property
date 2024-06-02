class Person:
  def __init__(self, name) -> None:
    self.name = name

  @property
  def name(self):
    return self._name

  @name.setter
  def name(self, value):
    if value.strip() == "":
      raise ValueError("name cannot be empty")
    self._name = value

  @name.deleter
  def name(self):
    del self._name
