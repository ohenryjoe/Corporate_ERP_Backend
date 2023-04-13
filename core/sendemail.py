from django.core.mail import send_mail

# send_mail(
#     'Subject here',
#     'Here is the message.',
#     'from@example.com',
#     ['to@example.com'],
#     fail_silently=False,
# )

def new_user_created(new_user):
    send_mail(
        'WELCOME TO UNEB',
        'A NEW USER WAS CREATED WITH THIS EMAIL ADDRESS',
        'ohenryjoe@gmail.com',
        ['julian.okello@gmail.com'],
        fail_silently=False,
    )
    
