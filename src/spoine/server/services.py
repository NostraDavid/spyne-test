from spyne import Application, Service, ServiceBase, rpc, Unicode, Integer, Iterable
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


class HelloWorldService(Service):
    @rpc(Unicode, Integer, _returns=Iterable(Unicode))
    def say_hello(ctx, name, times):
        for i in range(times):
            yield "Hello, %s" % name


app = Application(
    # services=[SpoineService, HelloWorldService],
    services=[SpoineService],
    tns="target_namespace",
    name="SpoineService",
    in_protocol=Soap11(),
    out_protocol=Soap11(),
)
spoine_service = csrf_exempt(DjangoApplication(app))
