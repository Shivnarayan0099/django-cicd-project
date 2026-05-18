from django.db import models

class TrafficLog(models.Model):
    timestamp = models.DateTimeField(auto_now_add=True)
    junction_id = models.IntegerField()
    hour = models.IntegerField()
    is_weekend = models.BooleanField(default=False)
    weather = models.IntegerField()
    vehicle_count = models.IntegerField()
    prediction_output = models.CharField(max_length=100)
    timer_strategy = models.CharField(max_length=100)

    def __str__(self):
        return f"Log #{self.id} - J{self.junction_id}"