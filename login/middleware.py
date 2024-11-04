# middleware.py
from django.utils.deprecation import MiddlewareMixin
import jwt

class TokenAuthenticationMiddleware(MiddlewareMixin):
    def process_request(self, request):
        token = request.session.get('token')
        username = request.session.get('username')
        name = request.session.get('name')
        title = request.session.get('title')
        department = request.session.get('department')
        mail = request.session.get('mail')
        photo = request.session.get('photo')

        if token and username:
            try:
                # Decodifica o token para garantir que seja válido
                payload = jwt.decode(token, 'mxygJRruLUnA6pRf9hlblb8Q32XyHmUPUfvhQgKvAX8=', algorithms=['HS256'])
                
                # Apenas armazene o username na requisição
                request.user = username  # Ou um objeto User se preferir
                request.user = name  # Ou um objeto User se preferir
                request.user = title  # Ou um objeto User se preferir
                request.user = department  # Ou um objeto User se preferir
                request.user = mail  # Ou um objeto User se preferir
                request.user = photo
            except jwt.ExpiredSignatureError:
                request.user = None  # Token expirado
            except jwt.InvalidTokenError:
                request.user = None  # Token inválido
        else:
            request.user = None  # Se não houver token, o usuário não está autenticado
