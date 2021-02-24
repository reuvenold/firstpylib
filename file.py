import datetime

class Person(object):
  def __init__(self, fname, lname, birthdate):
    self._fn = fname
    self._ln = lname
    self._bd = birthdate
  def sayhi(self):
    print(f'Hello {self._fn}!')
   
