document.addEventListener("DOMContentLoaded", function () {
    fetch('info.json')
        .then(response => response.json())
        .then(data => {
            const newsTableBody = document.getElementById('news-table-body');

            data.forEach(item => {
                const row = document.createElement('tr');

                const titleCell = document.createElement('td');
                titleCell.textContent = item.judul;

                const categoryCell = document.createElement('td');
                categoryCell.textContent = item.kategori;

                const timeCell = document.createElement('td');
                timeCell.textContent = item.waktu_publish;

                row.appendChild(titleCell);
                row.appendChild(categoryCell);
                row.appendChild(timeCell);

                newsTableBody.appendChild(row);
            });
        })
        .catch(error => {
            console.error('Error fetching JSON: ', error);
        });
});