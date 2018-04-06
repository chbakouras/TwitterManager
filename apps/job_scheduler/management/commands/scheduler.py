from django.conf import settings
from django.core.management import call_command
from django.core.management.base import BaseCommand

from apps.job_scheduler.models import Job


class Command(BaseCommand):
    help = 'Consumes synchronization jobs'

    def handle(self, *args, **options):
        jobs = Job.objects \
            .filter(finished=False) \
            .filter(running=False) \
            .filter(type__exact=settings.SYNCHRONIZE)

        for job in jobs:
            job.running = True
            job.save()

            call_command('synchronize', job.user_id, interactive=False)

            job.running = False
            job.finished = True
            job.save()
