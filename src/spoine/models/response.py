from spyne import ComplexModel, Unicode


class SpoineResponse(ComplexModel):
    __namespace__ = "my_namespace"
    some_string = Unicode(min_occurs=0, max_occurs=1, nillable=False)
