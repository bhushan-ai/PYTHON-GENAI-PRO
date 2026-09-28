class ChaiUtils:

    def clean_ingredients( text):
        return [item.strip() for item in text.split(",")]

raw = " water, milk, ginger , honey"


# using decorators
cleaned = ChaiUtils.clean_ingredients(raw)
print(cleaned)