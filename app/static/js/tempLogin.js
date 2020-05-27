"use strcit";
let url = `${location.protocol}//${location.hostname}${(location.port ? ':'+location.port : '')}`;
console.log(url);
$(() => {
    $("#signin").click(event => signin(event));
});

function signin(event) {
    window.location.href = `${url}/admin`;
}