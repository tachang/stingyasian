# -*- encoding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 5
_modified_time = 1295859789.3643911
_template_filename='/home/stingyasian/stingyasian/stingyasian/templates/public/ideaform.html'
_template_uri='/public/ideaform.html'
_template_cache=cache.Cache(__name__, _modified_time)
_source_encoding='utf-8'
from webhelpers.html import escape
_exports = ['headtags']


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
        __M_writer = context.writer()
        # SOURCE LINE 2
        __M_writer(u'\n\n')
        # SOURCE LINE 51
        __M_writer(u'\n\n<div class="container">\n\n<div class="header-padding"></div>\n\n<div class="heading-1">\n  Think you have what it takes to be a stingy asian?\n</div>\n\n<form name="ideaform" method="POST">\n\n<table class="standard-form">\n<tbody class="standard-form-body">\n\n<tr style="height: 100px;">\n  <td class="form-label">Name:</td>\n  <td class="form-input"><input id="name" type="text" name="name"/></td>\n  <td id="name-formstatus" class="field-status">&nbsp;</td>\n</tr>\n<tr>\n  <td class="form-label">E-mail:</td>\n  <td class="form-input"><input id="email" type="text" name="email"/></td>\n  <td id="email-formstatus" class="field-status"></td>\n</tr>\n<tr>\n  <td class="form-label">Your Stingy Idea:</td>\n  <td class="form-input"><textarea rows="4" cols="35" id="idea" name="idea"></textarea></td>\n  <td id="idea-formstatus" class="field-status"></td>\n</tr>\n\n<tr>\n  <td></td>\n  <td class="form-input">\n    <a href="#" onclick="document.ideaform.submit();"><div class="awesome">Submit This Shit</div></a>\n  </td>\n</tr>\n\n</tbody>\n\n</table>\n</form>\n\n<br/>\n\n<div class="textstyle-2">\n<p>\nMake the cut and we\'ll let you know. By giving us your e-mail we will send you whatever the fuck we want,\nwhenever we want.*\n</p>\n\n</div>\n\n<div class="footnote">\n  *Of course you can unsubscribe but remember what happened to Cynthia when she tried that. We don\'t talk about Cynthia.\n</div>\n\n</div>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_headtags(context):
    context.caller_stack._push_frame()
    try:
        __M_writer = context.writer()
        # SOURCE LINE 4
        __M_writer(u'\n  <title>A stingy asian\'s words of wisdom</title>\n\n  <script src="http://www.google.com/jsapi"></script>\n  <script>\n    // Load common libraries from Google\n    google.load("jquery", "1.4.2");\n    google.load("jqueryui", "1.8.5");\n  </script>\n  <script src="/js/livevalidation_standalone.compressed.js"></script>\n  <link rel="stylesheet" href="css/default.css" type="text/css"/>\n\n<script type="text/javascript">\n\n\nfunction customOnValid() {\n  var target_element = $( "#" + this.element.name + "-formstatus" );\n  target_element.text( this.message );\n  target_element.removeClass("field-invalid");\n  target_element.addClass("field-valid");\n}\n\nfunction customOnInvalid() {\n  var target_element = $( "#" + this.element.name + "-formstatus" );\n  target_element.text( this.message );\n  target_element.removeClass("field-valid");\n  target_element.addClass("field-invalid");\n}\n\n$(document).ready(function()\n{\n  var nameValidation = new LiveValidation(\'name\', { validMessage: " ", onInvalid: customOnInvalid, onValid: customOnValid } );\n  nameValidation.add( Validate.Presence, { failureMessage: "You forgot something you idiot." } );\n\n  var emailValidation = new LiveValidation(\'email\', { validMessage: " ", onInvalid: customOnInvalid, onValid: customOnValid } );\n  emailValidation.add( Validate.Presence, { failureMessage: "Wrong!" } );\n  emailValidation.add( Validate.Email, { failureMessage: "Wrong!" } );\n\n  var ideaValidation = new LiveValidation(\'idea\', { validMessage: " ", onInvalid: customOnInvalid, onValid: customOnValid } );\n  ideaValidation.add( Validate.Presence, { failureMessage: "Enter the damn idea." } );\n\n});\n\n\n\n</script>\n\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


