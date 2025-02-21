from uuid import uuid3, NAMESPACE_DNS

u = uuid3(NAMESPACE_DNS, "example.com")
print(u)  # Example: 5df41881-3aed-3515-88a7-2f4a814cf09e
