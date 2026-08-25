print("Hello World")
from dataclasses import dataclass, field
import uuid
@dataclass
class Student:
    name: str
    age: int
    gpa: float
    id: str = field(default_factory=uuid.uuid4)

student_1 = Student("Alice", 20, 3.8)
student_2 = Student("Bob", 22, 3.5)
student_3 = Student("Alice", 20, 3.8)

print(student_1)
print(student_1.id)
print(student_1 == student_2 )
print(student_1 == student_3 )