from django.db import models

class ATM(models.Model):
    balance = models.FloatField(default=1000.0)
    pin = models.CharField(max_length=4, default="1234")

    def authenticate(self, entered_pin):
        return entered_pin == self.pin

    def withdraw(self, amount):
        if amount > self.balance:
            return "Insufficient balance"
        self.balance -= amount
        self.save()
        return f"Withdrawn ${amount}. Balance: ${self.balance}"

    def deposit(self, amount):
        self.balance += amount
        self.save()
        return f"Deposited ${amount}. Balance: ${self.balance}"