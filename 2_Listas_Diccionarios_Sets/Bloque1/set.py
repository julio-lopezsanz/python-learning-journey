"""
Tienes esta lista con emails repetidos, usa un set para eliminar 
    - Los duplicados 
    - Imprime cuántos emails únicos hay

emails = ["a@mail.com", "b@mail.com", "a@mail.com", "c@mail.com", "b@mail.com"]
"""
emails = ["a@mail.com", "b@mail.com", "a@mail.com", "c@mail.com", "b@mail.com"]
unique_emails = list(set(emails))

print(unique_emails)
print(f"Cantidad de emails unicos: {len(unique_emails)}")
