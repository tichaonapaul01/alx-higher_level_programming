import os

if not os.path.exists("models"):
    os.makedirs("models")

with open("models/__init__.py", "w") as init_file:
    pass
