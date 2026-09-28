class ChaiOrder:
    def __init__(self, tea_type, sweatness, size):
        self.tea_type = tea_type
        self.sweatness = sweatness
        self.size = size

    @classmethod
    def from_dict(cls, order_data):
        return cls(
            order_data["tea_type"],
            order_data["sweatness"],
            order_data["size"]
        )

    @classmethod
    def from_string(cls, order_string):
        tea_type, sweatness, size = order_string.split("-")
        return cls(tea_type, sweatness, size)



class ChaiUtils:
    @staticmethod
    def valid_sizde(size):
        return size in ["Small", "Medium", "Large"]



order1 = ChaiOrder.from_dict({"tea_type" : "Masala", "sweatness": "medium", "size": "Large"})

order2 = ChaiOrder.from_string("Ginger-low-Small")

order3 = ChaiOrder("large", "Low" , 'large')

print(order1.__dict__)
print(order2.__dict__)
print(order3.__dict__)