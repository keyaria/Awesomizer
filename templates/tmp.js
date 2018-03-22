<script type="text/javascript" charset="utf-8">
      var data = '{{ data|tojson|safe }}'
      var data_converted = JSON.parse("[" + data + "]")[0]
      var re = /[A-Z]{1}\w+ ([A-Z]{1}[a-z]+|TH=\w+-\w+)/g;
      console.log(data_converted)
      $(document).ready(function()
      {
        if (data_converted.length != 0) {
            console.log("Database")
            for (var i = 0; i < data_converted.length; i++) {
              var d = String(data_converted[i][1])
              var authors = d.match(re)

                $( "#Content" ).prepend("<div style='display:inline-flex; height:200px; width: 48%; margin: 1% 1% 1% 1%; border: 1px solid #aabbcc;'> <img style='margin-right:2%;'src=\"" + data_converted[i][3] + " \"><div id=\"" + data_converted[i][2] +
                "-scanned\" style ='display:inline-block;'><i>"
                            + data_converted[i][0] + "</i><br> by: "
                            +  authors +
                              "<br> Times Scanned: " + data_converted[i][4] + "</div> <br /><br /> ");
            }
          }
          namespace = '/awesome'; // change to an empty string to use the global namespace

          // the socket.io documentation recommends sending an explicit package upon connection
          // this is specially important when using the global namespace
          var socket = io.connect('http://' + document.domain + ':' + location.port + namespace);

          // event handler for server sent data
          // the data is displayed in the "Received" section of the page
          socket.on('barcode', function(msg)
          {
              console.log("First time scanned")
              $( "#Content" ).prepend("<div style='float: left'> <img src=\"" + msg.data[3] + " \" style='height:160px; width:120px; display:block; margin-left:20px; margin-top: auto'><div id=\"" + msg.data[2] +
                  "-scanned\" style ='width: 150px; text-align: center; font-size: 15px;'>Times Scanned: " + msg.data[4] + "</div></div>");
          });
          //Recieves updated information
          socket.on('update_data', function(msg)
          {
              console.log(msg.data[0])
              var update= document.getElementById(msg.data[0][2].toString() + "-scanned")
              update.innerHTML = "Times Scanned: " + msg.data[0][4].toString()
          });
      });
  </script>
