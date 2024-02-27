from typing import List

PLAYER1 = '-'
PLAYER2 = '|'

WINNING_COMBINATIONS = [
    [0, 1, 2],  # Row 1
    [3, 4, 5],  # Row 2
    [6, 7, 8],  # Row 3
    [0, 3, 6],  # Column 1
    [1, 4, 7],  # Column 2
    [2, 5, 8],  # Column 3
    [0, 4, 8],  # Diagonal from top-left to bottom-right
    [2, 4, 6]   # Diagonal from top-right to bottom-left
]

class GameState:
    def __init__(self) -> None:
        self.board = [''] * 9
        self.last_move = None

    def is_cross(self, pos: int) -> bool:
        """
        Verifica si la posición [pos] del tablero es un cruce entre ambos jugadores
        """
        return PLAYER1 in self.board[pos] and PLAYER2 in self.board[pos]

    def successors(self, player: str):
        """
        Genera los sucesores para el jugador [player] en el estado actual del juego
        """
        for i, cell in enumerate(self.board):
            if player not in cell and (self.last_move is None or self.last_move != i):    
                successor = GameState()
                successor.board = self.board[:]  # Copia el tablero actual
                successor.board[i] += player     # Agrega el movimiento del jugador
                successor.last_move = i          # Actualiza el último movimiento
                yield successor

    def evaluate(self) -> int:
        """
        Evalúa el estado actual del juego
        0: El juego no ha terminado
        1: El juego ha terminado
        """
        for combination in WINNING_COMBINATIONS:            
            if all(self.is_cross(pos) for pos in combination):
                return 1
        return 0

    def has_successors(self) -> bool:
        """
        Verifica si el estado actual del juego tiene sucesores
        """
        return self.evaluate() != 1

def first_player(state: GameState, depth: int, alpha: int, beta) -> int:
    """
    Algoritmo minimax para el primer jugador
    """
    if depth == 0 or not state.has_successors():
        return -state.evaluate()

    best_score = float('-inf')
    for successor_state in state.successors(PLAYER1):
        best_score = max(best_score, second_player(successor_state, depth - 1, alpha, beta))
        alpha = max(alpha, best_score)
        if beta <= alpha:
            break
    return best_score

def second_player(state: GameState, depth: int, alpha: int, beta) -> int:
    """
    Algoritmo minimax para el segundo jugador
    """
    if depth == 0 or not state.has_successors():
        return state.evaluate()
    
    best_score = float('inf')
    for successor_state in state.successors(PLAYER2):
        best_score = min(best_score, first_player(successor_state, depth - 1, alpha, beta))
        beta = min(beta, best_score)
        if beta <= alpha:
            break
    return best_score

def main() -> None:
    initial_state = GameState()
    alpha_value = float('-inf')
    beta_value = float('inf')
    search_depth = 100
    print(first_player(initial_state, search_depth, alpha_value, beta_value))

if __name__ == '__main__':
    main()
