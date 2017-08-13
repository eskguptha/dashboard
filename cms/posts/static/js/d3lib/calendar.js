function init_calendar_plot(element_id, calendar_data) {

    var first_key = Object.keys(calendar_data)[0]
    var calendar_min = calendar_data[first_key];
    var calendar_max = calendar_data[first_key];
    for(k in calendar_data) {
      if(calendar_data[k] > calendar_max) calendar_max = calendar_data[k];
      if(calendar_data[k] < calendar_min) calendar_min = calendar_data[k];
    }
    var max = 5;
    if(Object.keys(calendar_data).length < 10) max = Object.keys(calendar_data).length;
    var step = Math.floor((calendar_max - calendar_min) / max);
    var legend = [];
    if(step == 0) {
        step = 1;
        legend.push(calendar_max);
    }
    for(i = calendar_min + step; i<= calendar_max - step; i = i+step) {
        legend.push(i);
    }

    var dt = new Date();
    dt.setMonth(dt.getMonth()-11);
    var calendar = new CalHeatMap();
    calendar.init({
        data: calendar_data,
        start: new Date(dt.getFullYear(), dt.getMonth()),
        itemSelector: '#'+element_id,
        domain : "month",
        subDomain : "x_day",
        range : 12,
        cellSize: 10,
        cellPadding: 2,
        cellRadius: 2,
        domainMargin: 4,
        legend: legend,
        domainDynamicDimension: false,
        tooltip: true,
    });
}
