from django.db import models
from django.contrib.auth.models import User
import random
from datetime import datetime, timedelta
from django.utils import timezone

# Create your models here.

class OTP(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    otp_code = models.CharField(max_length=6)
    created_at = models.DateTimeField(auto_now_add=True)
    expires_at = models.DateTimeField()
    
    def __str__(self):
        return f"{self.user.username} - {self.otp_code}"
    
    @classmethod
    def generate_otp(cls, user):
        # Delete any existing OTPs for this user
        cls.objects.filter(user=user).delete()
        
        # Generate a random 6-digit OTP
        otp_code = ''.join([str(random.randint(0, 9)) for _ in range(6)])
        
        # Set expiry to 15 minutes from now
        expires_at = timezone.now() + timedelta(minutes=15)
        
        # Create and return the OTP object
        otp = cls.objects.create(
            user=user, 
            otp_code=otp_code,
            expires_at=expires_at
        )
        return otp
    
    def is_valid(self):
        # Check if OTP is still valid (not expired)
        return timezone.now() < self.expires_at
