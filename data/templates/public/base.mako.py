# -*- encoding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 5
_modified_time = 1326310394.3621731
_template_filename=u'/home/stingyasian/stingyasian/stingyasian/templates/public/base.mako'
_template_uri=u'/public/base.mako'
_template_cache=cache.Cache(__name__, _modified_time)
_source_encoding='utf-8'
from webhelpers.html import escape
_exports = ['footer']


def render_body(context,**pageargs):
    context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        self = context.get('self', UNDEFINED)
        __M_writer = context.writer()
        # SOURCE LINE 2
        __M_writer(u'<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN"\n"http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">\n<html>\n\n<head>\n  <meta http-equiv="content-type" content="text/html; charset=UTF-8">\n  <!--\n  <script src="http://www.google.com/jsapi"></script>\n  <script>\n    // Load common libraries from Google\n    google.load("jquery", "1.4.2");\n    google.load("jqueryui", "1.8.5");\n  </script>\n  -->\n\n  <script type="text/javascript">\n\n  var _gaq = _gaq || [];\n  _gaq.push([\'_setAccount\', \'UA-19762144-1\']);\n  _gaq.push([\'_trackPageview\']);\n\n  (function() {\n    var ga = document.createElement(\'script\'); ga.type = \'text/javascript\'; ga.async = true;\n    ga.src = (\'https:\' == document.location.protocol ? \'https://ssl\' : \'http://www\') + \'.google-analytics.com/ga.js\';\n    var s = document.getElementsByTagName(\'script\')[0]; s.parentNode.insertBefore(ga, s);\n  })();\n\n  </script>\n\n  <link rel="stylesheet" href="css/reset.css" type="text/css"/>\n  ')
        # SOURCE LINE 32
        __M_writer(escape(self.headtags()))
        __M_writer(u'\n</head>\n\n')
        # SOURCE LINE 36
        __M_writer(u'\n\n\n\n\n<body>\n\n  <div class="wrapper">\n\n  <div id="fb-root"></div>\n  <script>\n  window.fbAsyncInit = function() {\n    FB.init({appId: \'your app id\', status: true, cookie: true,\n             xfbml: true});\n  };\n  (function() {\n    var e = document.createElement(\'script\'); e.async = true;\n    e.src = document.location.protocol +\n      \'//connect.facebook.net/en_US/all.js\';\n    document.getElementById(\'fb-root\').appendChild(e);\n  }());\n  </script>\n\n  <div class="push"></div>\n\n  ')
        # SOURCE LINE 61
        __M_writer(escape(self.body()))
        __M_writer(u'\n\n<script type="text/javascript"><!--\ngoogle_ad_client = "ca-pub-4024152477560029";\n/* Markers on a map */\ngoogle_ad_slot = "5556366285";\ngoogle_ad_width = 728;\ngoogle_ad_height = 90;\n//-->\n</script>\n<!--\n<script type="text/javascript" src="http://pagead2.googlesyndication.com/pagead/show_ads.js">\n-->\n</script>\n\n</div>\n\n\n\n  <div class="footer">\n    ')
        # SOURCE LINE 81
        __M_writer(escape(self.footer()))
        __M_writer(u'\n  </div>\n\n  <!-- We are not encouraging illegal activities nor amoral choices.  After all, we are relieving our angst. -->\n</body>\n\n</html>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_footer(context):
    context.caller_stack._push_frame()
    try:
        __M_writer = context.writer()
        # SOURCE LINE 35
        __M_writer(u'\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


