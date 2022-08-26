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
      var data = await res.json();
      console.log(res);
      renderAddress("Address Type", []);
   } catch (error) {
      console.log(error);
   }
}

function renderAddress(addressType, addressComponents) {
   // TODO render results in the #address-results div

   // Write Address Type text
   $("#parse-type").text(addressType);

   // TODO Write Address Components table

   // Set Address Results div to show
   $("#address-results").css("display", '');
}
