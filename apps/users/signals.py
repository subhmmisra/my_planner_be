

def add_user_full_name(sender, instance, created, **kwargs):
    if created:
        user = instance
        user.full_name = user.get_full_name()
        user.save()