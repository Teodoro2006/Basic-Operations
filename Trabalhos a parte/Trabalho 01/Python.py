class Person:
  def __init__(self, name, age, job, Country):
    self.name = name
    self.age = age
    self.job = job
    self.Country = Country

class Person1:
  def __init__(self1, name1, age1, job1, Country1):
    self1.name1 = name1
    self1.age1 = age1
    self1.job1 = job1
    self1.Country1 = Country1 
p1 = Person("Teodoro", 18, "student", "Portugal")
p2 = Person1("Jorge",18, "student", "Portugal" )


print(p1.name)
print(p1.age)
print(p1.job)
print(p1.Country)

print(p2.name1)
print(p2.age1)
print(p2.job1)
print(p2.Country1)
