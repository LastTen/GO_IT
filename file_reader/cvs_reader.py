import csv

users = [
    {
        "name": "Allen Raymond",
        "email": "nulla.ante@vestibul.co.uk",
        "phone": "(992) 914-3792",
        "favorite": False,
    },
    {
        "name": "Allen Raymond1",
        "email": "nulla.ante@vestibul.co.uk",
        "phone": "(992) 914-3792",
        "favorite": True,
    },
    {
        "name": "Allen Raymond2",
        "email": "nulla.ante@vestibul.co.uk",
        "phone": "(992) 914-3792",
        "favorite": False,
    },
]
file = "cvsfile.cvs"


def write_contacts_to_file(filename, contacts):
    with open(filename, "w", newline="") as fh:
        field_names = [key for key in contacts[0]]
        # field_names = contacts[0].keys()
        writer = csv.DictWriter(fh, fieldnames=field_names)
        writer.writeheader()
        for key in contacts:
            writer.writerow(key)


def read_contacts_from_file(filename):
    contacts = []
    with open(filename, "r", newline="") as fh:
        reader = csv.DictReader(fh)
        for row in reader:
            if row["favorite"] == "True":
                row["favorite"] = True
            if row["favorite"] == "False":
                row["favorite"] = False
            contacts.append(row)
    return contacts


write_contacts_to_file(file, users)
print(read_contacts_from_file(file))
