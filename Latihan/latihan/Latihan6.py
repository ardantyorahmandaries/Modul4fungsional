def point(x, y):
    return x, y

def line_equation_of(pl, M):
    # Menghitung nilai C (konstanta)
    x, y = pl
    C = y - M * x

    # Membuat dan mengembalikan persamaan garis
    return f"y = {M:.2f}x + {C:.2f}"

# Titik (1, 5) dan gradien 0
point_l = point(1, 5)
gradien = 0  # Ubah gradien sesuai dengan pernyataan

# Mencetak persamaan garis yang melalui titik (1, 5) dan bergradien 0
print("Persamaan garis yang melalui titik (1, 5) dan bergradien 0:")
print(line_equation_of(point_l, gradien))
