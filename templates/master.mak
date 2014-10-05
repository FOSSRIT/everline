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
            ${self.body()}
            <%include file="nav.mak" />
        </div>
    </div>
</div>

<%include file="scripts.mak"/>
<%include file="footer.mak"/>

</body>
