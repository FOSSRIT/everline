<ul class="nav nav-pills noclear" style="clear:none;">
  <li><a href="#home" role="tab" data-toggle="pill">home</a></li>
  <li><a href="#about" role="tab" data-toggle="pill">about</a></li>
  <li><a href="#timeline" role="tab" data-toggle="pill">timeline</a></li>
</ul>

<p class="pull-right ">Logged into Evernote as <span class="label label-green "><a class="text-white" target="_blank" href="http://sandbox.evernote.com">${username}</a></span></p>

<div class="tab-content">
    <div class="tab-pane fade" id="home">
        <p>home</p>
    </div>
    <div class="tab-pane fade" id="about">
        <%include file="preso.mak" />
    </div>
    <div class="tab-pane fade in active" id="timeline">
        <%include file="timeline.mak" />
    </div>
</div>
