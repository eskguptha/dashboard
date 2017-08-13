function init_barchart_plot(element_id, barchart_data) {
	var split_names =  barchart_data.names;
	var split_values = barchart_data.values;

	var parseDate = d3.time.format("%Y-%m-%d").parse;
	
	var svg = d3.select(element_id).append("svg");

    var margin = {top: 0, right: 0, bottom: 0, left: 0},
    width = parseInt(svg.style('width')) - margin.left - margin.right,
    height = parseInt(svg.style('height')) - margin.top - margin.bottom;

	var x = d3.scale.ordinal()
		.rangeRoundBands([0, width]);

	var y = d3.scale.linear()
		.rangeRound([height, 0]);

	var color = d3.scale.ordinal()
		    .range(["#3880aa","#4da944","#f26522","#c6080d","#672d8b","#ce1797","#d9ce00","#754c24","#2eb9b4","#0e2e42"]);
		
	var xAxis = d3.svg.axis()
		.scale(x)
		.orient("bottom");

	var yAxis = d3.svg.axis()
		.scale(y)
		.orient("right");
	
	// Creating multiple tooltip divs for each charts. One global div is sufficient.
	var div = d3.select("body")
        .append("div")
        .attr("class", "custom-tip");

	svg.append("g")
		.attr("transform", "translate(" + margin.left + "," + margin.top + ")");
	 
	 split_values = split_values.map(type);
	 var layers = d3.layout.stack()(split_names.map(function(c) {
		return split_values.map(function(d) {
		  return {x: d.key, y: d[c], z:c};
		});
	  }));

	  x.domain(layers[0].map(function(d) { return d.x; }));
	  y.domain([0, d3.max(layers[layers.length - 1], function(d) { return d.y0 + d.y; })]).nice();

	  var layer = svg.selectAll(".layer")
		  .data(layers)
		.enter().append("g")
		  .attr("class", "layer")
		  .style("fill", function(d, i) { return color(i); });
	  var formatTime = d3.time.format("%e %b %Y");
	  layer.selectAll("rect")
		  .data(function(d) { return d; })
		.enter().append("rect")
		  .attr("x", function(d) { return x(d.x); })
		  .attr("y", function(d) { return y(d.y + d.y0); })
		  .attr("height", function(d) { return y(d.y0) - y(d.y + d.y0); })
		  .attr("width", x.rangeBand() - 1)
		  .on("mouseover", function(d) {
                div.transition()
                	.duration(200)
                	.style("display","block");
                if(typeof(d.x) != 'string') d.x = formatTime(d.x);
            	div.html("<b>"+d.x+"</b><br/><b>"+d.z+ "</b>: "+d.y)
                	.style("left", (d3.event.pageX - 60) + "px")
                	.style("top", (d3.event.pageY - 50) + "px");
            })
	        .on("mouseout", function(d) {
	            div.transition()
	                .duration(500)
	                .style("display", "none");
	        });

	  svg.append("g")
		  .attr("class", "axis axis--x")
		  .attr("transform", "translate(0," + height + ")")
		  .call(xAxis);

	  svg.append("g")
		  .attr("class", "axis axis--y")
		  .attr("transform", "translate(" + width + ",0)")
		  .call(yAxis);

	function type(d) {
	  if(d.date) d.key = parseDate(d.date);
	  split_names.forEach(function(c) { d[c] = +d[c]; });
	  return d;
	}
}
