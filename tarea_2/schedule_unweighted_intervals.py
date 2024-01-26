class Petition:
    def __init__(self, start, length) -> None:
        self.start = start
        self.end = start + length
    
    def __repr__(self) -> str:
        return f'({self.start}, {self.end})'

def schedule_unweighted_intervals(requests) -> list:
    # Ordena las peticiones por su tiempo de finalización
    requests.sort(key=lambda request: request.end)

    # Inicializa el conjunto de peticiones aceptadas
    A = []
    # Inicializa el tiempo de finalización más reciente
    last_end_time = 0

    # Itera sobre las peticiones ordenadas
    for request in requests:
        # Si la petición no se solapa con la última petición aceptada
        # entonces la aceptamos
        if last_end_time <= request.start:
            A.append(request)
            last_end_time = request.end

    return A

requests = [
    Petition(6, 7),
    Petition(6, 5),
    Petition(11, 1),
]

print(schedule_unweighted_intervals(requests))