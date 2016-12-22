
var $challenge_list;
var user_cache = {};

//Get the username from id
function getUsername(id) {
	if(id in user_cache)
		return user_cache[id];
	else {
		$.ajax({
			url: '/get_username/'+id+'/',
			success: function(data) {
				user_cache[id] = data;
			},
			failure: function(data) { 
				
			}
		}); 
	}
}

//Visualize challenges from JSON
function visualizeChallenges(json) {
	$challenge_list.empty();
	for(var i = 0 ; i < json.length ; i++) {
		var challenge = json[i];
		var pk = challenge["pk"];
		var user1 = getUsername(challenge["fields"]["user1"]);
		var user2 = getUsername(challenge["fields"]["user2"]);
		var user1_turn = challenge["fields"]["user1_turn"];
		if(user1 && user2) {
			//Update view
			var list_item = "";
			list_item += "<li class='list-group-item'>";
			if(user1_turn)
				list_item += "<span class='highlight'>"+user1+"</span> vs "+user2;
			else
				list_item += user1+" vs <span class='highlight'>"+user2+"</span>";
			list_item += "<button type=\"button\" class=\"btn btn-success pull-right\" onclick=\"window.location='/game/"+pk+"';\">PLAY</button></li>";
			$challenge_list.append(list_item);
		}
	}
}

//AJAX request to update challenges list
function updateChallenges() {
	$.ajax({
		url: '/get_challenge_list/'+user+'/',
		success: function(data) {
			var json = eval("(" + data + ")");
			visualizeChallenges(json);
		},
		failure: function(data) { 
			
		}
	}); 
}

//Wait till all is loaded
$(document).ready(function() {
	//Get jQuery variables
	$challenge_list = $('#challenge_list');
	//Set interval for challenges update
	if(user) {
		updateChallenges();
		challengeUpdateIntervalID = setInterval(function(){updateChallenges()}, 3000);
	}
});