from dataclasses import dataclass

@dataclass
class MandelSet:
    result: str

def mandelbrot_set(c: complex, max_iter: int) -> int:
    z = 0j
    n = 0
    while abs(z) < 2 and n < max_iter:
        z = z * z + c
        n += 1
    return n

def mandel(max_iter: int) -> MandelSet:
    width = 80
    height = 40
    x_min, x_max = -2.0, 1.0
    y_min, y_max = -1.5, 1.5
    x_step = (x_max - x_min) / width
    y_step = (y_max - y_min) / height

    def pixel_character(n: int) -> str:
        if n <= 10:
            return ' '
        if n <= 20:
            return '.'
        if n <= 30:
            return '+'
        if n <= 40:
            return '='
        if n <= 50:
            return '?'
        if n <= 60:
            return '#'
        if n <= 70:
            return ':'
        return '*'

    result = ''.join(
        ''.join(
            pixel_character(mandelbrot_set(complex(x_min + x_step * x, y_min + y_step * y), max_iter))
            for x in range(width)
        ) + '\n'
        for y in range(height)
    )

    return MandelSet(result)
