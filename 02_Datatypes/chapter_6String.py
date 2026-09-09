ordered_chai = "Ginger tea"
customer_name = "priya"
print(f"Order for {customer_name} :  {ordered_chai} please! ")

# Indexing & Slicing : start :end : step
chai_description = "Aromatic and Bold"
print(f"First word: {chai_description[0:8]}")
print(f"Last word: {chai_description[12:]}")
print(f"Last word: {chai_description[::-1]}")

#Encoding and Decoding
labelText = "Chai Special"
encoded_Text = labelText.encode("utf-8")
print(f"Non Encoded Text: {labelText}")
print(f"Encoded Text: {encoded_Text}")
decoded_Text = encoded_Text.decode("utf-8")
print(f"decoded Text: {decoded_Text}")
