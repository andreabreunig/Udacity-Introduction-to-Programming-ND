// usability of coloring cells when clicked on
function colorMaker(cell) {
 cell.addEventListener('click', function(event) {
   var color = document.getElementById('colorPicker');
   event.target.style.backgroundColor = color.value;
 });
};

// creating the grid
function makeGrid(height, width) {
    var canvas = document.getElementById("pixelCanvas");
    canvas.innerHTML = '';
    for (var y = 0; y < height; y++) {
        var row = document.createElement('tr');
        // loop for each cell
        canvas.appendChild(row);
        for (var x = 0; x < width; x++) {
            var  cell = document.createElement('td');
            row.appendChild(cell);
            colorMaker(cell);
         }
     }
};

// start when clicking on submit button, saving the size of the grid
document.getElementById('sizePicker').onsubmit = function (event) {
  event.preventDefault()
  const height = document.getElementById('inputHeight').value;
  const width = document.getElementById('inputWidth').value;
  makeGrid(height, width);
};
