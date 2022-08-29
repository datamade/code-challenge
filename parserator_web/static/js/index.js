/* TODO: Flesh this out to connect the form to the API and render results
   in the #address-results div. */
const form = document.querySelector("form");

form.addEventListener("submit", (event) => {
  const addressSubmission = form.querySelector("#address").value;
  console.log(addressSubmission);

  fetch("api/parse/?address='" + addressSubmission + "'")
    .then((response) => response.json())
    .then((data) => console.log(data));
});
