

def matrix_multiply(A, B):
    if len(A)==0 or len(B)==0:
        raise ValueError("matrice not exist")
    if len(A[0]) != len(B):
        raise ValueError("A's cols number not equal to B's rows number")

    C = [[0 for row in range(len(B[0]))] for col in range(len(A))]

    for i in range(len(A)):
        for j in range(len(B[0])):
            for k in range(len(B)):
                if isinstance(A[i][k], str) or isinstance(B[k][j], str):
                    raise ValueError("not a number from matrice")
                C[i][j] += A[i][k] * B[k][j]
    return C
