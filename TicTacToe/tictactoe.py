"""
Tic Tac Toe Player
"""

import math
import copy

X = "X"
O = "O"
EMPTY = None


def initial_state():
    """
    Returns starting state of the board.
    """
    return [[EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]]


def player(board):
    """
    Retorna o jogador que tem o próximo turno no tabuleiro.

    O jogador X sempre inicia o jogo. Após cada jogada, os turnos alternam entre X e O.
    Se o tabuleiro estiver em um estado terminal (fim de jogo), qualquer valor de retorno é aceitável.

    Args:
        board (list): O estado atual do tabuleiro, uma matriz 3x3.

    Returns:
        str: "X" se for a vez do jogador X, "O" se for a vez do jogador O.
    """
    x_count = sum(row.count(X) for row in board)
    o_count = sum(row.count(O) for row in board)
    return X if x_count == o_count else O


def actions(board):
    """
    Retorna o conjunto de todas as ações possíveis no tabuleiro.

    Cada ação é representada como uma tupla (i, j), onde:
        - i: índice da linha (0, 1 ou 2)
        - j: índice da coluna (0, 1 ou 2)

    Uma ação é possível se a célula estiver vazia (EMPTY).
    Se o tabuleiro estiver em estado terminal, qualquer retorno é aceitável.

    Args:
        board (list): O estado atual do tabuleiro, uma matriz 3x3.

    Returns:
        set of tuple: Conjunto de posições disponíveis no formato (i, j).
    """
    return {(i, j) for i in range(3) for j in range(3) if board[i][j] == EMPTY}


def result(board, action):
    """
    Retorna um novo tabuleiro após aplicar a ação (i, j), sem modificar o original.

    A ação deve ser válida: ou seja, deve estar entre as posições vazias do tabuleiro.
    A jogada será feita pelo jogador que tem o turno atual.

    Args:
        board (list): O estado atual do tabuleiro, uma matriz 3x3.
        action (tuple): Uma tupla (i, j) representando a posição da jogada.

    Returns:
        list: Um novo tabuleiro com a jogada aplicada.

    Raises:
        ValueError: Se a ação for inválida.
    """
    if action not in actions(board):
        raise ValueError(f"Ação inválida: {action}")

    i, j = action
    new_board = copy.deepcopy(board)
    new_board[i][j] = player(board)
    return new_board


def winner(board):
    """
    Retorna o vencedor do jogo se houver um.

    O vencedor é o jogador (X ou O) que conseguiu alinhar três símbolos
    iguais em linha, coluna ou diagonal.

    Args:
        board (list): O estado atual do tabuleiro, uma matriz 3x3.

    Returns:
        str or None: "X" se X venceu, "O" se O venceu, ou None se não há vencedor.
    """
    # Verificar linhas e colunas
    for i in range(3):
        # Linha
        if board[i][0] == board[i][1] == board[i][2] != EMPTY:
            return board[i][0]
        # Coluna
        if board[0][i] == board[1][i] == board[2][i] != EMPTY:
            return board[0][i]

    # Verificar diagonais
    if board[0][0] == board[1][1] == board[2][2] != EMPTY:
        return board[0][0]
    if board[0][2] == board[1][1] == board[2][0] != EMPTY:
        return board[0][2]

    return None


def terminal(board):
    """
    Retorna True se o jogo acabou (vitória ou empate), False caso contrário.

    O jogo termina se:
    - Um dos jogadores venceu.
    - Todas as células estão preenchidas (empate).

    Args:
        board (list): O estado atual do tabuleiro, uma matriz 3x3.

    Returns:
        bool: True se o jogo acabou, False caso contrário.
    """
    return winner(board) is not None or all(cell != EMPTY for row in board for cell in row)


def utility(board):
    """
    Retorna a utilidade do tabuleiro terminal:
    - 1 se o jogador X venceu.
    - -1 se o jogador O venceu.
    - 0 se o jogo terminou empatado.

    Esta função só deve ser chamada quando o jogo já tiver terminado.

    Args:
        board (list): O estado final do tabuleiro, uma matriz 3x3.

    Returns:
        int: 1, -1 ou 0 conforme o resultado.
    """
    win = winner(board)
    if win == X:
        return 1
    elif win == O:
        return -1
    else:
        return 0


def minimax(board):
    """
    Retorna a ação ótima (i, j) para o jogador atual no tabuleiro, usando o algoritmo Minimax.

    Se o tabuleiro estiver em um estado terminal, retorna None.

    O algoritmo assume que ambos os jogadores jogam de forma ideal.
    X tentará maximizar o valor da utilidade, enquanto O tentará minimizar.

    Args:
        board (list): O estado atual do tabuleiro.

    Returns:
        tuple or None: A melhor ação (i, j) possível, ou None se o jogo terminou.
    """
    if terminal(board):
        return None

    turn = player(board)

    def max_value(state):
        if terminal(state):
            return utility(state), None
        v = -math.inf
        best_action = None
        for action in actions(state):
            min_val, _ = min_value(result(state, action))
            if min_val > v:
                v = min_val
                best_action = action
                if v == 1:
                    break  # melhor valor possível
        return v, best_action

    def min_value(state):
        if terminal(state):
            return utility(state), None
        v = math.inf
        best_action = None
        for action in actions(state):
            max_val, _ = max_value(result(state, action))
            if max_val < v:
                v = max_val
                best_action = action
                if v == -1:
                    break  # melhor valor possível para O
        return v, best_action

    if turn == X:
        _, action = max_value(board)
    else:
        _, action = min_value(board)

    return action