/* TODO: Flesh this out to connect the form to the API and render results
   in the #address-results div. */
   document.addEventListener('DOMContentLoaded', function() {
      const form = document.querySelector('form');
      const addressResults = document.getElementById('address-results');
  
      form.addEventListener('submit', function(e) {
          e.preventDefault();
          const address = document.getElementById('address').value;
  
          // Send request to API endpoint
          fetch(`/api/parse/?address=${encodeURIComponent(address)}`)
              .then(response => response.json())
              .then(data => {
                  // Clear previous results
                  addressResults.innerHTML = '';
                  addressResults.style.display = 'block';
  
                  if (data.detail && data.detail.startsWith('Error parsing address:')) {
                      // Display parsing error
                      const errorMessage = data.detail.split('ORIGINAL STRING:')[0].trim();
                      addressResults.innerHTML = `
                          <h4>Parsing Error</h4>
                          <p class="text-danger">${errorMessage}</p>
                          <p>The address could not be parsed. This may be due to:</p>
                          <ul>
                              <li>Duplicate address components</li>
                              <li>Invalid address format</li>
                          </ul>
                          <p>Please check the address and try again.</p>
                      `;
                  } else if (data.address_components) {
                      // Display successful results
                      addressResults.innerHTML = `
                          <h4>Parsing results</h4>
                          <p>Address type: <strong>${data.address_type}</strong></p>
                          <p>Input: <strong>${data.input_string}</strong></p>
                          <table class="table table-bordered">
                              <thead>
                                  <tr>
                                      <th>Address part</th>
                                      <th>Tag</th>
                                  </tr>
                              </thead>
                              <tbody>
                              </tbody>
                          </table>
                      `;
  
                      const resultsTable = addressResults.querySelector('tbody');
  
                      // Add new results
                      for (const [part, tag] of Object.entries(data.address_components)) {
                          const row = resultsTable.insertRow();
                          const cellPart = row.insertCell(0);
                          const cellTag = row.insertCell(1);
                          cellPart.textContent = part;
                          cellTag.textContent = tag;
                      }
                  } else {
                      // Unexpected response format
                      addressResults.innerHTML = `
                          <h4>Parsing Error</h4>
                          <p class="text-danger">An unexpected error occurred. Please try again.</p>
                      `;
                  }
              })
              .catch(error => {
                  console.error('Error:', error);
                  addressResults.style.display = 'block';
                  addressResults.innerHTML = `
                      <h4>Parsing Error</h4>
                      <p class="text-danger">An unexpected error occurred. Please try again.</p>
                  `;
              });
      });
  });
