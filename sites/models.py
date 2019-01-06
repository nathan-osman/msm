from django.db import models


class Site(models.Model):
    """
    A single website being monitored for uptime
    """

    UNKNOWN = 0
    ONLINE = 2
    OFFLINE = 1

    STATUS_CHOICES = (
        (UNKNOWN, "unknown"),
        (ONLINE, "online"),
        (OFFLINE, "offline"),
    )

    url = models.URLField()
    name = models.CharField(max_length=200)

    poll_interval = models.IntegerField("poll interval in seconds")

    status = models.IntegerField(choices=STATUS_CHOICES, default=UNKNOWN)
    status_time = models.DateTimeField(auto_now_add=True)

    last_poll = models.DateTimeField(null=True, blank=True)
    next_poll = models.DateTimeField(null=True, blank=True)
