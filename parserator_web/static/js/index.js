/* TODO: Flesh this out to connect the form to the API and render results
   in the #address-results div. */
   document.addEventListener('DOMContentLoaded', () => {
      document.getElementById('submit').addEventListener('click', async (e) => {
          const inputString = document.getElementById('address').value;
          const url = `api/parse/?input_string=${encodeURIComponent(inputString)}`;
          
          try {
              const response = await fetch(url, {
                  method: "GET",
                  headers: {
                      'X-CSRFToken': document.querySelector('[name=csrfmiddlewaretoken]').value,
                  }
              });
   
              if (!response.ok) {
                  throw new Error(`HTTP error! Status: ${response.status}`);
              }
   
              const data = await response.json();
              console.log(data);
          } catch (error) {
              console.error('Error:', error);
          }
      }, false);
   });
   
   