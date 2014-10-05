<!DOCTYPE html>
<head>
<meta http-equiv="Content-Type" content="text/html; charset=utf-8" />
<link href="/static/css/bower-deps.min.css" rel="stylesheet" />
<link href="/static/css/site.css" rel="stylesheet" />
</head>

<body ng-app="netherApp">

<div class="jumbotron background img-responsive">
    <div class="container">
        <div class="row">


<ul  class="list-unstyled">
% if request_type == 'bills':
% for result in feed:
    <blockquote><li><embed width="500" height="400" name="plugin" src="${result['last_version']['urls']['pdf']}" type="text/pdf"></li></blockquote>
    <br/>
% endfor
% elif request_type == 'news':
% for result in feed:
    <blockquote><li>${result['summary_detail']['value']}</li></blockquote>
% endfor
% endif
</ul>



        </div>
    </div>
</div>

<%include file="scripts.mak"/>
<%include file="footer.mak"/>

</body>
