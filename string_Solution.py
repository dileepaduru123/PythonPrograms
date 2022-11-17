def string_solution(s: str, T: str):
    """

    :param s:
    :param T:
    :return:
    """
    if not s or not T:
        print("IMPOSSIBLE")
        return 0
    s_size = len(s)
    t_size = len(T)
    if s_size == t_size:
        if s == T:
            print("EQUAL")
            return 0
        swap_element(S, T, s_size)
    elif s_size > t_size:
        swap_element(S, T, s_size)
        for j in range(t_size,s_size):
            print("REMOVE {}".format(s[j]))
    elif s_size <t_size:
        swap_element(S, T, t_size)
        for j in range(s_size, t_size):
            print("INSERT {}".format(T[j]))


def swap_element(S:str, T: str, tell_size: int):
    """

    :param S:
    :param T:
    :param tell_size:
    :return:
    """
    data = []
    for i in range(tell_size):
        if S[i] !=T[i]:
            data.append([S[i], T[i]])
        if len (data) !=tell_size:
            for j, k in data:
                print("SWAP element {} with {}".format(j, k))
        else:
            print("IMPOSSIBLE")
