N = int(raw_input())
rooms = map(int, raw_input().split())
uniq_rooms = set(rooms)


room = (sum(uniq_rooms) * N - sum(rooms)) / (N - 1)

print str(room)
