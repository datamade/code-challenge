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
      var preparedAddress = address.replaceAll(" ", "+");
      var response = await fetch("api/parse?address=" + preparedAddress);
      if (response.ok) {
         var parseResponse = response.json();
         writeResults(parseResponse);
      } else {
         showError();
      }
   } catch (error) {
      showError();
   }
}

function writeResults(parseResponse) {
   // Write Address Type text
   $("#parse-type").text(parseResponse.address_type);

   // TODO Write Address Components table
   console.log(parseResponse.address_components)

   showResults();
}

function showResults() {
   showOrHideById("error", false)
   showOrHideById("address-results", true)
}

function showError() {
   showOrHideById("address-results", false)
   showOrHideById("error", true)
}

function showOrHideById(id, show) {
   var setting = show ? '' : 'none';
   $(`#${id}`).css("display", setting);
}
