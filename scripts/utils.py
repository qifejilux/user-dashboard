import logging
import os

# Set up logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def validate_email(email: str) -> bool:
    """Check if an email address is valid."""
    import re
    email_regex = r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"
    if re.match(email_regex, email):
        return True
    return False

def is_uuid(uuid: str) -> bool:
    """Check if a string is a valid UUID."""
    import re
    uuid_regex = r"^[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}$"
    if re.match(uuid_regex, uuid):
        return True
    return False

def get_user_data(id: int) -> dict:
    """Retrieve user data from a database."""
    # Replace this with your actual database query
    data = {
        "id": 1,
        "name": "John Doe",
        "email": "johndoe@example.com"
    }
    return data

def send_email(subject: str, message: str, recipient: str) -> None:
    """Send an email to a recipient."""
    # Replace this with your actual email sending code
    import smtplib
    from email.mime.multipart import MIMEMultipart
    from email.mime.text import MIMEText

    msg = MIMEMultipart()
    msg['From'] = 'your-email@gmail.com'
    msg['To'] = recipient
    msg['Subject'] = subject

    body = message
    msg.attach(MIMEText(body, 'plain'))

    try:
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login(msg['From'], 'your-password')
        text = msg.as_string()
        server.sendmail(msg['From'], msg['To'], text)
        server.quit()
        logger.info('Email sent successfully')
    except Exception as e:
        logger.error(f'Failed to send email: {e}')

def clean_data(data: dict) -> dict:
    """Remove unnecessary keys from the input data."""
    # Remove keys that start with '__'
    cleaned_data = {key: value for key, value in data.items() if not key.startswith('__')}
    return cleaned_data