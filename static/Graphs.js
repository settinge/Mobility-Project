// Read in data
d3.csv("/Output/cleaneddata.csv").then(function(data) {

  var x = document.getElementById("selDataset");
  var y = document.getElementById("selDataset2");
  for (let i = 0; i < data.length; i++) {
    // Eliminate duplicates
    if (data[i].region != data[i+1].region) {
      var option = document.createElement("option");
      option.text = data[i].region;
      x.add(option);

    }
   

  }

  for (let i = 0; i < data.length; i++) {
    // Eliminate duplicates
    if (data[i].transportation_type != data[i+1].transportation_type) {
      var option = document.createElement("option");
      option.text = data[i].transportation_type;
      y.add(option);

    }

  }

  var inputField = d3.select("#selDataset2");
  inputField.on("change", function () {
    var user_pick_value = d3.event.target.value;
    var select_id = document.getElementById("selDataset");
    let city__pick = select_id.options[select_id.selectedIndex].value;

    // Make sure to change variables below

    console.log(data);
    let country = data.filter(city => city.region == city__pick && city.transportation_type == user_pick_value)
   console.log(country)
    let country_date = country.map(city_date => city_date.date);
    console.log(country_date)
    let country_score = country.map(city_date => city_date.score);
    console.log(country_score)

    
    var trace1 = {
        x: country_date,
        y: country_score,
        type: "line"
      }

      var layout = {
        title: "Country Mobility",
        margin: {
          l: 100,
          r: 100,
          t: 100,
          b: 100
        }
      }

       // // Render the plot to the div tag with id "plot"
     Plotly.newPlot("plot", [trace1], layout);
  }

  

   // let dateDriving = Belgium.map(driving => driving.transportation.)
   // console.log(dateDriving)

});


// var Belgium = data.region == "Belgium"
// console.log(Belgium)
 
//  // // Render the plot to the div tag with id "plot"
//   Plotly.newPlot("plot", [trace1], layout);

