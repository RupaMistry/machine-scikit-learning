from rest_framework.response import Response
from portalApp.exceptions import ModelException


def apiWrapper(api_method):
    def wrapper(*args, **kwargs):
        try:
            return api_method(*args, **kwargs)
        except ModelException as e:
            return Response(dict(status='Error', message=e.get_message()))
        except Exception as e:
            return Response(dict(status='Error', message=str(e)))
    return wrapper
