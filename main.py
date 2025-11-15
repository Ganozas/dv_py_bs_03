import smtplib
import os
from dotenv import load_dotenv

mail=('''
Привет, %friend_name%! %my_name% приглашает тебя на сайт %website%!

%website% — это новая версия онлайн-курса по программированию. 
Изучаем Python и не только. Решаем задачи. Получаем ревью от преподавателя. 

Как будет проходить ваше обучение на %website%? 

→ Попрактикуешься на реальных кейсах. 
Задачи от тимлидов со стажем от 10 лет в программировании.
→ Будешь учиться без стресса и бессонных ночей. 
Задачи не «сгорят» и не уйдут к другому. Занимайся в удобное время и ровно столько, сколько можешь.
→ Подготовишь крепкое резюме.
Все проекты — они же решение наших задачек — можно разместить на твоём GitHub. Работодатели такое оценят. 

Регистрируйся → %website%  
На курсы, которые еще не вышли, можно подписаться и получить уведомление о релизе сразу на имейл.
	''')
frend_name='Ирина'
my_name='Алексей'
website='https://dvmn.org/profession-ref-program/lsamsonov2013/r6PIz/'

mail=(mail.replace('%website%',website))
mail=(mail.replace('%friend_name%',frend_name))
mail=(mail.replace('%my_name%',my_name))

latter='''
From:leha.samsonov.2000@mail.ru
To:666ren12qaz@gmail.com
Subject:Приглашение
Content-Type:text/plain; charset="UTF-8";
	'''
latter=latter + mail
latter=latter.encode("UTF-8")

load_dotenv()
LOGIN=os.getenv('LOGIN')
PASSVORD=os.getenv('PASSVORD')

server=smtplib.SMTP_SSL('smtp.mail.ru',465)
server.login(LOGIN,PASSVORD)
server.sendmail('leha.samsonov.2000@mail.ru','leha.samsonov.2000@mail.ru',latter)
server.quit()
