/* TODO: Flesh this out to connect the form to the API and render results
   in the #address-results div. */
$('#api-parse').on('submit', function(event){
   //prevent page reload on submit
   event.preventDefault();
   //unhide results section
   $('#address-results').show();
   //show loading message
   $('h4').show()
   //clear body of previous results
   $('tbody').html('');
   //clear parse type of previous results
   $('#parse-type').html('');
   //serialize form data
   var form_data = $('#api-parse').serializeArray();
   $.ajax({
      //send get request with data to /api/parse/
      type: 'GET',
      url: '/api/parse/',
      data: form_data,
      success: function(response){
         //parse  json response to javascript array -- index 0 being address object, 1 being string of address type
         var address = JSON.parse(response)
         //hide loading message
         $('h4').hide()
         //show parse type
         $('#parse-type').html(address[1]);
         //if parse type is abmiguous, don't display results
         if (address[1] == 'Ambiguous'){
            $('thead').hide()
            $('tbody').html('Unable to parse results');
         }
         else {
            //for each part of the address object, make a row with the part and the tag
            $.each(address[0], function(part, tag){
               $('thead').show()
               $('tbody').append('<tr><td>'+ part +'</td><td>'+ tag +'</td></tr>')
            })
         }

      },
      error: function(response) {
         $("#address-results").html("Something went wrong!");
     }
   })
})
