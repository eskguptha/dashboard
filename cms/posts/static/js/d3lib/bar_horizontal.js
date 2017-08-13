function init_bar_horizontal_plot(element_id, bar_keys,bar_values) {

		var colors = ["#3880aa","#4da944","#f26522","#c6080d","#672d8b","#ce1797","#d9ce00","#754c24","#2eb9b4","#0e2e42"];

		var grid = d3.range(25).map(function(i){
			return {'x1':0,'y1':0,'x2':0,'y2':480};
		});

		var tickVals = grid.map(function(d,i){
			if(i>0){ return i*10; }
			else if(i===0){ return "100";}
		});

		var xscale = d3.scale.linear()
						.domain([10,250])
						.range([0,722]);

		var yscale = d3.scale.linear()
						.domain([0,bar_keys.length])
						.range([0,480]);

		var colorScale = d3.scale.quantize()
						.domain([0,bar_keys.length])
						.range(colors);

		var svg = d3.select(element_id)
						.append('svg')
						.attr({'width':600,'height':500});

		var grids = svg.append('g')
						  .attr('id','grid')
						  .attr('transform','translate(150,10)')
						  .selectAll('line')
						  .data(grid)
						  .enter()
						  .append('line')
						  .attr({'x1':function(d,i){ return i*30; },
								 'y1':function(d){ return d.y1; },
								 'x2':function(d,i){ return i*30; },
								 'y2':function(d){ return d.y2; },
							})
						  .style({'stroke':'#adadad','stroke-width':'1px'});

		var	xAxis = d3.svg.axis();
			xAxis
				.orient('bottom')
				.scale(xscale)
				.tickValues(tickVals);

		var	yAxis = d3.svg.axis();
			yAxis
				.orient('left')
				.scale(yscale)
				.tickSize(2)
				.tickFormat(function(d,i){ return bar_keys[i]; })
				.tickValues(d3.range(17));

		var y_xis = svg.append('g')
						  .attr("transform", "translate(150,0)")
						  .attr('id','yaxis')
						  .call(yAxis);

		var x_xis = svg.append('g')
						  .attr("transform", "translate(150,480)")
						  .attr('id','xaxis')
						  .call(xAxis);

		var chart = svg.append('g')
							.attr("transform", "translate(150,0)")
							.attr('id','bars')
							.selectAll('rect')
							.data(bar_values)
							.enter()
							.append('rect')
							.attr('height',19)
							.attr({'x':0,'y':function(d,i){ return yscale(i)+19; }})
							.style('fill',function(d,i){ return colorScale(i); })
							.attr('width',function(d){ return 0; });


		var transit = d3.select("svg").selectAll("rect")
						    .data(bar_values)
						    .transition()
						    .duration(1000) 
						    .attr("width", function(d) {return xscale(d); });

		var transitext = d3.select('#bars')
							.selectAll('text')
							.data(bar_values)
							.enter()
							.append('text')
							.attr({'x':function(d) {return xscale(d)-200; },'y':function(d,i){ return yscale(i)+35; }})
							.text(function(d){ return d; }).style({'fill':'#fff','font-size':'14px'});



}