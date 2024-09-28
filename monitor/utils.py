# from django.core.mail import EmailMessage
# from django.template.loader import render_to_string
# from django.utils.html import strip_tags
# from django.utils import timezone

# LAST_EARTQUAKE_EMAIL_SENT = None
# LAST_VOLCANO_EMAIL_SENT = None
# LAST_HUMIDITY_EMAIL_SENT = None

# def send_earthquacke_email():
#     global LAST_EARTQUAKE_EMAIL_SENT

#     if not(LAST_EARTQUAKE_EMAIL_SENT and (timezone.now() - LAST_EARTQUAKE_EMAIL_SENT).seconds < 300):
#         email_subject = 'Earthquacke Happening!'
#         email_body = 'Dear Admin, Unfortunately an earthquake is happenning in the environment! Please take the neccessary actions!'
#         email_sender = 'es.natural.disaster@gmail.com'
#         email_recipient = ['77fetrat@gmail.com']

#         email = EmailMessage(
#             email_subject,
#             email_body,
#             email_sender,
#             email_recipient
#         )
#         email.send()

#         LAST_EARTQUAKE_EMAIL_SENT = timezone.now()

# def send_volcano_email():
#     global LAST_VOLCANO_EMAIL_SENT

#     if not(LAST_VOLCANO_EMAIL_SENT and (timezone.now() - LAST_VOLCANO_EMAIL_SENT).seconds < 300):
#         email_subject = 'Volcanoinc Eruptions Detected!'
#         email_body = 'Dear Admin, Unfortunately we have detected volcanic eruptions in the environment! Please take the neccessary actions!'
#         email_sender = 'es.natural.disaster@gmail.com'
#         email_recipient = ['77fetrat@gmail.com']

#         email = EmailMessage(
#             email_subject,
#             email_body,
#             email_sender,
#             email_recipient
#         )
#         email.send()

#         LAST_VOLCANO_EMAIL_SENT = timezone.now()

# def send_humidity_email():
#     global LAST_HUMIDITY_EMAIL_SENT

#     if not(LAST_HUMIDITY_EMAIL_SENT and (timezone.now() - LAST_HUMIDITY_EMAIL_SENT).seconds < 300):
#         email_subject = 'Extreme Humidity!'
#         email_body = 'Dear Admin, Unfortunately the humidity of the environment is so extreme! Please take the neccessary actions!'
#         email_sender = 'es.natural.disaster@gmail.com'
#         email_recipient = ['77fetrat@gmail.com']

#         email = EmailMessage(
#             email_subject,
#             email_body,
#             email_sender,
#             email_recipient
#         )
#         email.send()

#         LAST_HUMIDITY_EMAIL_SENT = timezone.now()
