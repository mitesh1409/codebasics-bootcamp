def triangle(base, height):
    return round((base * height) / 2, 2)

print(f'Inside area.py - __name__: {__name__}')

mini_triangle_area = triangle(10, 5)
print(f'triangle area: {mini_triangle_area}')
