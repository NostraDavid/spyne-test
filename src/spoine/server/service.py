from spyne import Application, ServiceBase, rpc
from spyne.server.django import DjangoApplication
from django.views.decorators.csrf import csrf_exempt
from spyne.protocol.soap import Soap11
from spoine.models.request import SpoineRequest
from spoine.models.response import SpoineResponse


class SpoineService(ServiceBase):
    @rpc(SpoineRequest, _returns=SpoineResponse, _body_style="bare")
    def SpoineService(ctx, req: SpoineRequest):
        print(repr(req))
        resp = SpoineResponse()
        return resp


spoine_application = Application(
    services=[SpoineService],
    tns="target_namespace",
    name="SpoineService",
    in_protocol=Soap11(),
    out_protocol=Soap11(),
)
spoine_app = csrf_exempt(DjangoApplication(spoine_application))
