#figure 모듈2
#이 모듈은 Line 클래스와 도형의 넓이를 구하는 함수를 제공한다.
import figure_main

import math

class Line:
    #클래스 Line: 선의 길이
    __length = 1
    #__length : 선의 길이이고 기본값은 1. 외부에서 접근 불가능한 필드.
    def __init__(self, length = 1):
        if( (type(length) == int or type(length) == float) and length > 0 ):
            self.__length = length
        else:
            self.__length = 1
        """
        생성자: 초기 __length 값을 설정
        length가 0 이하이거나 int/float 타입이 아닌 경우 기본 값 1로 설정
        """

    def set_length(self, length) :
        if( (type(length) == int or type(length) == float) and length > 0 ):
            self.__length = length
        """
        __length 값을 설정하는 메소드
        length가 0 이하이거나 int/float 타입이 아닌 경우 값을 변경하지 않음
        """


    def get_length(self) :
        return self.__length
        """
        __length 값을 반환하는 메소드
        """


def area_square(line):
    """
    길이를 입력받아 정사각형 넓이를 구하는 함수
    정사각형의 넓이 = 한 변의 길이 ** 2
    Args: line(한 변의 길이)
    Returns:
        int or float: 정사각형의 넓이를 반환
        매개변수의 타입이 Line 클래스가 아닐 경우 0을 반환
    """
    square_area = line.get_length() ** 2
    if isinstance(line, Line):
        return square_area
    else:
        return 0

def area_circle(line):
    """
    길이를 입력받아 원의 넓이를 구하는 함수
    원의 넓이 = 반지름 ** 2 * PI
    Args: line(반지름의 길이)
    Returns:
        int or float: 원의 넓이를 반환
        매개변수의 타입이 Line 클래스가 아닐 경우 0을 반환
    """
    circle_area = line.get_length() ** 2 * math.pi
    if isinstance(line, Line):
        return circle_area
    else:
        return 0

def area_regular_triangle(line):
    """
    길이를 입력받아 정삼각형 넓이를 구하는 함수
    Args: line(한 변의 길이)
    Returns:
        int or float: 정삼각형의 넓이를 반환
        매개변수의 타입이 Line 클래스가 아닐 경우 0을 반환
    """
    triangle_area = line.get_length() ** 2 * (math.sqrt(3) / 4)
    if isinstance(line, Line):
        return triangle_area
    else:
        return 0