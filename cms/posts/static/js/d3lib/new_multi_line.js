function multi_line_plot(element_id, line_data) {
    colors = d3.scale.category20()
    j=0
    var svg = d3.select("#"+element_id).append("svg")
              .attr("width", 950)
              .attr("height", 160);
    var margin = {top: 0, right: 0, bottom: 20, left: 0},
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
    
    line_data.forEach(function(d) {
    for (property in d) {
        var data = Array();
        i = 0

        for (each in d[property]){
            data[i] = {date:parseDate(each),value:(+d[property][each]/1000000),key:property}
            i++;
        }
        x.domain(d3.extent(data, function(d) { return d.date; }));
        y.domain(d3.extent(data, function(d) { return d.value; }));

        svg.append("path")
          .style("stroke", colors(j))
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
            .style("fill", colors(j))
            .on("mouseover", function(d) {
                div.transition()
                    .duration(200)
                    .style("opacity", .9);
                div.html(formatTime(d.date) + "<br/>"+d.key+": "+ parseInt(d.value * 1000000))
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
            .style("fill", colors(j))
            .style('opacity', 0.9)
            .attr('cx', function(d) { return x(d.date) })
            .attr('cy', function(d) { return y(d.value) })
            .attr('r', function() { return 4; });
        j++;
        }        
        });

        
    

}
