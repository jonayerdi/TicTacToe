
var $header_turn;
var $board_area;
var boardUpdateIntervalID;

//Sets the board to the values of data
function setBoard(data) {
	var countBlank = 0;
	var countX = 0;
	var win = 0;
	for(var i = 0 ; i < 36 ; i++) {
		var value;
		var $square = $('#s'+i+'');
		switch (data[i]) {
			case 'X':
				value='X';
				countX++;
				$square.addClass("squareX");
			break;
			case 'O':
				value='O';
				countX--;
				$square.addClass("squareO");
			break;
			case 'x':
				value='X';
				win=1;
				$square.addClass("squareXWin");
			break;
			case 'o':
				value='O';
				win=2;
				$square.addClass("squareOWin");
			break;
			default:
				value='';
				countBlank++;
			break;
		}
		$square.html(value);
	}
	if(win>0) {
		if(win===1) $header_turn.html(user1+"(<span class='squareX'>X</span>) wins");
		else $header_turn.html(user2+"(<span class='squareO'>O</span>) wins");
	}
	else {
		if(countBlank==0) $header_turn.html("Stalemate");
		else if(countX<=0) $header_turn.html(user1+"(<span class='squareX'>X</span>)'s turn");
		else $header_turn.html(user2+"(<span class='squareO'>O</span>)'s turn");
	}
}

//AJAX request to update board state
function updateBoard() {
	$.ajax({
		url: '/get_board_state/'+game_id+'/',
		success: function(data) {
			setBoard(data);
		},
		failure: function(data) { 
			
		}
	}); 
}

//Called when the user clicks a cell from the board
function cell_clicked(n) {
	$.ajax({
		url: '/change_board_state/'+game_id+'/'+n+'/',
		type: 'post',
		success: function(data) {
			setBoard(data);
		},
		failure: function(data) { 
			
		}
	}); 
}

//Builds the board table
function buildBoard() {
	var device_width = (window.innerWidth > 0) ? window.innerWidth : screen.width;
	var device_height = (window.innerHeight > 0) ? window.innerHeight : screen.height;
	var size = (device_width > device_height) ? (device_height-100)/6 : (device_width-100)/6;
	$board_area.empty();
	$board_area.append("<table class=\"board-table\"></table>");
	var $board_table = $(".board-table");
	for(var i = 0 ; i < 6 ; i++) {
		$board_table.append("<tr id=\"row"+i+"\" height='"+size+"' width='"+size+"'></tr>");
		var $board_row = $("#row"+i);
		for(var j = 0 ; j < 6 ; j++) {
			$board_row.append("<td onclick=\"cell_clicked("+((6*i)+j)+")\" id=\"s"+((6*i)+j)+"\" height='"+size
			+"' width='"+size+"' style=\"font-size:"+size/2+"px;\"></td>");
		}
	}
}

//Wait till all is loaded
$(document).ready(function() {
	//Get jQuery variables
	$header_turn = $('#header_turn');
	$board_area = $('#board_area');
	//Build the board
	buildBoard();
	updateBoard();
	//Set interval for board update
	boardUpdateIntervalID = setInterval(function(){updateBoard()}, 1000);
});