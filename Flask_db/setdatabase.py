from app import db, Puppy

db.create_all()


sam = Puppy('Sammy', 3, "pug")
frank = Puppy('Frankie', 4, "lab")


print(sam.id)
print(frank.id)


db.session.add_all([sam, frank])

db.session.commit()

print(sam.id)
print(frank.id)
