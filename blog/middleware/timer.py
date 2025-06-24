import time
from django.utils.deprecation import MiddlewareMixin

class TimerMiddleware(MiddlewareMixin):
    def process_request(self, request):
        request.start_time = time.time()

    def process_response(self, request, response):
        duration = time.time() - getattr(request, 'start_time', time.time())
        print(f"Tiempo de respuesta: {duration:.2f} segundos")
        return response

