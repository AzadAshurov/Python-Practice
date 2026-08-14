import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

name = "Azad"
age = 22

print(f"Hello, my name is {name} and I'm {age} years old")

print(type(name))
print(type(age))

def say_hello(your_name: str) -> None:
    print(f"Hello {your_name}")

say_hello(name)
say_hello("GPT")

def add(a: int, b: int) -> int:
    return a + b

print(add(10, 20))
print(add("10", "20"))   # специально для эксперимента

logger.info("Application started")
logger.warning("Demo warning")
logger.error("Demo error")