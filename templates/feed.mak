<ul>
% if request_type == 'bills':
% for result in feed:
    <blockquote><li><embed width="500" height="400" name="plugin" src="${result['last_version']['urls']['pdf']}" type="text/pdf"></li></blockquote>
% endfor
% elif request_type == 'news':
% for result in feed:
    <blockquote><li>${result['summary_detail']['value']}</li></blockquote>
% endfor
% endif
</ul>
