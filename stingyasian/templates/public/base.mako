# -*- coding: utf-8 -*-
<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN"
"http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">
<html>

<head>
  <meta http-equiv="content-type" content="text/html; charset=UTF-8">
  <!--
  <script src="http://www.google.com/jsapi"></script>
  <script>
    // Load common libraries from Google
    google.load("jquery", "1.4.2");
    google.load("jqueryui", "1.8.5");
  </script>
  -->

  <script type="text/javascript">

  var _gaq = _gaq || [];
  _gaq.push(['_setAccount', 'UA-19762144-1']);
  _gaq.push(['_trackPageview']);

  (function() {
    var ga = document.createElement('script'); ga.type = 'text/javascript'; ga.async = true;
    ga.src = ('https:' == document.location.protocol ? 'https://ssl' : 'http://www') + '.google-analytics.com/ga.js';
    var s = document.getElementsByTagName('script')[0]; s.parentNode.insertBefore(ga, s);
  })();

  </script>

  <link rel="stylesheet" href="css/reset.css" type="text/css"/>
  ${self.headtags()}
</head>

<%def name="footer()">
</%def>




<body>

  <div class="wrapper">

  <div id="fb-root"></div>
  <script>
  window.fbAsyncInit = function() {
    FB.init({appId: 'your app id', status: true, cookie: true,
             xfbml: true});
  };
  (function() {
    var e = document.createElement('script'); e.async = true;
    e.src = document.location.protocol +
      '//connect.facebook.net/en_US/all.js';
    document.getElementById('fb-root').appendChild(e);
  }());
  </script>

  <div class="push"></div>

  ${self.body()}

<script type="text/javascript"><!--
google_ad_client = "ca-pub-4024152477560029";
/* Markers on a map */
google_ad_slot = "5556366285";
google_ad_width = 728;
google_ad_height = 90;
//-->
</script>
<!--
<script type="text/javascript" src="http://pagead2.googlesyndication.com/pagead/show_ads.js">
-->
</script>

</div>



  <div class="footer">
    ${self.footer()}
  </div>

  <!-- We are not encouraging illegal activities nor amoral choices.  After all, we are relieving our angst. -->
</body>

</html>
