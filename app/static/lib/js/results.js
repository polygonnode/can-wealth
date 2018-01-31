var svg = d3.select("svg"),
    margin = {top: 20, right: 20, bottom: 30, left: 40},
    width = +svg.attr("width") - margin.left - margin.right,
    height = +svg.attr("height") - margin.top - margin.bottom;

//change the rangeRound to width if u want it to expand
var x = d3.scaleBand().rangeRound([0, 500]).padding(0.1),
    y = d3.scaleLinear().rangeRound([height, 0]);

var g = svg.append("g")
    .attr("transform", "translate(" + margin.left + "," + margin.top + ")");
var data = [
  {date: "1", moneyTowardsGoal: 16020, moneyTowardsGoalPusInterest: 16020+25},
  {date: "2", moneyTowardsGoal: 17042, moneyTowardsGoalPusInterest: 17042+52},
  {date: "3", moneyTowardsGoal: 18066, moneyTowardsGoalPusInterest: 18066+81},
  {date: "4", moneyTowardsGoal: 19092, moneyTowardsGoalPusInterest: 17042+52},
  {date: "5", moneyTowardsGoal: 20119, moneyTowardsGoalPusInterest: 17042+52},
  {date: "6", moneyTowardsGoal: 21149, moneyTowardsGoalPusInterest: 17042+52},
  {date: "7", moneyTowardsGoal: 21149, moneyTowardsGoalPusInterest: 17042+52},
  {date: "8", moneyTowardsGoal: 21149, moneyTowardsGoalPusInterest: 17042+52},
  {date: "9", moneyTowardsGoal: 21149, moneyTowardsGoalPusInterest: 17042+52},
  {date: "10", moneyTowardsGoal: 21149, moneyTowardsGoalPusInterest: 17042+52},
  {date: "11", moneyTowardsGoal: 21149, moneyTowardsGoalPusInterest: 17042+52},
  {date: "12", moneyTowardsGoal: 21149, moneyTowardsGoalPusInterest: 17042+52},
  {date: "13", moneyTowardsGoal: .16, moneyTowardsGoalPusInterest: 17042+52},
];

var test_goal = 50000;
var test_down_payment = 15000;
var test_monthly_payment = 1000;

  x.domain(data.map(function(d) { return d.date; }));
  y.domain([0, test_goal]);

  g.append("g")
      .attr("class", "axis axis--x")
      .attr("transform", "translate(0," + height + ")")
      .call(d3.axisBottom(x));

  g.append("g")
      .attr("class", "axis axis--y")
      .call(d3.axisLeft(y).ticks(10))
    .append("text")
      .attr("transform", "rotate(-90)")
      .attr("y", 6)
      .attr("dy", "0.71em")
      .attr("text-anchor", "end")
      .text("moneyTowardsGoal");

  g.selectAll(".bar")
    .data(data)
    .enter().append("rect")
      .attr("class", "bar")
      .attr("x", function(d) { return x(d.date);})
      .attr("y", function(d) { return y(d.moneyTowardsGoalPusInterest); })
      .attr("width", x.bandwidth())
      .attr("height", function(d) { return height - y(d.moneyTowardsGoalPusInterest); });


  g.selectAll(".bar1")
    .data(data)
    .enter().append("rect")
      .attr("class", "bar1")
      .attr("x", function(d) { return x(d.date); })
      .attr("y", function(d) { return y(d.moneyTowardsGoal); })
      .attr("width", x.bandwidth())
      .attr("height", function(d) { return height - y(d.moneyTowardsGoal); });
