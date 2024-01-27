class Petition:
    def __init__(self, start, length) -> None:
        self.start = start
        self.end = start + length
    
    def __repr__(self) -> str:
        return f'({self.start}, {self.end})'

def schedule_unweighted_intervals() -> list:
    # Lee el número de peticiones
    t = int(input())
    
    # Lee las peticiones
    requests = []
    for i in range(t):
        start, length = map(int, input().split())
        requests.append(Petition(start, length))
    
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

if __name__ == '__main__':
    print(schedule_unweighted_intervals())