// Define the class names of the divs
const divClassName = '.sc-gQeIUl.breHMb';
const percentageClassName = '.sc-dTHgTJ.gGGPgR.sc-bZpYCy.hUNKvs span';

// Get all the divs into a node list
let divs = document.querySelectorAll(divClassName);

// Convert the node list to an array
divs = Array.from(divs);

// Sort the array based on the percentage
divs.sort((a, b) => {
    const percentageA = a.querySelector(percentageClassName).innerText.replace('%', '').replace('-', '');
    const percentageB = b.querySelector(percentageClassName).innerText.replace('%', '').replace('-', '');

    return percentageB - percentageA; // Descending order
});

// Get the parent element
let parent = divs[0].parentNode;

// Remove all the divs
for (let div of divs) {
    parent.removeChild(div);
}

// Add the divs back in sorted order
for (let div of divs) {
    parent.appendChild(div);
}
