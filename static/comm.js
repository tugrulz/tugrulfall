/**
 * Created by tugrulz on 30.07.2016.
 */

var url = "localhost:5000";
var gamename = "ahmet"; // bad programming, should be changed with the variable afterwards //

(function isGameOn() {
  $.ajax({
    url: "startgame/"+gamename,
    success: function(data) {
        console.log("GAME STARTED");
      if(data != "Negative") {
         //window.location.href = data
          document.open();
            document.write(data);
            document.close();
      }
    },
    complete: function() {
      // Schedule the next request when the current one's complete
      setTimeout(isGameOn, 1000);
    }
  });
})();

(function areNewPlayers() {
  $.ajax({
    url: "updateLobby/"+gamename,
    success: function(data) {
        console.log("UPDATE PLAYERS");
        console.log(data);
        var players = JSON.parse(data);
        //data = $.parseJSON(data);
        // console.log("Parsed: " + data);
        console.log(typeof (players));
        console.log(typeof(players[0]))
        //players = data.substring(2,data.length - 2).split('/",/"');
        $('#players ul').html('');
        jQuery.each(players, function(index, playername) {
       $('#players ul').append(
        $('<li>').append(
            playername+""
        ));


    });

    //setTimeout(areNewPlayers, 3000);
    },
    complete: function() {
      // Schedule the next request when the current one's complete
      setTimeout(areNewPlayers, 3000);
    }
  });
})();


/*$( "#newGame" ).click(function() {
  alert( "New game is establishing." );
    $.post(url,
    {
        //request: "newGame",
        name: "Admin",
    },
    function(data, status){
        alert("Data: " + data + "\nStatus: " + status);
    });
});


$( "#newGame" ).click(function() {
  alert( "New game is establishing." );
});?/*/



