class Contact:
    def __init__(self, name, email, phone, address):
        self.name = name
        self.email = email
        self.phone = phone
        self.address = address

    def to_json(self):
        return {
            "name": self.name,
            "email": self.email,
            "phone": self.phone,
            "address": self.address,
        }
    @staticmethod
    def from_json(data):
        return Contact(data["name"], data["email"], data["phone"], data["address"])
