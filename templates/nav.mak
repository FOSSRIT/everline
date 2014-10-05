<ul class="nav nav-pills noclear" style="clear:none;">
  <li><a href="#home" role="tab" data-toggle="pill">home</a></li>
  <li><a href="#about" role="tab" data-toggle="pill">about</a></li>
  <li><a href="#timeline" role="tab" data-toggle="pill">timeline</a></li>
</ul>

<p class="pull-right">Logged into Evernote as ${username}</p>

<div class="tab-content">
    <div class="tab-pane fade" id="home">
        <p>home</p>
    </div>
    <div class="tab-pane fade" id="about">
        <h1>About</h1>
        <p>AYO DECAUSE, WRITE SOME COOL SHIT ABOUT HOW THIS APP IS COOL N SHIT</p>
    </div>
    <div class="tab-pane fade in active" id="timeline">
        <%include file="timeline.mak" />
    </div>
</div>
