
import smtplib as stl
import mimetypes as mt

from email import policy
from email.message import EmailMessage
from email.header import Header


SERVER_INFO = {
    'Google': {
        'SMTP': {
            'Host': 'smtp.gmail.com',
            'Port': {
                'SSL': 465,
                'TSL': 587,
                'STARTTSL': 587
            }
        },
        'IMAP': {
            'Host': 'imap.gmail.com',
            'Port': 993
        }
    }
}


class EmailAccount:

    address = None
    password = None

    @classmethod
    def set_account(cls, address, password):
        cls.address = address
        cls.password = password


class Email:

    def __init__(
        self,
        host, port,
        is_tsl=False, is_ssl=False,
        **params
    ):
        self.host = host
        self.port = port
        self.is_tsl = is_tsl
        self.is_ssl = is_ssl

        self.email = EmailMessage(policy=policy.SMTP)

        self.Subject = params.get('Subject')
        self.From = params.get('From')
        self.To = params.get('To')
        self.Preamble = params.get('Preamble', '흔한 찐따의 이메일')
        self.Message = params.get('Message')


    @property
    def address(self):
        return EmailAccount.address
    @address.setter
    def address(self, address):
        EmailAccount.address = address

    @property
    def password(self):
        return EmailAccount.password
    @password.setter
    def password(self, password):
        EmailAccount.password = password

    @property
    def host(self):
        return self._host
    @host.setter
    def host(self, host):
        self._host = host

    @property
    def port(self):
        return self._port
    @port.setter
    def port(self, port):
        self._port = port

    @property
    def is_tsl(self):
        return self._is_tsl
    @is_tsl.setter
    def is_tsl(self, is_tsl):
        self._is_tsl = is_tsl

    @property
    def is_ssl(self):
        return self._is_ssl
    @is_ssl.setter
    def is_ssl(self, is_ssl):
        self._is_ssl = is_ssl

    @property
    def Subject(self):
        return self.email.get('Subject')
    @Subject.setter
    def Subject(self, subject):
        if subject is not None:
            self.email['Subject'] = subject

    @property
    def From(self):
        return self.email.get('From')
    @From.setter
    def From(self, _from):
        if _from is not None:
            self.email['From'] = _from

    @property
    def To(self):
        return self.email.get('To')
    @To.setter
    def To(self, to):
        if to is not None:
            self.email['To'] = to

    @property
    def Preamble(self):
        return self._preamble
    @Preamble.setter
    def Preamble(self, preamble):
        self._preamble = preamble

    @property
    def Message(self):
        return self._message
    @Message.setter
    def Message(self, message):
        print(type(message))
        print(message)
        print(repr(message))
        self._message = message
        if message is not None:
            self.email.set_content(message)

    @property
    def email(self):
        return self._email
    @email.setter
    def email(self, email):
        self._email = email


    def login(self):
        if self.is_ssl:
            smtp = stl.SMTP_SSL(self.host, self.port)
            print(smtp)
        else:
            smtp = stl.SMTP(self.host, self.port)

        if self.is_tsl:
            self.ehlo = smtp.ehlo()
            self.starttls = smtp.starttls()

        smtp.login(self.address, self.password)
        return smtp


    def send(self):
        smtp = self.login()
        smtp.send_message(self.email, mail_options=['SMTPUTF8'])
        smtp.quit()


    def attach(self, filename):
        maintype, subtype = self._get_mimetypes(filename)
        with open(filename, 'rb') as file:
            data = file.read()
            self.email.add_attachment(
                data,
                maintype=maintype,
                subtype=subtype,
                filename=filename.split('/')[-1]
            )
            return filename


    def _get_mimetypes(self, filename):
        ctype, encoding = mt.guess_type(filename)
        if ctype is None or encoding is not None:
            ctype = 'application/octet-stream'
        maintype, subtype = ctype.split('/', 1)
        return maintype, subtype

