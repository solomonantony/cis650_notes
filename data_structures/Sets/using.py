# Tuples are hashable (if their elements are hashable)
locations = {
    (40.7128, -74.0060): "New York",
    (34.0522, -118.2437): "Los Angeles",
}

print("City at (40.7128, -74.0060):", locations[(40.7128, -74.0060)])
