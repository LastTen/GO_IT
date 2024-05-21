import json

contacts = [
    {
        "name": "Allen Raymond",
        "email": "nulla.ante@vestibul.co.uk",
        "phone": "(992) 914-3792",
        "favorite": False,
    }
]


def write_contacts_to_file(filename, contacts):
    new_contacts = {"contacts": contacts}
    with open(filename, "w") as fh:
        json.dump(new_contacts, fh, indent=2)


def read_contacts_from_file(filename):
    with open(filename, "r") as fh:
        x = json.load(fh)
        return x["contacts"]


if __name__ == "__main__":
    write_contacts_to_file("filename.json", contacts)
    print(read_contacts_from_file("filename.json"))
