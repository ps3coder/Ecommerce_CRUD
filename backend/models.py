from config import db

class Product(db.Model):
    id = db.Column(db.integer, primary_key=True)
    product_name = db.Column(db.String(255),unique=True, nullable=False)
    price = db.Column(db.Float, nullable=False)
    description = db.Column(db.Text, nullable=False)
    specification = db.Column(db.Text, nullable=False)

    def to_json(self):
        return {
            "id": self.id,
            "productName": self.product_name,
            "price":self.price,
            "description":self.description,
            "specification":self.specification
        }