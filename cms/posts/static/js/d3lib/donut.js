function init_donut_plot(element_id, donut_data, opts) {
    var width = 280,
    height = 168,
    radius = Math.min(width, height) / 2;

    var color = d3.scale.ordinal()
        .range(["#3880aa","#4da944","#f26522","#c6080d","#672d8b","#ce1797","#d9ce00","#754c24","#2eb9b4","#0e2e42"]);
    var arc = d3.svg.arc()
        .outerRadius(radius - 10)
        .innerRadius(radius - 30);
    var pie = d3.layout.pie()
        .value(function(d) { return d.count; })
        .sort(null);

    var svg = d3.select("#" + element_id).append("svg")
        .attr("width", width)
        .attr("height", height)
        .append("g")
        .attr("transform", "translate(" + 75 + "," + height / 2 + ")");
    
    var div = d3.select("body")
        .append("div")
        .attr("class", "custom-tip");

    var path = svg.datum(donut_data).selectAll("path")
      .data(pie)
      .enter().append("path")
      .attr("fill", function(d, i) { if (d.data.count > 0) return color(d.data.key); })
      .attr("d", arc)
      .on("mousemove",function(d){
                var mouseVal = d3.mouse(this);
                div.style("display","none");
                div
                .html(d.data.key+"</br>"+d.data.count)
                .style("left", (d3.event.pageX+12) + "px")
                .style("top", (d3.event.pageY-10) + "px")
                .style("display","block");
            })
      .on("mouseout",function(){div.html(" ").style("display","none");})
      .each(function(d) { this._current = d; });

    if(opts.legend != false) {
        var legend = svg.append("g")
        .attr("class", "legend")
        .attr("width", radius * 2)
        .attr("height", radius * 2)
        .selectAll("g")
        .data(color.domain().slice())
        .enter().append("g")
        .attr("transform",
        function(d, i) {
            return "translate(80," + ((i * 15) - radius) + ")";
        });

        legend.append("rect")
        .attr("width", 14)
        .attr("height", 14)
        .style("fill", color);

        legend.append("text")
        .attr("x", 20)
        .attr("y", 8)
        .attr("dy", ".25em")
        .text(function(d) {
            return d.toString().substr(0, 20);
        });
    }
}