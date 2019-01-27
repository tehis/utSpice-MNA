let selectedItem = 'Battery';
const elements = ['Battery','Current','Capacitor','Resistor','Inductor','OpAmp'];
let nodeCount = 0;
let canvasElements = [];

function renderSidebar(){
	let sidebar = document.getElementById("sidebar");
	for(i in elements){
		sidebar.innerHTML += (`<img src="${"./static/img/" + elements[i] + ".png"}"
								onclick="console.log(selectedItem = '${elements[i]}')"
								class="sidebar-element"
								id="${elements[i]}"
								/>\n`);
	}
}

function parseEquation(str){

}

function createEl(event){
	let coord = { x: event.pageX , y: event.pageY };
	let canvas = document.getElementById("canvas");
	let neg = Number(prompt("Enter the node number connected to the negative/left side of this element"));
	let pos = Number(prompt("Enter the node number connected to the positive/right side of this element"));
	var value, out;
	if(selectedItem != "OpAmp"){
		value = (selectedItem == "Battery" || selectedItem == "Current")?(prompt("Please enter this element's equation in the following format\n(m)<sin/cos>((w)t+θ)")):(Number(prompt("Please enter this element's value")));
	}
	else{
		out = Number(prompt("Please enter the node connected to the output"));
	}
	$.ajaxSetup({
		async: false
	});
	const req = $.ajax({
		type: 'POST',
		contentType:'application/json;charset-utf-08',
		dataType: 'json',
		data:JSON.stringify({
			'type': selectedItem,
			'value': value,
			'neg': neg,
			'pos': pos,
			'out': (selectedItem == 'OpAmp') ? out : -1
		}),
		url:`/addelement/${selectedItem}`,
		success: (data, textStatus, jQxhr)=>{
			if(textStatus == 'success') console.log('successfully sent data and response is: ', data);
			else console.error('data: ', data, '\n jQxhr: ', jQxhr);
		}
	});
	canvasElements.push((selectedItem=="OpAmp")?
	{"type":selectedItem,"points":{"neg":neg,"pos":pos,"out":out},"value":''}:
	{"type":selectedItem,"points":{"neg":neg,"pos":pos},"value":value});
	
	
	canvas.innerHTML += ((selectedItem != "OpAmp")?
	(`<div class="canvas-element"
	style="left:${coord.x}px;top:${coord.y}px;">
	<p>${value}</p>
	<div class="inner-el">
	<p>${neg}</p>
	<img class="canvas-img" src="${'./static/img/' + selectedItem + '.png'}">
	<p>${pos}</p>
	</div>
	</div>`):
	(`	<div class="opamp-in-canvas canvas-element"
	style="left:${coord.x}px;top:${coord.y}px;">
	<div class="opamp-sidebar">
	<p>${pos}</p>
	<p>${neg}</p>
	</div>
	<img src="./static/img/OpAmp.png" class="canvas-img">
	<p>${out}</p>
	</div>`))
	console.log(canvasElements);
}

$("#node-form").submit(()=>{
	$.ajaxSetup({
		async: false
	});
	const prevs = [];
	$.ajax({
		data: $(this).serialize(),
		type: 'POST',
		url: '/calculate',
		success: (data)=>{
			const prevHTML = $("#node-nums").html();
			$("#node-nums").html('<div id="ans">' + JSON.stringify(data) + '</div>'
								+ '<button id="reset-btn">Reset</button>');
			console.log('data : ', data);
			prevs.push(prevHTML);
			// setTimeout(()=>{
			// 	$("#ans").html(prevHTML);
			// },5000);
		}
	});
	$("#reset-btn").on('click', ()=>{
		$("#ans").html(prevs[0]);
		$(".canvas-element").remove();
		$.ajax({
			type: 'POST',
			url: '/reset'
		});
	});
	return false;
});