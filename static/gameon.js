/**
 * Created by tugrulz on 05.08.2016.
 */

var url = "localhost:5000";
var gamename = "ahmet"; // bad programming, should be changed with the variable afterwards //

function isVotingFinished() {
    var dontcallmeagain = false;
  $.ajax({

    url: "finalDecision/"+gamename,
    success: function(data) {
        console.log("VOTING CHECK");
      if(data != "Negative") {
         //window.location.href = data
          $("#revealed-agent").removeClass('hidden');
          dontcallmeagain = true;
      }
    },
    complete: function() {
      // Schedule the next request when the current one's complete
        if(dontcallmeagain == false)
            setTimeout(isGameOn, 1000);
    }
  });
}

