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
        console.log("UPDATE PLAYERS")
        jQuery.each(data, function(playername) {
       $('#players ul').append(
        $('<li>').append(
            playername+""
        ));


    });

    setTimeout(areNewPlayers, 2000);
    },
    complete: function() {
      // Schedule the next request when the current one's complete
      setTimeout(areNewPlayers, 2000);
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



