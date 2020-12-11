def wrapper(f):
    def fun(l):
        return f(['+91 ' + li[-10:-5] + ' ' + li[-5:] for li in l])
    return fun
# def wrapper(f):
#     def fun(l):
#         nl = []
#         for li in l:
#           nl += ['+91 '+li[-10:-5]+' '+li[-5:]]
#         return f(nl)
#     return fun


''' sort_phone has a decorator called wrapper. Whenever sort_phone is called sort_phone itself is passed to a wrapper(decorator) and fun is returned with l being passed to inner function (fun). So, basically we are extending sort_phone with a wrapper or also called decorator.'''


@wrapper
def sort_phone(l):
    print '\n'.join(sorted(l))


if __name__ == '__main__':
    l = [raw_input() for _ in range(int(input()))]
    sort_phone(l)
