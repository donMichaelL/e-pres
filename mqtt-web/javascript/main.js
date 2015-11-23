(function() {


		var chart = new CanvasJS.Chart("chartContainer", { 
		title: {
			text: "Adding & Updating dataPoints"
		},
		data: [
		{
			type: "spline",
			dataPoints: [
			]
		}
		]
	});
	chart.render();	

	// var btnConnect = document.querySelector('.btn-connect');
	// var btnSubscribe = document.querySelector('.btn-subscribe');
	// var messages = document.querySelector('.messages');

	// btnConnect.addEventListener('click', function(e) {
	// e.preventDefault();
	// client = mows.createClient('ws://127.0.0.1:1882');
	// appendMessage('connection open :)');
	// client.on('message', function (topic, message) {
	// 	console.log(message);
	// 	appendMessage(message);
	// });
	// });


	// btnSubscribe.addEventListener('click', function(e) {
	// 	e.preventDefault();
	// 	client && client.subscribe("airsoul");
	// 	appendMessage('subscribe -> ' + "airsoul");
	// });

	//   appendMessage = function(message) {
	//     var element = document.createElement('p');
	//     var string = document.createTextNode(message);
	//     element.appendChild(string);
	//     messages.appendChild(element);
	//   }
client = new Paho.MQTT.Client(host, Number(port), "clientId");

// set callback handlers
client.onConnectionLost = onConnectionLost;
client.onMessageArrived = onMessageArrived;

// connect the client
client.connect({onSuccess:onConnect});


// called when the client connects
function onConnect() {
  // Once a connection has been made, make a subscription and send a message.
  console.log("onConnect");
  client.subscribe(topic);
  message = new Paho.MQTT.Message("The Test message  15 send by HTTP");
  message.destinationName = "World";
  client.send(message); 
}

// called when the client loses its connection
function onConnectionLost(responseObject) {
  if (responseObject.errorCode !== 0) {
    console.log("onConnectionLost:"+responseObject.errorMessage);
  }
}

// called when a message arrives
function onMessageArrived(message) {
  console.log("onMessageArrived: <<"+message.payloadString +">> with topic--> " + message.destinationName);
  var number = message.payloadString.match(/\d+/)[0];
  console.log(number);
  if(number != null)
  	updateGraph(parseInt(number));
}



				function updateGraph(new_value){
					console.log(new_value);
					var length = chart.options.data[0].dataPoints.length;
					chart.options.title.text = "New DataPoint Added at the end";
					chart.options.data[0].dataPoints.push({ y: new_value});
					chart.render();
				};









 })();
