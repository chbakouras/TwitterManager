import tweepy
from django.contrib.auth.models import User
from django.core.management.base import BaseCommand

from apps.manager.models import Friend
from apps.synchronize_commands.utils import get_api


class Command(BaseCommand):

    help = 'Synchronize twitter friends'

    def add_arguments(self, parser):
        parser.add_argument('user_id')

    def handle(self, *args, **options):
        user_id = options['user_id']

        try:
            user = User.objects.get(id=user_id)

            self.stdout.write(self.style.SUCCESS('Found user ' + user.first_name + ' ' + user.last_name))

            api = get_api(user)
            me = api.me()

            self.stdout.write(self.style.SUCCESS('Start synchronization...'))

            for twitterFriend in tweepy.Cursor(api.friends).items():
                friend = Friend(
                    twitter_id=twitterFriend.id,
                    profile_image_url=twitterFriend.profile_image_url,
                    screen_name=twitterFriend.screen_name,
                    user=user
                )

                self.stdout.write(self.style.SUCCESS('Friend found (' + friend.screen_name + ')'))

                friendships = api.show_friendship(source_id=twitterFriend.id, target_id=me.id)
                for friendship in friendships:
                    if friendship.id == twitterFriend.id:
                        friend.following_back = friendship.following
                        if friendship.following:
                            self.stdout.write(self.style.SUCCESS(friend.screen_name + ' follow you back'))

                existing_friend = Friend.objects.filter(twitter_id=friend.twitter_id)

                if existing_friend:
                    existing_friend.update(
                        twitter_id=friend.twitter_id,
                        profile_image_url=friend.profile_image_url,
                        screen_name=friend.screen_name,
                        following_back=friend.following_back
                    )
                    self.stdout.write(self.style.SUCCESS(friend.screen_name + ' already persisted'))
                    self.stdout.write(self.style.SUCCESS('Updated'))
                else:
                    friend.save()
                    self.stdout.write(self.style.SUCCESS('Created'))
        except User.DoesNotExist:
            self.stdout.write(self.style.ERROR('User with id ' + user_id + ' does not exist'))
