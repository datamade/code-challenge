//Probably unnecessary but I have found firing everything off inside a ready listener to be more reliable
$(document).ready(function(){

   //Load our various elements into some variables for ease of typing and readability
   var form = $('form');
   var results = $('#address-results')
   var pt = $('#parse-type')
   var loading = $('#loading')
   var table = $('tbody')

   //Wait for the submit button to be clicked
   form.submit(function(e){
      //Don't automatically reload the page

      e.preventDefault();

      //Show our loading message
      loading.show();

      //Clear our data and hide the table in case this isn't the first query
      table.html('');
      results.hide();

      //Query our API and pass on the form data
      //Could be improved by handling request errors
      $.get("/api/parse", form.serialize())
      .done(function(data){

         //Just currently set up to handle a single generic error
         if (data == "error!"){
            alert("Error: API error or bad address.")
         }
         //If there are no errors, pull our data out and display it!
         else {         
            pt.html(data[1])
            //Loop through each pair in the array and put it in a table row
            $.each(data[0], function(i, line){
                  table.append("<tr><td>" + line[0]+"</td><td>"+line[1]+"</td></tr>")
            })
            //Hide our loading message and display our data
            //Could be improved by having the results wait to fade in until after the loading message is done fading out
            loading.fadeOut();
            results.fadeIn();
         }
      })
   })
   
});