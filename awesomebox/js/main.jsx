import React from 'react';
import ReactDOM from 'react-dom';
import Recently_Awesomized from './recently_awesomized';

console.log(document.referrer);

let temp_url = "/api/v1/books/"
window.location.hash = "recently-awesome"

if (document.referrer.indexOf("about") !== -1) {
  temp_url += "?sorted=True"
  window.location.hash = "most-awesome"
}

ReactDOM.render(
  <Recently_Awesomized url={temp_url}/>,
  document.getElementById('reactEntry'),
);
