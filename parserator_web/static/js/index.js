/* TODO: Flesh this out to connect the form to the API and render results
   in the #address-results div. */

jquery('form').on('submit', function(event){
   /** Connect the HTML form to the API and render results in the
   #address-results div. */

   // Prevent the page from reloading
   event.preventDefault();

   // Clear data from previous queries from the page
   jquery('tbody').html('')
   jquery('#address-results').hide()
   jquery('#error-message').hide()
   
   // Load form data into userInput as a JSON object
   var userInput = jquery('form').serializeArray();

   // * WIP: Catching bad inputs clientside
   // if (jquery('#address').val == ''){
   //    console.log('found it')
   //    jquery('#error-message').html("Please no.")
   //    jquery('#error-message').show()
   //    return false;
   // }

   // GET request to parserator API
   jquery.ajax({
      method: 'GET',
      url: '/api/parse/',
      data: userInput,
      success: function(response){

         // Extract data from GET response object
         var {address_components,address_type,http_error} = response

         if (http_error !== undefined){
            /** Catch exceptions stemming from usaddress */

            // Show error message in the error message div
            jquery('#error-message').html("Uh oh! That doesn't seem to be a valid address.")

            // Hide the address component table
            jquery('#error-message').show()

         } else {
            /**
             * Display address components, their respective tags, and
             * address type for street addresses or ambiguous addresses.*/

            // Extract parsed address components from GET response
            var {address_components,address_type} = response

            /* Fill the address component table: For each address component, 
            append a row to the table with the component and its tag. */
            jquery.each(address_components, function(tag, component){
               jquery('tbody').append('<tr><td>'+component+'</td><td>'+tag+'</td></tr>')
            })
            
            // Show filled address component table
            jquery('#address-results').show();
            
            // Display address type in parse-type
            jquery('#parse-type').html(address_type)

         }
      }
   })
})