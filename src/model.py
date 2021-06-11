import smtplib  # Импортируем библиотеку по работе с SMTP

# Добавляем необходимые подклассы - MIME-типы
from email.mime.multipart import MIMEMultipart  # Многокомпонентный объект
from email.mime.text import MIMEText  # Текст/HTML


# from email.mime.image import MIMEImage              # Изображения
def send_mail(addr_from: str = "shiaz@yandex.ru", addr_to: str = "shiaz@yandex.ru", password: str = "siz035036503530",
              text_msg: str = 'Текст'):
    """
    Отправляет письмо

    :param addr_from: От кого.
    :param addr_to: Кому письмо.
    :param password: Пароль.
    """
    msg = MIMEMultipart()  # Создаем сообщение
    msg['From'] = addr_from  # Адресат
    msg['To'] = addr_to  # Получатель
    msg['Subject'] = 'Тема сообщения'  # Тема сообщения

    text_msg = "Текст сообщения"
    msg.attach(MIMEText(text_msg, 'plain'))  # Добавляем в сообщение текст

    server = smtplib.SMTP_SSL('smtp.yandex.ru', 465)  # Создаем объект SMTP
    # server.set_debuglevel(True)                         # Включаем режим отладки - если отчет не нужен, строку можно закомментировать

    server.ehlo()
    server.login(addr_from, password)
    text = msg.as_string()
    server.sendmail(addr_from, addr_to, text)
    server.quit()