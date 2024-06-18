document.addEventListener("DOMContentLoaded", function() {
    const mntoggle = document.querySelector('.menu-toggle input');
    const nav = document.querySelector('nav ul');

    mntoggle.addEventListener('click', function() {
        nav.classList.toggle('menushow');
    });

    function updateHeadline() {
        $.get('./pertemuan_8/headline.json', function(obj) {
            const headlines = obj.split('\n');
            let str = '';

            for (let i = 0; i < headlines.length; i++) {
                str += `${headlines[i]}<br>`;
            }
            $('#headline_text').html(str);
        });
    }

    function addItems(kat, jud, pub, up) {
        const table = document.getElementsByTagName('table')[0];
        const newRow = table.insertRow(1);

        const cel1 = newRow.insertCell(0);
        const cel2 = newRow.insertCell(1);
        const cel3 = newRow.insertCell(2);
        const cel4 = newRow.insertCell(3);

        cel1.innerHTML = kat;
        cel2.innerHTML = jud;
        cel3.innerHTML = pub;
        cel4.innerHTML = up;
    }

    function fetchJSONData() {
        fetch("./info.json")
            .then(res => {
                if (!res.ok) {
                    throw new Error(`HTTP error! Status: ${res.status}`);
                }
                return res.json();
            })
            .then(data => {
                data.forEach(item => {
                    addItems(item.kategori, item.judul, item.waktu, item.update);
                });
            })
            .catch(error => console.error("Unable to fetch data:", error));
    }

    updateHeadline();
    fetchJSONData();
});
