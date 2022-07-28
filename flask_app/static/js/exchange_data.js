let tableBody = document.getElementById("tableBody");

function fetchExhangeData(element, event) {
  fetch("https://api.coingecko.com/api/v3/exchanges?per_page=10")
    .then((res) => res.json())
    .then((data) => {
      data.forEach((e) => {
        console.log(e);
        tableBody.innerHTML += `<tr>
                                <td>${e.trust_score}</td>
                                <td>${e.name}</td>
                                <td>${e.trade_volume_24h_btc}</td>
                                <td><a href="${e.url}">Visit ${e.name}</a></td>
                            </tr>`;
      });
    })
    .catch((err) => {
      alert("it didnt work");
      console.log(err);
    });
}

fetchExhangeData();
