from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
import requests



def get_is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def get_is_perfect(n):
    return n == sum(i for i in range(1, n) if n % i == 0)

def is_armstrong(n):
    digits = [int(d) for d in str(n)]
    return n == sum(d**len(digits) for d in digits)

def get_fun_fact(n):
    response = requests.get(f"http://numbersapi.com/{n}")
    if response.status_code == 200:
        return response.text
    return "No fun fact available"

def get_number_properties(n):
    properties = []
    if is_armstrong(n):
        properties.append("armstrong")
    if n % 2 == 0:
        properties.append("even")
    else:
        properties.append("odd")
    return properties

def get_digit_sum(n):
    return sum(int(d) for d in str(n))



class MathAPIView(APIView):
    def get(self, request, n):
        try:
            number = int(n)
            is_prime = get_is_prime(n)
            is_perfect = get_is_perfect(n)
            properties = get_number_properties(n)
            fun_fact = get_fun_fact(n)
            digit_sum = get_digit_sum(number)
            data = {
                "number": number,
                "is_prime": is_prime,
                "is_perfect": is_perfect,
                "properties": properties,
                "digit_sum": digit_sum,
                "fun_fact": fun_fact,

            }
            return Response(data, status=status.HTTP_200_OK)
        except ValueError:
            return Response({"number": "alphabet", "error": True}, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


