const url_api = `http://localhost:5000/api/query_data`;
let data_api = null;

document.querySelector('#search').addEventListener('click', e => {
    let value_search = document.querySelector('#input_search').value.toLowerCase();
    let list_theme = null;
    list_theme = data_api.filter( x => x.theme === value_search )
    add_data_html(list_theme);
});


document.querySelectorAll('i.main_icon.fab').forEach(e => {
    e.addEventListener("click", () => {
        let list_theme = null;
        list_theme = data_api.filter( x => x.theme === e.dataset.theme );
        if ( e.dataset.theme === 'all' ) {
            add_data_html(data_api);
        } else {
            add_data_html(list_theme);
        }
    })
});


function add_data_html(data_list) {
    const div_main = document.querySelector('div.main_container');
    div_main.innerHTML = '';
    if ( data_list <= 0 ) {
        div_main.innerHTML += 'Rien';
        return;
    } else {
        for(let key in data_list) {
            div_main.innerHTML += `<div class="video_link">${data_list[key].lien}</div>`;
        }
        document.querySelectorAll('iframe').forEach(e => {
            e.removeAttribute('width');
            e.removeAttribute('height');
        })
    }
}


async function getData(url) {
    const response = await fetch(url);
    data_api = await response.json()
    add_data_html(data_api);
    return data_api;
}

getData(url_api);
