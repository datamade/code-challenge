/* Connects the form to the API and render results
   in the #address-results div. */

$('.form').on('submit', function (event) {
   // Prevent default form submission behavior
   event.preventDefault();

   var address = getAddress();
   submitAddress(address);

});

function getAddress() {
   var address = $("#address").val().trim();
   console.log(`Submitted form with: ${address}`);
   return address;
}

async function submitAddress(address) {
   try {
      // TODO submit results to API properly
      var res = await fetch("api/parse?address=" + address);
      var parseResponse = await res.json();
      renderAddress(parseResponse);
   } catch (error) {
      console.log(error);
   }
}

function renderAddress(parseResponse) {
   console.log(parseResponse.input_string);
   // TODO render results in the #address-results div

   // Write Address Type text
   $("#parse-type").text(parseResponse.address_type);

   // TODO Write Address Components table
   console.log(parseResponse.address_components)

   // Set Address Results div to show
   $("#address-results").css("display", '');
}
