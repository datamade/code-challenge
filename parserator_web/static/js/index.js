document.addEventListener('DOMContentLoaded', function() {
   document.querySelector('form').addEventListener('submit', function(event) {
         event.preventDefault();

         var address = document.querySelector('#address').value;

         fetch('/api/parse?address=' + encodeURIComponent(address), {
            headers: {
               'X-CSRFToken': document.querySelector('[name=csrfmiddlewaretoken]').value
            }
         })
         .then(response => response.json())
         .then(data => {
            var resultsDiv = document.getElementById('address-results');
            var resultsTableBody = resultsDiv.querySelector('tbody');
            var parseType = document.getElementById('parse-type');

            resultsTableBody.innerHTML = ''; // Clear previous results

            if (data.error) {
               resultsDiv.style.display = 'block';
               parseType.innerText = 'Error';
               resultsTableBody.innerHTML = '<tr><td colspan="2">' + data.error + '</td></tr>';
            } else {
               resultsDiv.style.display = 'block';
               parseType.innerText = data.address_type;

               var components = data.address_components;
               for (var part in components) {
                     var row = document.createElement('tr');
                     var partCell = document.createElement('td');
                     var tagCell = document.createElement('td');
                     partCell.innerText = part;
                     tagCell.innerText = components[part];
                     row.appendChild(partCell);
                     row.appendChild(tagCell);
                     resultsTableBody.appendChild(row);
               }
            }
         })
         .catch(error => {
            console.error('Error:', error);
         });
   });
});
