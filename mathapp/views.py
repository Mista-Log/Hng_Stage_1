# from rest_framework.views import APIView
import requests
from django.http import JsonResponse
# from rest_framework.response import Response
from django.views import View



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
    if n > 0:
        if is_armstrong(n):
            properties.append("armstrong")
    if n % 2 == 0:
        properties.append("even")
    else:
        properties.append("odd")
    return properties




def get_digit_sum(n):
    return sum(int(d) for d in str(abs(n)))



# class MathAPIView(APIView):

#     def get(self, request):

#         number = request.GET.get("number") 

#         try:
#             number = int(number)
#             is_prime = get_is_prime(number)
#             is_perfect = get_is_perfect(number)
#             properties = get_number_properties(number)
#             fun_fact = get_fun_fact(number)
#             digit_sum = get_digit_sum(number)
#             data = {
#                 "number": number,
#                 "is_prime": is_prime,
#                 "is_perfect": is_perfect,
#                 "properties": properties,
#                 "digit_sum": digit_sum,
#                 "fun_fact": fun_fact,
#             }
#             return JsonResponse(data, status=200)
#         except Exception as e:
#             return JsonResponse({"number": "alphabet", "error": True}, status=400)

# ...existing code...
# def get_success_message():
#     return {"message": "Request was successful", "status": 200}
def get_success_message():
    return {"message": "Request was successful", "status": 200}
def get_bad_request_message():
    return {"number": "alphabet", "error": True}
    # def get_number_properties(n):
    #     properties = []
    #     if n < 0:
    #         properties.append("negative")
    #     else:
    #         if is_armstrong(n):
    #             properties.append("armstrong")
    #         if n % 2 == 0:
    #             properties.append("even")
    #         else:
    #             properties.append("odd")
    #     return properties

# class MathAPIView(APIView):
#     def get(self, request):
#         number = request.GET.get("number")

#         if number is None:
#             return Response(get_bad_request_message(), status=400)

#         try:
#             number = int(number)
#         except ValueError:
#             return Response(get_bad_request_message(), status=400)

#         is_prime = get_is_prime(number)
#         is_perfect = get_is_perfect(number)
#         properties = get_number_properties(number)
#         fun_fact = get_fun_fact(number)
#         digit_sum = get_digit_sum(number)

#         response_data = {
#             "number": number,
#             "is_prime": is_prime,
#             "is_perfect": is_perfect,
#             "properties": properties,
#             "digit_sum": digit_sum,
#             "fun_fact": fun_fact,

#         }

#         return Response(response_data, status=200)

    # def get(self, request):
    #     number = request.GET.get("number")

    #     if number is None:
    #         return Response({"number": "alphabet", "error": True}, status=400)

    #     try:
    #         number = int(number)
    #     except ValueError:
    #         return Response({"number": "alphabet", "error": True}, status=400)

    #     is_prime = get_is_prime(number)
    #     is_perfect = get_is_perfect(number)
    #     properties = get_number_properties(number)
    #     fun_fact = get_fun_fact(number)
    #     digit_sum = get_digit_sum(number)

    #     response_data = {
    #         "number": number,
    #         "is_prime": is_prime,
    #         "is_perfect": is_perfect,
    #         "properties": properties,
    #         "fun_fact": fun_fact,
    #         "digit_sum": digit_sum,
    #     }

    #     return Response(response_data)

class MathAPIView(View):
    def get(self, request):
        try:
            number = request.GET.get("number")

            if number is None:
                return JsonResponse(get_bad_request_message(), status=400)

            try:
                number = int(number)
            except ValueError:
                return JsonResponse(get_bad_request_message(), status=400)

            is_prime = get_is_prime(number)
            is_perfect = get_is_perfect(number)
            properties = get_number_properties(number)
            fun_fact = get_fun_fact(number)
            digit_sum = get_digit_sum(number)

            response_data = {
                "number": number,
                "is_prime": is_prime,
                "is_perfect": is_perfect,
                "properties": properties,
                "digit_sum": digit_sum,
                "fun_fact": fun_fact,
            }

            return JsonResponse(response_data, status=200)
        except Exception as e:
            return JsonResponse({"error": str(e)}, status=500)