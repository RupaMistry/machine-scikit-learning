from rest_framework.response import Response
from rest_framework.views import APIView
from portalApp.views.generic_model import BaseLearningModel
from portalApp.views.utils import apiWrapper


class GenericModelController(APIView):
    @apiWrapper
    def post(self, request):
        model = BaseLearningModel(
            user_id=request.user.id,
            params=request.data
        )
        return Response(model.response)
