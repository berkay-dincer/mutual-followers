import tweepy
import argparse


def friends_to_set(screen_name):
    s = set()
    for friend in tweepy.Cursor(api.friends, screen_name=screen_name, count=200).items():
        s.add(';'.join([friend.screen_name, friend.name, friend.description]))
    return s


def remove_ugly_characters(mutual_friend_str):
    mutual_friend_str = mutual_friend_str.strip()
    mutual_friend_str = mutual_friend_str.rstrip()
    mutual_friend_str = mutual_friend_str.replace('\n', '')
    mutual_friend_str = mutual_friend_str.replace('\t', '')
    return mutual_friend_str


# Instantiate the parser
parser = argparse.ArgumentParser(description='mutual-followers')

parser.add_argument('--consumer_key', type=str, help='twitter consumer key', required=True)
parser.add_argument('--consumer_secret', type=str, help='twitter consumer secret', required=True)
parser.add_argument('--access_token', type=str, help='twitter access token', required=True)
parser.add_argument('--access_token_secret', type=str, help='twitter access token secret', required=True)

parser.add_argument('--users', type=str, help='users to see mutual friends', required=True)

args = parser.parse_args()

auth = tweepy.OAuthHandler(args.consumer_key, args.consumer_secret)
auth.set_access_token(args.access_token, args.access_token_secret)

api = tweepy.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True)

users = args.users.split(',')

friends_set = friends_to_set(users[0])
del users[0]

for user in users:
    next_friends = friends_to_set(user)
    friends_set = friends_set.intersection(next_friends)

print('Mutual friend count:' + str(len(friends_set)))

for mutual_friend in friends_set:
    mutual_friend = remove_ugly_characters(mutual_friend)
    mutual_friend_split = mutual_friend.split(';')
    pretty_str = '@' + mutual_friend_split[0] + ' // ' + mutual_friend_split[1] + ' // ' + mutual_friend_split[2]
    print(pretty_str)
