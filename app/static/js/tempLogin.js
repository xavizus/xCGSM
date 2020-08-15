"use strcit";
let url = `${location.protocol}//${location.hostname}${(location.port ? ':'+location.port : '')}`;
$(() => {
    $("#signin").click(event => signin(event));
});

function signin(event) {
    let searchParams = new URLSearchParams(window.location.search);
    if (searchParams.has('wantedUrl')) {
        console.log(searchParams.get('wantedUrl'))
        window.location.href = `${url}${searchParams.get('wantedUrl')}`;
        return;
    }
    window.location.href = `${url}/admin`;
}