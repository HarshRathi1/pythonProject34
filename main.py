english_readers=int(input())
english_readers_id=set(map(int,input().split()))
french_readers=int(input())
french_readers_id=set(map(int,input().split()))
all_ids=english_readers_id.union(french_readers_id)
print(len(all_ids))
