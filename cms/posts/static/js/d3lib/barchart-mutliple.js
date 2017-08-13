function init_multi_barchart_plot(element_id, barchart_data) {
  var svg = d3.select(element_id).append("svg");
  var margin = {top: 20, right: 160, bottom: 35, left: 30};
  var width = 960 - margin.left - margin.right,
      height = 500 - margin.top - margin.bottom;

  var svg = d3.select(element_id)
    .append("svg")
    .attr("width", width + margin.left + margin.right)
    .attr("height", height + margin.top + margin.bottom)
    .append("g")
    .attr("transform", "translate(" + margin.left + "," + margin.top + ")");

  var data = barchart_data.values;
  var column_names = barchart_data.names;

  // Transpose the data into layers
  var dataset = d3.layout.stack()(column_names.map(function(item) {
    return data.map(function(d) {
      return {x: d.key, y: +d[item]};
    });
  }));


  // Set x, y and colors
  var x = d3.scale.ordinal()
    .domain(dataset[0].map(function(d) { return d.x; }))
    .rangeRoundBands([10, width-10], 0.02);

  var y = d3.scale.linear()
    .domain([0, d3.max(dataset, function(d) {  return d3.max(d, function(d) { return d.y0 + d.y; });  })])
    .range([height, 0]);

  var colors = ["#3880aa","#4da944","#f26522","#c6080d","#672d8b","#ce1797","#d9ce00","#754c24","#2eb9b4","#0e2e42"];


  // Define and draw axes
  var yAxis = d3.svg.axis()
    .orient("left")
    
    

  var xAxis = d3.svg.axis()
    .scale(x)
    .orient("bottom")
    .tickFormat( function(d) { return d } );

  svg.append("g")
    .attr("class", "y axis")
    

  svg.append("g")
    .attr("class", "x axis")
    .attr("transform", "translate(0," + height + ")")
    .call(xAxis);


  // Create groups for each series, rects for each segment 
  var groups = svg.selectAll("g.cost")
    .data(dataset)
    .enter().append("g")
    .attr("class", "cost")
    .style("fill", function(d, i) { return colors[i]; });

  var rect = groups.selectAll("rect")
    .data(function(d) { return d; })
    .enter()
    .append("rect")
    .attr("x", function(d) { return x(d.x); })
    .attr("y", function(d) { return y(d.y0 + d.y); })
    .attr("height", function(d) { return y(d.y0) - y(d.y0 + d.y); })
    .attr("width", x.rangeBand())
    .on("mouseover", function() { tooltip.style("display", null); })
    .on("mouseout", function() { tooltip.style("display", "none"); })
    .on("mousemove", function(d) {
      var xPosition = d3.mouse(this)[0] - 15;
      var yPosition = d3.mouse(this)[1] - 25;
      tooltip.attr("transform", "translate(" + xPosition + "," + yPosition + ")");
      tooltip.select("text").text(d.y);
    });


  // Prep the tooltip bits, initial display is hidden
  var tooltip = svg.append("g")
    .attr("class", "tooltip")
    .style("display", "none");
      
  tooltip.append("rect")
    .attr("width", 30)
    .attr("height", 20)
    .attr("fill", "white")
    .style("opacity", 0.5);

  tooltip.append("text")
    .attr("x", 15)
    .attr("dy", "1.2em")
    .style("text-anchor", "middle")
    .attr("font-size", "12px")
    .attr("font-weight", "bold");
}