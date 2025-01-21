
from products import dao

class Product:
    def __init__(self, id: int, name: str, description: str, cost: float, qty: int = 0):
        self.id = id
        self.name = name
        self.description = description
        self.cost = cost
        self.qty = qty

    @classmethod
    def load(cls, data: dict):
        """Alternative constructor to create a Product from a dictionary."""
        return cls(**data)

def list_products() -> list[Product]:
    """Fetch and return a list of Product objects."""
    return [Product.load(product) for product in dao.list_products()]

def get_product(product_id: int) -> Product:
    """Fetch and return a single Product object by ID."""
    return Product.load(dao.get_product(product_id))

def add_product(product: dict):
    """Add a new product."""
    dao.add_product(product)

def update_qty(product_id: int, qty: int):
    """Update the quantity of a product, ensuring it is not negative."""
    if qty < 0:
        raise ValueError('Quantity cannot be negative')
    dao.update_qty(product_id, qty)

