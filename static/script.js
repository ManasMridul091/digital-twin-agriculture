let tempData = [], humData = [], rainData = [], yieldData = [];
let labels = [];

function createChart(id, label, dataArray) {
    return new Chart(document.getElementById(id), {
        type: 'line',
        data: {
            labels: labels,
            datasets: [{
                label: label,
                data: dataArray,
                borderWidth: 2,
                tension: 0.4 // smooth curves
            }]
        }
    });
}

const tempChart = createChart("tempChart", "Temperature", tempData);
const humChart = createChart("humChart", "Humidity", humData);
const rainChart = createChart("rainChart", "Rainfall", rainData);
const yieldChart = createChart("yieldChart", "Yield", yieldData);

// 🔴 Live simulation
setInterval(() => {
    fetch('/get_data')
    .then(res => res.json())
    .then(data => {

        labels.push("T" + labels.length);
        tempData.push(data.temperature);
        humData.push(data.humidity);
        rainData.push(data.rainfall);
        yieldData.push(data.yield);

        if (labels.length > 10) {
            labels.shift();
            tempData.shift();
            humData.shift();
            rainData.shift();
            yieldData.shift();
        }

        tempChart.update();
        humChart.update();
        rainChart.update();
        yieldChart.update();

        document.getElementById("insights").innerHTML =
            `🌾 Crop: ${data.crop}<br>
             💧 Irrigation: ${data.irrigation}<br>
             📈 Yield: ${data.yield}`;
    });
}, 2000);


// Prediction
function predict() {
    fetch('/predict', {
        method: 'POST',
        headers: {'Content-Type': 'application/json'},
        body: JSON.stringify({
            N: 50, P: 50, K: 50,
            temperature: document.getElementById('temp').value,
            humidity: document.getElementById('humidity').value,
            ph: 6.5,
            rainfall: document.getElementById('rainfall').value
        })
    })
    .then(res => res.json())
    .then(data => {
        document.getElementById("result").innerText =
            "🌾 Predicted Crop: " + data.crop;
    });
}