from faker import Faker
import random
from models import Game
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine

# Create an engine and session
engine = create_engine('sqlite:///games.db')  # Update the path if needed
Session = sessionmaker(bind=engine)
session = Session()

# Initialize Faker
fake = Faker()

# Clear the database to prevent duplicates
session.query(Game).delete()
session.commit()

# Add a console message to show progress
print("Seeding games...")

# Generate 50 random game records
games = [
    Game(
        title=fake.name(),
        genre=fake.word(),
        platform=fake.word(),
        price=random.randint(0, 60)
    )
    for _ in range(50)
]

# Save the new game data to the database
session.bulk_save_objects(games)
session.commit()

print("Seeding complete!")
