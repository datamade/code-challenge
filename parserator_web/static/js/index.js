/* TODO: Flesh this out to connect the form to the API and render results
   in the #address-results div. */
// URL for the local API endpoint
const url = "http://localhost:8000/api/parse"; // TODO: Change this URL in production

// Get the submit button element by its ID
const submitButton = document.getElementById("submit");

// Save the blank HTML for the results table to reset it later
let blankTable = document.getElementById("address-table").innerHTML;

submitButton.onclick = async function(event) {
    event.preventDefault(); // Prevent the default form submission behavior

    // Get the results div element by its ID
    let results = document.getElementById("address-results");

    // Hide the results div and reset its content in case of an error
    results.style.display = "none";

    // Get the value from the address input field
    let addressString = document.getElementById("address").value;

    // Create URL query parameters using the address input value
    let queryTerms = new URLSearchParams({ address: addressString });

    try {
        // Fetch the parsed address from the API endpoint with the query parameters
        const response = await fetch(`${url}?${queryTerms}`);

        // Check if the response is ok (status code 200-299)
        if (!response.ok) {
            throw new Error(`HTTP error! Status: ${response.status}`);
        }

        // Parse the JSON response
        const data = await response.json();

        // Display the parsed address components in the results div
        results.innerText = `Parsed Address Components: ${JSON.stringify(data.address_components)}`;
        results.style.display = "block";
    } catch (error) {
        // Display the error message in the results div
        results.innerText = `Error: ${error.message}`;
        results.style.display = "block";
        console.error(`${error} in response to query at ${url}?${queryTerms}`);
    }
};
