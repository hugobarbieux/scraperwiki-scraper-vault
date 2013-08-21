<!DOCTYPE html>
<html>
    <head>
        <title>PSMSL Tide Gauge Locations</title>
        <meta name="viewport" content="width=device-width, initial-scale=1.0, user-scalable=no">
        <meta charset="UTF-8">
        <style type="text/css">
            html, body, #map_canvas {
                margin: 0;
                padding: 0;
                height: 100%;
            }
        </style>
        <script type="text/javascript" src="https://maps.googleapis.com/maps/api/js?sensor=false"></script>
        <script type="text/javascript" src="https://ajax.googleapis.com/ajax/libs/jquery/1.7/jquery.min.js"></script>
        <script type="text/javascript">
            var map;
            $(function(){
                var myOptions = {
                    zoom: 7,
                    center: new google.maps.LatLng(53.405092, -2.969876),
                    mapTypeId: google.maps.MapTypeId.ROADMAP
                };
                map = new google.maps.Map(document.getElementById('map_canvas'), myOptions);
            });
        </script>
<script type="text/javascript">           
    var map;
    $(function(){
        var myOptions = {
            zoom: 10,
            center: new google.maps.LatLng(0, 0),
            mapTypeId: google.maps.MapTypeId.ROADMAP
        };
        map = new google.maps.Map(document.getElementById('map_canvas'), myOptions);
        $.ajax({
            url: 'https://api.scraperwiki.com/api/1.0/datastore/sqlite?format=jsondict&name=psmsl_tide_gauge_locations&query=select%20lat%2Clon%20from%20%60swdata%60%20limit%2010',
            dataType: 'json',
            success: function(data){ drop_markers(data); }
        });
        function drop_markers(data){
            bounds = new google.maps.LatLngBounds();
            for(i = 0; i < data.length; i++){
                myLatLng = new google.maps.LatLng(data[i].latitude, data[i].longitude);
                markerOptions = {position: myLatLng, map: map, title: data[i].name};
                new google.maps.Marker(markerOptions);
                bounds.extend(myLatLng);
                map.fitBounds(bounds);
            }
        }
    });
</script>
    </head>
    <body>
        <div id="map_canvas"></div>
    </body>
<html>