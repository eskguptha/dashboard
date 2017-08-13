function init_bar_vertical_plot(element_id, data) {
    var svg = d3.select(element_id).append("svg");
		var margin = {top: 10, right: 20, bottom: 10, left: 40},
    width = parseInt(svg.style('width')) - margin.left - margin.right,
    height = parseInt(svg.style('height')) - margin.top - margin.bottom;
    var colors = ["#3880aa","#4da944","#f26522","#c6080d","#672d8b","#ce1797","#d9ce00","#754c24","#2eb9b4","#0e2e42"];
    
  svg.append("g")
    .attr("transform", 
          "translate(" + margin.left + "," + margin.top + ")");
    data.forEach(function(d) {
        d.segment = d.segment;
        d.value = +d.value;
    });
  

var x = d3.scale.ordinal().rangeRoundBands([0, width], .05);

var y = d3.scale.linear().range([height, 0]);

var xAxis = d3.svg.axis()
    .scale(x)
    .orient("bottom")

var yAxis = d3.svg.axis()
    .scale(y)
    .orient("left")
    .ticks(10);

var div = d3.select("body")
        .append("div")
        .attr("class", "custom-tip");


  x.domain(data.map(function(d) { return d.segment; }));
  y.domain([0, d3.max(data, function(d) { return d.value; })]);


  svg.append("g")
      .attr("class", "x axis")
      .attr("transform", "translate(0," + height + ")")
      .call(xAxis)
    .selectAll("text")
      .style("text-anchor", "end")
      .attr("dx", "35")
      .attr("dy", "5");

  svg.append("g")
      .attr("class", "y axis")
      .call(yAxis)
    .append("text")
      .attr("transform", "rotate(-90)")
      .attr("y", 6)
      .attr("dy", ".71em")
      .style("text-anchor", "end");


  svg.selectAll("bar")
      .data(data)
    .enter().append("rect")
      .style("fill", "#3880aa")
      .attr("x", function(d) { return x(d.segment); })
      .attr("width", x.rangeBand())
      .attr("y", function(d) { return y(d.value); })
      .attr("height", function(d) { return height - y(d.value); })
      .on("mouseover", function(d) {
                div.transition()
                .duration(200)
                .style("display","block");
            div.html(""+d.segment + "<br/><b>Count</b>: "+d.value)
                .style("left", (d3.event.pageX - 60) + "px")
                .style("top", (d3.event.pageY - 50) + "px");
            })
          .on("mouseout", function(d) {
              div.transition()
                  .duration(500)
                  .style("display", "none");
          });
}