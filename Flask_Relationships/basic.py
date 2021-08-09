# Create entries into the tables


from app import db, Puppy, Owner, Toy


# Create 2 puppies

rufus = Puppy('rufus')
fido = Puppy('fido')


# add puppies to the db

db.session.add_all([rufus, fido])
db.session.commit


# Check
print(Puppy.query.all())


rufus = Puppy.query.filter_by(name='rufus').first()
print(rufus)


# create owner

jose = Owner('jose', rufus.id)

# Give rufus some toys

toy1 = Toy('Chew toy', rufus.id)
toy2 = Toy('ball', rufus.id)
print(rufus.report_toys())

db.session.add_all([jose, toy2, toy1])

db.session.commit()

# Grab rufus after those additions

rufus = Puppy.query.filter_by(name='rufus').first()
print(rufus)
