print("enter your friends name in your friend listof group a")

group_a = set(input().split())

print("enter your friends name in your friend list group b")

group_b = set(input().split())

common_friends = group_a & group_b

if common_friends:
    print("\ncommon friends:")
    for friend in common_friends:
        print(friend)

    else:
        print("No common friends found.")