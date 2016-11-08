# -*- encoding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 5
_modified_time = 1291359921.5351291
_template_filename='/home/stingyasian/stingyasian/stingyasian/templates/public/index.html'
_template_uri='/public/index.html'
_template_cache=cache.Cache(__name__, _modified_time)
_source_encoding='utf-8'
from webhelpers.html import escape
_exports = ['headtags', 'footer']


def _mako_get_namespace(context, name):
    try:
        return context.namespaces[(__name__, name)]
    except KeyError:
        _mako_generate_namespaces(context)
        return context.namespaces[(__name__, name)]
def _mako_generate_namespaces(context):
    pass
def _mako_inherit(template, context):
    _mako_generate_namespaces(context)
    return runtime._inherit_from(context, u'base.mako', _template_uri)
def render_body(context,**pageargs):
    context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        c = context.get('c', UNDEFINED)
        __M_writer = context.writer()
        # SOURCE LINE 2
        __M_writer(u'\n\n')
        # SOURCE LINE 8
        __M_writer(u'\n\n')
        # SOURCE LINE 18
        __M_writer(u'\n\n\n\n<div id="tidbit">\n  ')
        # SOURCE LINE 23
        __M_writer(escape(c.tidbit))
        __M_writer(u'\n  <a href="/">\n    <div id="refresh-page-link" class="heading-2 link">>> That\'s not stingy enough for me.</div>\n  </a>\n\n  <div style="min-height: 100px;">\n  <div class="facebook-container">\n  <script src="http://connect.facebook.net/en_US/all.js#xfbml=1"></script><fb:like href="http://www.stingyasian.com/" font="tahoma"></fb:like>\n  </div>\n\n  <div class="twitter-container">\n  Tweet this shit:<br/>\n\n  <br/>\n  <a href="http://twitter.com/share" class="twitter-share-button" data-text="#stingyasian" data-count="horizontal">Tweet</a><script type="text/javascript" src="http://platform.twitter.com/widgets.js"></script>\n  </div>\n\n  </div>\n\n</div>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_headtags(context):
    context.caller_stack._push_frame()
    try:
        __M_writer = context.writer()
        # SOURCE LINE 4
        __M_writer(u'\n  <title>A stingy asian\'s words of wisdom</title>\n  <link rel="stylesheet" href="css/default.css" type="text/css"/>\n\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_footer(context):
    context.caller_stack._push_frame()
    try:
        __M_writer = context.writer()
        # SOURCE LINE 10
        __M_writer(u'\n\n   <p>\n   Made by two <a href="http://of.jennism.com/">stingy</a>\n   <a href="http://returnbooleantrue.blogspot.com/">asians</a>.\n\n   Think you can be <a href="/stingyideas">more stingy</a>?\n   </p>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


