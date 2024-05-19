# Homework #4

## Module Description

- **Line Class**
  - Represents a line with a private length attribute.
  - Length can be set and retrieved using `set_length` and `get_length` methods.
  - Only int or float values are allowed

- **Functions**
  - `area_square(line)`: 사각형 넓이 구하는 함수
  - `area_circle(line)`: 원 넓이 구하는 함수
  - `area_regular_triangle(line)`: 정삼각형 넓이 구하는 함수

## Usage

```python
from figure import Line, area_square, area_circle, area_regular_triangle

line = Line(3)
print(area_square(line))  # Output: 9
print(area_circle(line))  # Output: 28.274333882308138
print(area_regular_triangle(line))  # Output: 3.897114317029974