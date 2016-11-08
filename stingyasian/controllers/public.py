import logging
import random

from pylons import request, response, session, tmpl_context as c, url
from pylons.controllers.util import abort, redirect

from stingyasian.lib.base import BaseController, render

log = logging.getLogger(__name__)

class PublicController(BaseController):

  def index(self):

    if( 'tidbit_ids' not in session ):
      session['tidbit_ids'] = []
      session.save()

    f = open('/home/stingyasian/stingyasian/tidbits.txt', 'r')
    tidbits = f.readlines()

    # Case where person has seen all tidbits
    if( len(session['tidbit_ids']) == len(tidbits) ):
      session['tidbit_ids'] = []
      session.save()

    index = random.randint(0, len(tidbits)-1 )
    while( index in session['tidbit_ids'] ):
      index = random.randint(0, len(tidbits)-1 )

    c.tidbit = tidbits[index]
    session['tidbit_ids'].append(index)
    session.save()

    return render('/public/index.html')



  def index2(self):

    if( 'tidbit_ids' not in session ):
      session['tidbit_ids'] = []
      session.save()

    f = open('/home/stingyasian/stingyasian/tidbits.txt', 'r')
    tidbits = f.readlines()

    # Case where person has seen all tidbits
    if( len(session['tidbit_ids']) == len(tidbits) ):
      session['tidbit_ids'] = []
      session.save()

    index = random.randint(0, len(tidbits)-1 )
    while( index in session['tidbit_ids'] ):
      index = random.randint(0, len(tidbits)-1 )

    c.tidbit = tidbits[index]
    session['tidbit_ids'].append(index)
    session.save()

    return render('/public/index2.html')
