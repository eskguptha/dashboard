function init_map_plot(element_id, map_data, map_features) {
    var map_container = d3.select("#"+element_id);

    var impressionsById = {};
    var namesById = {};
    var div = d3.select("body").append("div")
        .attr("id", "map-tip")
        .attr("class", "custom-tip")
        .style("opacity", 0);
    map_data.forEach(function(d) {
      impressionsById[d.id] = d.impressions;
      namesById[d.id] = d.name;
    });

    var width = parseInt(map_container.style('width')),
        height = parseInt(map_container.style('height'));

    var colours = ["#D4F7E6","#A8F0CC","#7DE8B3","#52E099","#26D980","#1FAD66","#17824D","#0F5733"];

    var heatmapColour = d3.scale.linear()
      .domain(d3.range(0, 1, 1.0 / (colours.length - 1)))
      .range(colours);

    // dynamic bit...
    var c = d3.scale.linear().domain(d3.extent(map_data, function(d) { return d.impressions;})).range([0,1]);

    var projection = d3.geo.mercator()
        .center([10, -5])
        .scale(100)
        .translate([width/2, height/1.5])
        .rotate([0,0]);

    var svg = map_container.append("svg")
        .attr("width", width)
        .attr("height", height);

    var path = d3.geo.path()
        .projection(projection);

    var g = svg.append("g");

    // load and display the World
    d3.json(map_features, function(error, topology) {
        g.selectAll("path")
          .data(topojson.object(topology, topology.objects.countries)
          .geometries)
          .enter()
          .append("path")
          .attr("d", path)
          .attr("fill", function(d) {
              if(impressionsById[d.id]) {
                  return heatmapColour(c(impressionsById[d.id]));
              } else {return "#CCC"}
           })
          .on("mouseover", function(d) {
              if(impressionsById[d.id]) {
                  div.transition()
                        .duration(200)
                        .style("opacity", .9);
                  div.html(namesById[d.id] + "<br/>"  + impressionsById[d.id])
                        .style("left", (d3.event.pageX) + "px")
                        .style("top", (d3.event.pageY - 40) + "px");
              }
          })
          .on("mouseout", function(d) {
              div.transition()
                  .duration(500)
                  .style("opacity", 0);
          });
    });
}
