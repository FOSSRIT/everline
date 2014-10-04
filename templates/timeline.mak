<%inherit file="master.mak"/>
    <div id="my-timeline"></div>

    <!-- jQuery -->
    <script type="text/javascript" src="http://ajax.googleapis.com/ajax/libs/jquery/1.7.2/jquery.min.js"></script>
    <!-- BEGIN TimelineJS -->
    <script type="text/javascript" src="http://cdn.knightlab.com/libs/timeline/latest/js/storyjs-embed.js"></script>
    <script>
        $(document).ready(function() {
            createStoryJS({
                type:       'timeline',
                width:      '800',
                height:     '600',
                source:     '/static/data/example_json.json',
                embed_id:   'my-timeline'
            });
        });
    </script>
    <!-- END TimelineJS -->
