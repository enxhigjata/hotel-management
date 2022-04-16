function initMap() {
  const tirana = {
    lat: 41.3291,
    lng: 19.8183,
  };

  const map = new google.maps.Map(document.getElementById("map"), {
    zoom: 14,
    center: tirana,
  });

  const marker = new google.maps.Marker({
    position: tirana,
    map: map,
  });
}
