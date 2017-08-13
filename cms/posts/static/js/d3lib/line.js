function init_line_plot(element_id, line_data) {

    var svg = d3.select("#"+element_id).append("svg");

    var margin = {top: 0, right: 0, bottom: 0, left: 0},
    width = parseInt(svg.style('width')) - margin.left - margin.right,
    height = parseInt(svg.style('height')) - margin.top - margin.bottom;

    var parseDate = d3.time.format("%Y-%m-%d").parse;

    var x = d3.time.scale()
        .range([5, width]);

    var y = d3.scale.linear()
        .range([height, 5]);

    var xAxis = d3.svg.axis()
        .scale(x)
        .orient("bottom");

    var yAxis = d3.svg.axis()
        .scale(y)
        .orient("left");

    var line = d3.svg.line()
        .interpolate("cardinal")
        .x(function(d) { return x(d.date); })
        .y(function(d) { return y(d.value); });


    svg.append("g").attr("transform", "translate(" + margin.left + "," + margin.top + ")");

    var data = Array();
    line_data.forEach(function(d) {
    i = 0
    for (property in d) {
        data[i] = {date:parseDate(property),value:(+d[property]/1000000)}
        i++;
    }
    });

    x.domain(d3.extent(data, function(d) { return d.date; }));
    y.domain(d3.extent(data, function(d) { return d.value; }));

    svg.append("path")
      .datum(data)
      .attr("class", "line")
      .attr("d", line);

    dataDotsGroup = svg.append('g');
    var dots = dataDotsGroup.selectAll('.data-point').data(data);
    var div = d3.select("body").append("div")
        .attr("class", "tooltip")
        .style("opacity", 0);
    var formatTime = d3.time.format("%e %b %Y");
    dots.enter().append('circle')
        .style('opacity', 0)
        .attr("r", 20)
        .attr("cx", function(d) { return x(d.date); })
        .attr("cy", function(d) { return y(d.value); })
        .on("mouseover", function(d) {
            div.transition()
                .duration(200)
                .style("opacity", .9);
            div.html(formatTime(d.date) + "<br/>"  + parseInt(d.value * 1000000))
                .style("left", (d3.event.pageX - 60) + "px")
                .style("top", (d3.event.pageY - 50) + "px");
            })
        .on("mouseout", function(d) {
            div.transition()
                .duration(500)
                .style("opacity", 0);
        });

    dataCirclesGroup = svg.append('g');
    var circles = dataCirclesGroup.selectAll('.data-point').data(data);
    circles.enter().append('circle')
        .attr('class', 'data-point')
        .style('opacity', 0.9)
        .attr('cx', function(d) { return x(d.date) })
        .attr('cy', function(d) { return y(d.value) })
        .attr('r', function() { return 4; });

}
