from flask_mail import Mail

def mail_config(mail_routes):
    mail_routes.config['MAIL_SERVER']='smtp.mailtrap.io'
    mail_routes.config['MAIL_PORT'] = 2525
    mail_routes.config['MAIL_USERNAME'] = '9e5ea2f8051c1c'
    mail_routes.config['MAIL_PASSWORD'] = 'f95843dfc60972'
    mail_routes.config['MAIL_USE_TLS'] = True
    mail_routes.config['MAIL_USE_SSL'] = False
    return Mail(mail_routes)
