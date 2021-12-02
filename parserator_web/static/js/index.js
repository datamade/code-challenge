$('form').on('submit', function (event) {
  /** Connect the HTML form to the API and render results in the
  #address-results div. */

  // Prevent the page from reloading
  event.preventDefault()

  // Clear data from previous queries from the page
  $('tbody').html('')
  $('#address-results').hide()
  $('#error-message').hide()

  // Load form data into userInput as a JSON object
  var userInput = $('form').serializeArray()

  // * WIP: Catch obviously bad inputs clientside
  // if ($('#address').val == ''){
  //    console.log('found it')
  //    $('#error-message').html("Please no.")
  //    $('#error-message').show()
  //    return false;
  // }

  // GET request to parserator API
  $.ajax({
    method: 'GET',
    url: '/api/parse/',
    data: userInput,
    success: function (response) {
      /**
       * Display address components, their respective tags, and
       * address type for street addresses or ambiguous addresses.*/

      // Extract data from GET response object
      // pytest Does Not Like this syntax, but from what I can tell it's okay.
      var {address_components,address_type} = response

      /* Fill the address component table: For each address component,
      append a row to the table with the component and its tag. */
      $.each(address_components, function (tag, component) {
        $('tbody').append('<tr><td>'+component+'</td><td>'+tag+'</td></tr>')
      })

      // Show filled address component table
      $('#address-results').show()

      // Display address type in parse-type
      $('#parse-type').html(address_type)
    },
    statusCode: {
      400: function () {
      /** Catch exceptions stemming from usaddress parseError */

        // Show error message in the error message div
        $('#error-message').html("Uh oh! That doesn't seem to be a valid address.")

        // Hide the address component table
        $('#error-message').show()
      }
    }
  })
})