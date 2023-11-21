a = set(input().split())
b = set(input().split())

result = sorted(list(a & b))
print(' '.join(result))