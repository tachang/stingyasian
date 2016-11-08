import logging

from pylons import request, response, session, tmpl_context as c, url
from pylons.controllers.util import abort, redirect

from stingyasian.lib.base import BaseController, render

import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

log = logging.getLogger(__name__)

class IdeaController(BaseController):

  def idea_form(self):
    return render('/public/ideaform.html')

  def idea_submit(self):

    text = """
    Name: %s
    E-mail: %s
    Idea: %s
    """ % ( request.params['name'], request.params['email'], request.params['idea'] )

    msg = MIMEText( text.encode('utf-8') )
    msg['Subject'] = "A stingy idea"
    msg['From'] = "mailer@stingyasian.com"
    msg['To'] = "jeff.tchang@gmail.com, jenn.ng@gmail.com, atasteofcyn@gmail.com"

    s = smtplib.SMTP('smtp.gmail.com', 587)
    s.ehlo()
    s.starttls()
    s.ehlo()
    s.login('mailer@stingyasian.com','63H325')

    s.sendmail( msg['From'], [ "jeff.tchang@gmail.com", "jenn.ng@gmail.com", "atasteofcyn@gmail.com" ], msg.as_string())
    #s.sendmail( msg['From'], [ "jeff.tchang+nojenncyn@gmail.com" ], msg.as_string())
    s.quit()

    redirect(url(controller='public', action='index'))
