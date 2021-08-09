from app import db, Puppy


# Create entry

my_puppy = Puppy('Rufus', 5, "pug")  # Create

db.session.add(my_puppy)

db.session.commit()


# Read

all_puppies = Puppy.query.all()  # list of puppies objects in the table


print(all_puppies)


# Select by id
puppy_one = Puppy.query.get(1)


# Filters

puppy_frankie = Puppy.query.filter_by(name='Frankie')
print(puppy_frankie.all())


# Update
first_puppy = Puppy.query.get(1)
first_puppy.age = 10
db.session.add(first_puppy)
db.session.commit()


# Delete
second_puppy = Puppy.query.get(2)
print("Second puppy: "+second_puppy)
db.session.delete(second_puppy)
db.session.commit()


#
all_puppies = Puppy.query.all()
print(all_puppies)
