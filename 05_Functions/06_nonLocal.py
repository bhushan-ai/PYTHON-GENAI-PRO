
def update_order():
    chai_type = "Elaichi"
    def kitchen():
        nonlocal chai_type #use to access above function variable
        chai_type = "Kesar"
    kitchen()
    print("After kitchen update ", chai_type )


update_order()